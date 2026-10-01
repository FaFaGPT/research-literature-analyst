---
task_id: single-paper-deep-reading
status: not-run
---

# Single-paper deep reading

## Input and evidence key

Choose one real method paper with accessible full text, equations or a reproducible procedure, a comparison table, and an appendix if available. The curator records verified bibliography, exact result cells with conditions, essential method steps, and at least one limitation. Supply the paper to the agent, but retain the expert evidence key for evaluation.

## Task prompt

```text
Use $research-literature-analyst to deeply read the supplied paper.
Explain its motivation, assumptions, method and design choices, equations
or procedure, baselines, numerical results, and evidence limits.
Record actual reading coverage and priority. Separate reports from inference.
Create a linked paper note in the provided output directory.
Use only the supplied materials; mark inaccessible information explicitly.
```

## Acceptance and review

- Trace the central method explanation and every extracted key number to the evidence key.
- Check appendix coverage separately; inaccessible code cannot be reported as inspected.
- Apply bibliography, alignment, numerical, reconstruction, and separation rubric dimensions.
- Run vault validation. A structurally valid but scientifically incorrect answer fails the relevant human criteria.

No source pack or result is bundled here. The evaluator must select and record the sources before execution.
