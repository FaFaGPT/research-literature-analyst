"""Small shared helpers for offline repository and Obsidian checks."""

import re
import os
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    raise SystemExit("Install validation dependency: python -m pip install -r scripts/requirements.txt")

IGNORE = {".git", ".obsidian", ".tools", ".venv", "__pycache__"}
PLACEHOLDER = re.compile(r"(?<!\$)\{\{[^{}\n]+\}\}")
READING_STATUSES = {"metadata-only", "abstract-only", "partial-full-text", "full-text"}


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError("duplicate YAML key: " + str(key))
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def load_yaml(text):
    return yaml.load(text, Loader=UniqueLoader)


def files(root):
    return sorted(p for p in root.rglob("*") if p.is_file()
                  and not any(part in IGNORE for part in p.relative_to(root).parts))


def frontmatter(text):
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return {}, text
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            data = load_yaml("".join(lines[1:index]))
            if not isinstance(data, dict):
                raise ValueError("front matter must be a YAML mapping")
            return data, "".join(lines[index + 1:])
    raise ValueError("unclosed YAML front matter")


def prose(text, inline=True):
    """Ignore fenced code and optionally inline code when checking doc examples."""
    result, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if match:
            marker, suffix = match.groups()
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not suffix.strip():
                fence = None
            continue
        if fence is None:
            result.append(line)
    if fence is not None:
        raise ValueError("unclosed Markdown code fence")
    result = "\n".join(result)
    return re.sub(r"(`+).*?\1", "", result) if inline else result


def structure_errors(body):
    try:
        content = prose(body)
    except ValueError as error:
        return [str(error)]
    errors = []
    if len(re.findall(r"^#\s+\S", content, re.M)) != 1:
        errors.append("expected exactly one level-one Markdown heading")
    if re.search(r"^#{7,}\s", content, re.M):
        errors.append("heading deeper than level six")
    return errors


def invalid_windows_name(name):
    stem = name.split(".")[0].upper()
    reserved = stem in {"CON", "PRN", "AUX", "NUL"} or bool(re.fullmatch(r"(?:COM|LPT)[1-9¹²³]", stem))
    return bool(re.search(r'[<>:"/\\|?*\x00-\x1f]', name) or name.endswith((" ", ".")) or reserved)


def filename_errors(root):
    errors, seen = [], {}
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if any(part in IGNORE for part in rel.parts):
            continue
        name = path.name
        if invalid_windows_name(name):
            errors.append(f"{rel}: invalid Windows filename")
        key = rel.as_posix().casefold()
        if key in seen:
            errors.append(f"{rel}: case-insensitive path collision with {seen[key]}")
        seen[key] = rel
    return errors


class HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        self.targets.extend(value for key, value in attrs if key in {"src", "href"} and value)


def markdown_targets(content):
    # Inline destinations support escaped characters, spaces in <...>, one
    # nested parenthesis level, and an optional quoted title.
    target = r'<[^>]+>|(?:\\.|[^\s()<>]|\([^()]*\))+'
    targets = [m.group(1).strip("<>") for m in re.finditer(
        r'!?\[[^\]\n]*\]\(\s*(' + target + r')(?:\s+["\'][^\n]*?["\'])?\s*\)', content)]
    definitions = {}
    for match in re.finditer(r'^\s*\[([^\]]+)\]:\s*(<[^>]+>|\S+)', content, re.M):
        definitions[match.group(1).strip().casefold()] = match.group(2).strip("<>")
    targets.extend(definitions.values())
    missing = []
    for match in re.finditer(r'!?\[([^\]\n]+)\]\[([^\]\n]*)\]', content):
        label = (match.group(2) or match.group(1)).strip().casefold()
        if label not in definitions:
            missing.append("undefined reference link: " + label)
    parser = HTMLLinks()
    parser.feed(content)
    targets.extend(parser.targets)
    return targets, missing


def heading_names(text):
    _, body = frontmatter(text)
    return [re.sub(r'\s+#+\s*$', '', m.group(1)).strip()
            for m in re.finditer(r'^#{1,6}\s+(.+)$', prose(body, inline=False), re.M)]


