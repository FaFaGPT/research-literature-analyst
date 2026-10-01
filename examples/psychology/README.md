# Psychology example

**Illustrative/synthetic; no real study has been analyzed.** The question below is a proposed task, not a literature finding.

## Research question

Under what population, task and measurement conditions might AI oversight change perceived accountability?

## Real inputs to collect

Select original construct/theory sources and empirical papers with support and counterevidence. Record who was sampled, how oversight was manipulated, how accountability was measured, uncertainty, and whether designs justify causal interpretation. Do not assume different accountability scales measure the same construct.

## Prompt

```text
Use $research-literature-analyst with the source pack I provide to investigate
oversight and perceived accountability. Preserve Motivation and research
directions, identify boundary conditions, and show which evidence supports
or challenges each scoped claim. Do not infer a causal effect from correlation.
```

## Expected navigation

Topic → paper notes → scoped Claim → accountability concept → direction → social-science evidence matrix. The future real vault should contain the two-part topic outline, independent notes, source locations and a search log. No real-paper output or screenshot is currently included.

## Open the synthetic vault

Open the `vault/` directory as an Obsidian vault, starting at [the research map](vault/00-Research-map.md). Seven connected notes demonstrate file layout, metadata and links. Every note is explicitly marked synthetic; the paper record is not a publication and the Claim has insufficient evidence.

Validate its structure from the repository root:

```bash
python scripts/validate_vault.py examples/psychology/vault
```
