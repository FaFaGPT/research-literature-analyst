---
task_id: obsidian-generation
status: not-run
---

# Obsidian generation

## Input and evidence key

Provide a focused question and a small real source pack with enough evidence for at least one candidate direction. Include a title with Windows-forbidden punctuation and two similar short titles to test naming without corrupting bibliographic metadata.

## Task prompt

```text
Use $research-literature-analyst to produce an Obsidian research library
from the supplied sources. Keep Motivation with motivation papers and
theoretical foundations, then Research content and related work.
Each direction must retain its small motivation and concrete content.
Aim for about five evidence-supported directions without padding.
Connect papers, claims, concepts, directions, and an evidence matrix.
Create safe filenames and valid YAML, and resolve all template variables.
```

## Acceptance and review

- Run `python scripts/validate_vault.py path/to/vault` against the actual vault root.
- Open the vault in Obsidian for a real rendering check when available; record if this check was not performed.
- An expert checks the required research structure, substantive summaries, useful relationships, and any unjustified direction padding.
- Assess bibliography, alignment, coverage, and usefulness separately from structural checks.

The source pack, execution, and Obsidian screenshots still need a real run.