def github_anchors(headings):
    used, anchors = {}, set()
    for heading in headings:
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        index = used.get(slug, 0)
        used[slug] = index + 1
        anchors.add(slug + ("-" + str(index) if index else ""))
    return anchors


def property_strings(data):
    """Read property values without YAML serialization wrapping long links."""
    pending, seen = [data], set()
    while pending:
        value = pending.pop()
        if isinstance(value, str):
            yield value
        elif isinstance(value, (dict, list)) and id(value) not in seen:
            seen.add(id(value))
            pending.extend(value.values() if isinstance(value, dict) else value)


def link_errors(root, wiki=False):
    paths = files(root)
    known = {p.relative_to(root).as_posix(): p for p in paths}
    # Exact spelling matters even when checks run on Windows.
    def exact(path):
        try:
            path.resolve().relative_to(root.resolve())
            name = Path(os.path.abspath(path)).relative_to(root).as_posix()
        except ValueError:
            return None
        if name in known:
            return known[name]
        if any(k.startswith(name.rstrip('/') + '/') for k in known):
            return path if path.is_dir() else None
        return None

    errors = []
    for source in paths:
        if source.suffix.lower() != ".md":
            continue
        try:
            text = source.read_text(encoding="utf-8-sig")
            data, body = frontmatter(text)
            content = prose(body)
            targets, reference_errors = markdown_targets(content)
            errors.extend(f"{source.relative_to(root)}: {e}" for e in reference_errors)
            for target in targets:
                target = re.sub(r"\\([ ()])", r"\1", target)
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc:
                    continue
                name = unquote(parsed.path)
                destination = exact((root / name.lstrip('/')) if name.startswith('/') else source.parent / name) if name else source
                if destination is None:
                    errors.append(f"{source.relative_to(root)}: broken local link {target}")
                elif parsed.fragment and destination.suffix == ".md":
                    anchors = github_anchors(heading_names(destination.read_text(encoding="utf-8-sig")))
                    if unquote(parsed.fragment) not in anchors:
                        errors.append(f"{source.relative_to(root)}: missing heading {target}")
            if not wiki:
                continue
            # Properties may contain quoted wikilinks; include them as well.
            property_text = '\n'.join(property_strings(data))
            for target in re.findall(r'!?\[\[([^\]\n]+)\]\]', content + '\n' + property_text):
                address = target.replace('\\|', '|').split('|', 1)[0]
                name, _, fragment = address.partition('#')
                name = unquote(name)
                if not name:
                    candidates = [source]
                else:
                    # A dot can be part of a note title, as in [[Method.v2]].
                    names = [name] if name.endswith('.md') else [name, name + '.md']
                    direct = [exact(root / n) if '/' in n else exact(source.parent / n) for n in names]
                    candidates = [p for p in direct if p is not None and p.is_file()]
                    if not candidates:
                        candidates = [p for p in paths if p.name in names]
                if len(candidates) != 1 or candidates[0] is None:
                    errors.append(f"{source.relative_to(root)}: broken or ambiguous wikilink {target}")
                    continue
                destination = candidates[0]
                if fragment and destination.suffix == '.md':
                    dest_text = destination.read_text(encoding="utf-8-sig")
                    if fragment.startswith('^'):
                        valid = bool(re.search(r'\^' + re.escape(fragment[1:]) + r'\s*$', dest_text, re.M))
                    else:
                        valid = all(part in heading_names(dest_text) for part in fragment.split('#'))
                    if not valid:
                        errors.append(f"{source.relative_to(root)}: missing wikilink heading/block {target}")
        except (ValueError, TypeError, yaml.YAMLError, UnicodeError) as error:
            errors.append(f"{source.relative_to(root)}: {error}")
    return errors


def finish(errors, label):
    if errors:
        print('\n'.join('ERROR: ' + error for error in errors))
        print(f"FAIL: {label} ({len(errors)} issue(s))")
        return 1
    print("PASS: " + label)
    return 0
