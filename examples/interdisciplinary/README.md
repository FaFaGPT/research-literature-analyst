# Interdisciplinary example

**Illustrative/synthetic; no real publication or user study has been analyzed.** The mechanism below remains a research question.

## Research question

When might model explanations improve calibrated human reliance rather than simply increase agreement with the model?

## Real inputs to collect

Collect theory about reliance/calibration, human-subject evidence, and method evaluations. Keep algorithmic accuracy, explanation fidelity, user understanding and appropriate reliance distinct. Record task expertise, stakes, interface, model error distribution and timing.

## Prompt

```text
Use $research-literature-analyst to synthesize the provided sources on
explanations and calibrated reliance. Bridge concepts explicitly across
disciplines, retain conflicting evidence, and propose a minimal study
whose failure criteria can refute the candidate mechanism.
```

## Expected navigation

Topic → theory and empirical/method papers → qualified Claim → reliance concept → direction → linked domain-specific evidence matrices. Use separate tables when measurements are incompatible. No real-paper output or screenshot is currently included.

## Open the synthetic vault

Open the `vault/` directory as an Obsidian vault, starting at [the research map](vault/00-Research-map.md). Seven connected notes demonstrate file layout, metadata and links. Every note is explicitly marked synthetic; the paper record is not a publication and the Claim has insufficient evidence.

Validate its structure from the repository root:

```bash
python scripts/validate_vault.py examples/interdisciplinary/vault
```
