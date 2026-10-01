---
task_id: incremental-update
status: not-run
---

# Incremental update

## Input and evidence key

Supply a frozen existing vault with stable paper and claim IDs, user annotations, a known claim, and links from a direction and topic. Add a real contradictory or scope-narrowing paper. Save a before snapshot and hashes of notes unrelated to the update.

## Task prompt

```text
Use $research-literature-analyst to update the supplied research map
using this new paper. Reassess the affected claim and evidence matrix,
explain the conflict, and revise the direction and topic only where needed.
Preserve IDs, creation dates, and user annotations. Record old and new
interpretations with their sources and keep remaining uncertainty explicit.
```

## Acceptance and review

- Verify source alignment of the revised claim and any changed evidence sufficiency.
- Inspect the diff for lost annotations, duplicated paper/claim nodes, stale summaries, and unnecessary rewrites.
- Check that changes to scientific meaning are explained and linked; identity changes cannot be silent.
- Apply alignment, synthesis, separation, and usefulness rubrics; validate the resulting vault.

No before/after research run has been executed for this protocol yet.
