# Machine-learning example

**Illustrative/synthetic; no real model or benchmark has been evaluated.** This is a suggested task and input-selection guide.

## Research question

Does a proposed retrieval change improve task performance when training data, evaluation split and compute budget are held comparable?

## Real inputs to collect

Choose a core method, its closest baseline, and a replication or challenging result. Record dataset/version, split, training data, metric, uncertainty, inference budget and implementation. A score difference under different compute budgets is not automatically a method improvement.

## Prompt

```text
Use $research-literature-analyst on the supplied method papers.
Reconstruct their key equations and procedures, compare only compatible
conditions, and connect the evidence matrix to scoped claims.
Explain any split, compute, implementation or baseline-fairness mismatch.
```

## Expected navigation

Topic → methods papers → performance Claim → retrieval concept → candidate direction → ML evidence matrix. The future real vault must distinguish paper-reported results, calculated comparisons and unrun experiments. No real-paper output or screenshot is currently included.

## Open the synthetic vault

Open the `vault/` directory as an Obsidian vault, starting at [the research map](vault/00-Research-map.md). Seven connected notes demonstrate file layout, metadata and links. Every note is explicitly marked synthetic; the paper record is not a publication and the Claim has insufficient evidence.

Validate its structure from the repository root:

```bash
python scripts/validate_vault.py examples/machine-learning/vault
```
