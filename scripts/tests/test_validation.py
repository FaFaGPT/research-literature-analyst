"""Regression fixtures for checks; these are not literature benchmark results."""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _validation import frontmatter, invalid_windows_name, link_errors, structure_errors
from validate_vault import validate


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def note(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')

    def test_duplicate_yaml_rejected(self):
        with self.assertRaises(ValueError):
            frontmatter('---\ntype: paper\ntype: topic\n---\n# A\n')

    def test_local_links_code_and_case(self):
        self.note('README.md', '# Test\n[ok](<with space.md>)\n`[sample](missing.md)`\n[bad](WITH%20SPACE.md)\n')
        self.note('with space.md', '# Destination\n')
        errors = link_errors(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn('WITH%20SPACE.md', errors[0])

    def test_wikilinks_properties_anchors_and_ambiguity(self):
        self.note('index.md', '---\ntype: topic\nlinks: ["[[a/Paper#Result]]"]\n---\n# Map\n[[Paper]]\n[[a/Paper#Missing]]\n')
        self.note('a/Paper.md', '# A\n## Result\n')
        self.note('b/Paper.md', '# B\n')
        errors = link_errors(self.root, wiki=True)
        self.assertEqual(len(errors), 2)
        self.assertTrue(any('ambiguous' in e for e in errors))
        self.assertTrue(any('heading' in e for e in errors))

    def test_vault_rejects_missing_status_placeholder_and_duplicate_doi(self):
        self.note('one.md', '---\ntype: paper\nid: "doi:10.1000/EXAMPLE"\n---\n# One\n{{unfinished}}\n')
        self.note('two.md', '---\ntype: paper\nid: "https://doi.org/10.1000/example"\nreading_status: abstract-only\n---\n# Two\n')
        errors = validate(self.root)
        self.assertTrue(any('reading_status' in e for e in errors))
        self.assertTrue(any('placeholder' in e for e in errors))
        self.assertTrue(any('duplicate ID' in e for e in errors))

    def test_valid_minimal_vault(self):
        self.note('Map.md', '---\ntype: topic\n---\n# Map\n[[P#Finding]]\n')
        self.note('P.md', '---\ntype: paper\nid: synthetic:test\nreading_status: metadata-only\n---\n# Paper\n## Finding\nNo scientific finding; test fixture.\n[[Map]]\n')
        self.assertEqual(validate(self.root), [])

    def test_windows_filename(self):
        for name in ['CON.md', 'LPT1.txt', 'a:b.md', 'trailing.', 'trailing ']:
            self.assertTrue(invalid_windows_name(name), name)
        self.assertFalse(invalid_windows_name('研究地图.md'))

    def test_structure_and_reference_links(self):
        self.assertTrue(structure_errors('# A\n```python\nprint(1)\n'))
        self.note('README.md', '# A\n[missing][reference]\n<img src="missing.png">\n')
        self.assertEqual(len(link_errors(self.root)), 2)

    def test_wikilinks_dotted_note_and_real_attachment(self):
        self.note('Map.md', '# Map\n[[Method.v2]]\n![[figure.png]]\n')
        self.note('Method.v2.md', '# Method\n')
        (self.root / 'figure.png').write_bytes(b'fixture')
        self.assertEqual(link_errors(self.root, wiki=True), [])

    def test_missing_block_anchor(self):
        self.note('Map.md', '# Map\n[[Paper#^found]]\n[[Paper#^missing]]\n')
        self.note('Paper.md', '# Paper\nEvidence paragraph. ^found\n')
        errors = link_errors(self.root, wiki=True)
        self.assertEqual(len(errors), 1)
        self.assertIn('missing', errors[0])

    def test_long_wikilink_in_properties(self):
        import yaml
        title = 'A long research title with spaces ' * 3
        title = title.strip()
        self.note(title + '.md', '# Paper\n')
        properties = yaml.safe_dump({'links': ['[[' + title + ']]', '[[Missing long title]]']})
        self.note('Map.md', '---\n' + properties + '---\n# Map\n')
        errors = link_errors(self.root, wiki=True)
        self.assertEqual(len(errors), 1)
        self.assertIn('Missing long title', errors[0])

    def test_repository_placeholders_in_prose_not_instructional_code(self):
        from validate_templates import validate as validate_package
        self.note('Bad.md', '# Bad\nUnfilled {{title}}\n')
        self.note('Good.md', '# Good\nUse `{{title}}` in a template.\n')
        errors = validate_package(self.root)
        self.assertTrue(any('Bad.md: unresolved' in e for e in errors))
        self.assertFalse(any('Good.md:' in e for e in errors))

    def test_invalid_agent_metadata_reports_error(self):
        from validate_templates import validate as validate_package
        for content in ['- invalid list root\n', 'interface: invalid scalar\n']:
            with self.subTest(content=content):
                self.note('agents/openai.yaml', content)
                errors = validate_package(self.root)
                self.assertTrue(any('agents/openai.yaml:' in e for e in errors))

    def test_claim_schema_and_duplicate_ids(self):
        import yaml
        claim = {'type': 'claim', 'claim_id': 'C001', 'claim_statement': 'Untested fixture',
                 'claim_type': 'research-hypothesis', 'current_status': 'draft',
                 'population_context_task': 'Unspecified', 'boundary_conditions': 'Unknown',
                 'unresolved_conflict': 'Not assessed', 'evidence_sufficiency': 'insufficient evidence'}
        for field in ['supporting_papers', 'challenging_papers', 'evidence_types',
                      'evidence_locations', 'linked_concepts', 'linked_directions']:
            claim[field] = []
        self.note('C1.md', '---\n' + yaml.safe_dump(claim) + '---\n# C1\n')
        self.assertEqual(validate(self.root), [])
        claim['evidence_sufficiency'] = 0.98
        self.note('C2.md', '---\n' + yaml.safe_dump(claim) + '---\n# C2\n')
        errors = validate(self.root)
        self.assertTrue(any('qualitative' in e for e in errors))
        self.assertTrue(any('duplicate ID' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
