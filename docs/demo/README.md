# Record a real demo

**Status: no real execution recording is included.** Existing overview images are illustrations. The example vaults are synthetic format fixtures and must not be presented as real literature-analysis output.

## Choose an inspectable task

Use a narrow question and a few accessible real papers, including a relevant challenge or limitation. Record source URLs/DOIs, versions, retrieval date, permission to show excerpts, the skill commit and the model/tool conditions actually known.

Example prompt to adapt before recording:

```text
Use $research-literature-analyst with these real sources and this question.
Preserve Motivation and research directions. Deeply read the core method,
create scoped Claims and an evidence matrix, test one candidate gap,
and save the notes into a new Obsidian directory.
Record unavailable information and do not invent missing findings.
```

Replace descriptive inputs with actual materials when executing. Save the exact executed prompt, not just this example.

## Capture the real sequence

1. **Prompt:** show the actual question, source pack and output location.
2. **Codex running:** record genuine retrieval, reading and file creation. Keep enough context to show access failures and corrections; explain any speed-up or edits.
3. **Generated files:** show the directory and run the validators. Save the original output before manual edits.
4. **Source spot-check:** compare a claim and a numerical result, if present, with the actual source location.
5. **Obsidian:** open the real generated directory and navigate topic → paper → Claim → matrix → direction. Show the preserved Motivation structure.
6. **Incremental update:** provide new evidence or a specific critique and show the actual changed notes and judgment, if included in the recording.

Do not replace failures with synthetic UI frames. Protect private account details and unpublished materials when recording.

## Deliverable checklist

| Media | Location to use after recording | Evidence it should show |
| --- | --- | --- |
| Execution GIF/video | `docs/demo/codex-execution.gif` or a documented real video location | Actual prompt, run and created files |
| Vault screenshot | `docs/screenshots/obsidian-vault.png` | Real output opened in Obsidian |
| Paper note screenshot | `docs/screenshots/paper-note.png` | Source location and method/result explanation |
| Research map screenshot | `docs/screenshots/research-map.png` | Topic outline, Claims and direction relationships |

These filenames are a capture plan, not existing assets. Embed them in the main READMEs only after the files exist and have been checked. See [screenshot requirements](../screenshots/README.md).

Store a run note with date, commit, sources, exact prompt, actual output location, edits, validator results and unverified claims. Use the [benchmark reporting contract](../../benchmarks/results/README.md) if making evaluation claims; a recording alone does not establish performance.
