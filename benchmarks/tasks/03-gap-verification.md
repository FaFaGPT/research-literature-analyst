---
task_id: research-gap-verification
status: not-run
---

# Research gap verification

## Input and evidence key

Build a small set of proposed gaps, including at least one that real prior work already addresses and one whose answer changes with terminology or scope. Freeze the expert adjudication and the sources establishing it. Keep the adjudication hidden from the agent. State whether retrieval is open-web or limited to a supplied pack.

## Task prompt

```text
Use $research-literature-analyst to test each proposed research gap.
Try to kill the gap. Search direct and synonymous terms, adjacent theories
and disciplines, closest methods, backward and forward citations, and
critiques, replications, or alternative explanations, within the allowed scope.
Record what actually ran and what could not run. Look specifically for
work that already resolves the question. Give a bounded gap status,
the strongest counterexample, and remaining uncertainty.
```

## Acceptance and review

- Already-addressed cases must not be presented as unqualified new gaps.
- Restricted or failed searches must not be presented as completed coverage.
- For an evaluated set, report the numerator and denominator of known-addressed cases incorrectly called supported gaps; do not infer a stable rate from a tiny set.
- Apply gap-validity, coverage, alignment, and usefulness rubrics. Cases lacking expert adjudication remain unassessed.

This file defines a protocol and contains no measured false-positive result.
