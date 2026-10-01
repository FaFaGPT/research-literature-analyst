"""Check generated notes structurally. This does not assess scientific accuracy."""

import argparse
import re
from pathlib import Path
import yaml
from _validation import (PLACEHOLDER, READING_STATUSES, files, filename_errors,
                         finish, frontmatter, link_errors, structure_errors)

CLAIM_TYPES = {'paper-reported', 'cross-paper-synthesis', 'analyst-inference', 'research-hypothesis'}
CLAIM_STATUSES = {'draft', 'active', 'superseded', 'retired'}
SUFFICIENCY = {'strong evidence', 'moderate evidence', 'limited evidence', 'conflicting evidence', 'insufficient evidence'}
GAP_STATUSES = {'supported gap', 'partially addressed', 'underexplored', 'terminology-dependent', 'already addressed', 'insufficient evidence'}
CLAIM_LISTS = {'supporting_papers', 'challenging_papers', 'evidence_types', 'evidence_locations', 'linked_concepts', 'linked_directions'}


def canonical_id(value):
    value = str(value).strip().casefold()
    return re.sub(r'^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)', '', value)


def validate(root):
    errors, ids = filename_errors(root), {}
    notes = [p for p in files(root) if p.suffix == '.md']
    if not notes:
        return errors + ['vault contains no Markdown notes']
    for path in notes:
        rel = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding='utf-8-sig')
            data, body = frontmatter(text)
            if not data.get('type'):
                errors.append(rel + ': missing note type/front matter')
            if PLACEHOLDER.search(text):
                errors.append(rel + ': unresolved template placeholder')
            errors.extend(rel + ': ' + error for error in structure_errors(body))
            kind = data.get('type')
            if kind == 'paper':
                if not data.get('id'):
                    errors.append(rel + ': missing paper id')
                if data.get('reading_status') not in READING_STATUSES:
                    errors.append(rel + ': missing or invalid reading_status')
                if 'reading_priority' in data and data['reading_priority'] not in {'Tier A', 'Tier B', 'Tier C', 'Tier D'}:
                    errors.append(rel + ': invalid reading_priority')
            if kind == 'claim':
                for field in {'claim_id', 'claim_statement', 'population_context_task', 'boundary_conditions', 'unresolved_conflict'}:
                    if not isinstance(data.get(field), str) or not data[field].strip():
                        errors.append(rel + ': missing or invalid ' + field)
                for field in CLAIM_LISTS:
                    if not isinstance(data.get(field), list):
                        errors.append(rel + ': missing or invalid list ' + field)
                if data.get('claim_type') not in CLAIM_TYPES:
                    errors.append(rel + ': invalid claim_type')
                if data.get('current_status') not in CLAIM_STATUSES:
                    errors.append(rel + ': invalid current_status')
                if data.get('evidence_sufficiency') not in SUFFICIENCY:
                    errors.append(rel + ': invalid qualitative evidence_sufficiency')
            if 'gap_status' in data and data['gap_status'] not in GAP_STATUSES:
                errors.append(rel + ': invalid gap_status')
            identifier = data.get('claim_id') if kind == 'claim' else data.get('id')
            if identifier:
                identity = (str(kind), canonical_id(identifier))
                if identity in ids:
                    errors.append(rel + ': duplicate ID with ' + ids[identity])
                ids[identity] = rel
        except (ValueError, TypeError, yaml.YAMLError, UnicodeError) as error:
            errors.append(rel + ': ' + str(error))
    return errors + link_errors(root, wiki=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path, help='Actual Obsidian vault root, not a nested topic folder')
    args = parser.parse_args()
    if not args.root.is_dir():
        return finish(['vault directory does not exist'], 'vault structure')
    return finish(validate(args.root.resolve()), 'vault structure (not research quality)')


if __name__ == '__main__':
    raise SystemExit(main())
