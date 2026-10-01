"""Validate the skill package, template YAML, and basic Markdown structure."""

import argparse
from pathlib import Path
import yaml
from _validation import (PLACEHOLDER, files, filename_errors, finish,
                         frontmatter, load_yaml, prose, structure_errors)

TEMPLATES = {"topic-map.md", "paper-note.md", "direction-note.md", "concept-note.md", "reading-queue.md", "claim-note.md", "evidence-matrix.md"}
REQUIRED = {"README.md", "README.zh-CN.md", "SKILL.md", "agents/openai.yaml", "LICENSE",
            "CITATION.cff", "CHANGELOG.md", "CONTRIBUTING.md", ".github/workflows/validate.yml",
            "benchmarks/README.md", "examples/README.md", "docs/usage.md",
            "references/reading-depth.md", "references/search-and-update.md", "references/obsidian-format.md",
            "references/evidence-synthesis.md"}


def validate(root):
    errors = filename_errors(root)
    for name in sorted(REQUIRED | {'assets/' + x for x in TEMPLATES}):
        if not (root / name).is_file():
            errors.append("missing required file: " + name)
    for path in files(root):
        if path.suffix not in {'.md', '.yaml', '.yml', '.cff'}:
            continue
        rel = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding='utf-8-sig')
            template = rel.startswith('assets/') and path.name in TEMPLATES
            if path.suffix == '.md':
                data, body = frontmatter(text)
                errors.extend(rel + ': ' + error for error in structure_errors(body))
                check_text = prose(body) + '\n' + (text.split('---', 2)[1] if data else '')
                if template and not data:
                    errors.append(rel + ': template needs front matter')
                if rel == 'SKILL.md':
                    if data.get('name') != 'research-literature-analyst' or not isinstance(data.get('description'), str):
                        errors.append(rel + ': invalid skill identity or description')
            else:
                data = load_yaml(text)
                if not isinstance(data, dict):
                    errors.append(rel + ': YAML document must be a mapping')
                    continue
                check_text = text
                if rel == 'agents/openai.yaml':
                    interface = data.get('interface', {})
                    if not isinstance(interface, dict) or not isinstance(interface.get('default_prompt'), str) or '$research-literature-analyst' not in interface['default_prompt']:
                        errors.append(rel + ': default_prompt must invoke the skill')
            if not template and PLACEHOLDER.search(check_text):
                errors.append(rel + ': unresolved template placeholder outside an approved template')
        except (ValueError, TypeError, yaml.YAMLError, UnicodeError) as error:
            errors.append(rel + ': ' + str(error))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    if not args.root.is_dir():
        return finish(['root directory does not exist'], 'skill and templates')
    return finish(validate(args.root.resolve()), 'skill and templates')


if __name__ == '__main__':
    raise SystemExit(main())
