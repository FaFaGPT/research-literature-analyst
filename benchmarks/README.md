# Evaluation framework

**Status: task protocols are defined; no real-paper benchmark has been run.** Synthetic examples and validator tests demonstrate file structure only. They do not measure citation accuracy, hallucination, method understanding, or research usefulness.

## Tasks

| Task | Required input | Output under review |
| --- | --- | --- |
| [Single-paper reading](tasks/01-single-paper.md) | One full paper and its available appendix | Method explanation, results, source locations |
| [Multi-paper synthesis](tasks/02-synthesis.md) | Papers supporting and challenging one scoped claim | Evidence matrix, claim and conflict analysis |
| [Gap verification](tasks/03-gap-verification.md) | A proposed gap plus a frozen search/source pack | Attempted falsification and bounded gap status |
| [Incremental update](tasks/04-incremental-update.md) | Existing vault and new contradictory evidence | Revised judgments with preserved identity and annotations |
| [Obsidian generation](tasks/05-obsidian.md) | Research question and checked source pack | Connected, valid notes with the required topic outline |

## Run protocol

1. Select an appropriate task and obtain accessible real sources. Record DOI or stable URL, version, access date, local source checksum, and any missing appendix/code. Do not upload restricted papers without permission.
2. Freeze the question, prompt, source pack, expected evidence locations, skill commit, model identity, tool access, and search cutoff **before** running. An expert prepares the evidence key independently of the generated answer.
3. Separate closed-source-pack evaluation from open-web evaluation. For open-web work, preserve actual queries, dates, accessed pages, exclusions, and retrieval failures. The two settings do not have identical coverage.
4. Run the task in a fresh output directory. Save the exact prompt, tool-access conditions, unedited output, and later corrections separately.
5. Run structural checks, then have a domain expert apply the [human rubric](rubrics/expert-review.md). Ideally a second expert independently rates a subset and records disagreements; never claim multiple reviewers unless they participated.
6. Publish results following [the reporting contract](results/README.md), including failed or incomplete runs, denominators, exclusions, and source access limits. Do not turn unreviewed items into zero scores or silently omit them.

## Automatic checks

Validation needs Python 3.9+ and one small dependency, PyYAML. The skill itself needs neither Python nor an Obsidian plugin.

```bash
python -m pip install -r scripts/requirements.txt
python scripts/validate_templates.py
python scripts/validate_links.py
python -m unittest discover -s scripts/tests -v
python scripts/validate_vault.py path/to/actual-vault-root
```

The first three checks use the repository root automatically. Vault paths are explicit. Validators exit nonzero on errors and do not edit files, follow external URLs, download papers, or call a model.

| Automatic | What it establishes |
| --- | --- |
| YAML parsing and duplicate-key rejection | Syntactic metadata validity |
| Local Markdown/HTML links and Obsidian links | Existing, unambiguous destinations and supported heading/block anchors |
| Template placeholders | Variables are confined to approved templates or quoted instructional examples |
| Windows filenames and case collisions | Portability of filenames |
| Duplicate IDs and reading status | Basic note identity and coverage metadata |
| Required resources and basic Markdown structure | Package completeness, one H1, closed fences |

The link checker supports inline, full/collapsed reference links, HTML `src`/`href`, and vault wikilinks. Instructional code is excluded from repository link checks. It is a focused checker, not a complete Markdown renderer. External source correctness requires review.

## Human review

Experts assess bibliographic accuracy, claim-source alignment, numerical accuracy, method reconstruction, evidence coverage, report/inference separation, gap false-positive tendency, cross-paper synthesis, critical analysis, and research usefulness. Use the [rubric](rubrics/expert-review.md), not structural validation as a proxy for scientific correctness.

The [CI workflow](../.github/workflows/validate.yml) runs offline repository checks and any checked-in illustrative vaults. Passing it is not a research benchmark score.
