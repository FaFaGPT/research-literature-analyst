<p align="center">
  <img src="docs/images/logo.png" alt="Research Literature Analyst logo" width="128">
</p>

# Research Literature Analyst

[English](README.md) | [简体中文](README.zh-CN.md)

A Codex skill for doctoral-depth paper reading, evidence-grounded research synthesis, and a persistent Obsidian literature library.

![Paper analysis, theory, methods, critical reading and research mapping](docs/images/overview.en.png)

## Beyond one-shot paper summarization

A paper summary explains one source. This workflow maintains a research question across sources and sessions: track reading coverage, localize evidence, separate reports from inference, compare papers, verify gaps, and revise the research map as evidence changes.

The main structure stays **1. Motivation → 1.1 Motivation papers → 1.2 Theoretical foundations**, then **2. Research content and related work**, with about five distinct directions when justified. Each direction retains **① its own motivation papers** and **② concrete research content**.

## Examples and output

Explore [psychology](examples/psychology/README.md), [machine learning](examples/machine-learning/README.md), and [interdisciplinary research](examples/interdisciplinary/README.md). These are illustrative/synthetic guides, not completed real-paper reviews. No real execution GIF or Obsidian screenshot is currently available.

Each example includes a small linked synthetic vault. For genuine execution and Obsidian captures, follow the [demo recording guide](docs/demo/README.md); no nonexistent screenshots are embedded.

## Core capabilities

- Read theory through constructs, assumptions, mechanisms and boundaries.
- Reconstruct methods, equations, design choices and experiments.
- Compare supporting and challenging evidence under explicit conditions.
- Maintain scoped Claim nodes, discipline-specific evidence matrices and conflict analyses.
- Try to falsify candidate gaps before treating them as research opportunities.
- Turn feedback into targeted retrieval and updates to existing notes.
- Develop research hypotheses with minimal studies and failure criteria.

## Installation

In Codex:

```text
$skill-installer Install https://github.com/FaFaGPT/research-literature-analyst
Use path . and name research-literature-analyst.
```

For manual installation into `~/.agents/skills/research-literature-analyst`, see the [Windows, macOS and Linux instructions](docs/usage.md). Choose one installation method. No dependency installation is needed to use the skill.

## Usage

```text
Use $research-literature-analyst to investigate [research question].
Sources: [URLs, DOIs, or local papers]. Write in English.
Save to [output directory / Obsidian vault]. Keep Motivation and research
directions; explain the core methods, experiments, and evidence limits.
```

To continue: “Section 2.2 needs stronger theory. Find counterevidence, revise the existing notes, and explain what changed.” More [topic, paper and update prompts](docs/usage.md) are available.

Instructions and templates are Chinese; output defaults to Chinese and follows an explicit request for English. Retrieval and PDF inspection depend on the host's tools and source access.

## Obsidian structure

```text
research-notes/<topic>/
├── 00-研究地图.md
├── 01-Papers/
├── 02-Directions/
├── 03-Concepts/
├── 04-Claims/
├── 05-Evidence/
└── 90-补读与检索记录.md
```

Open the directory as a vault or write into an existing one. Use Markdown, YAML and internal links without a Dataview, Templater or Zotero dependency. See [file and linking rules](references/obsidian-format.md).

## Evidence model

Record actual coverage as `metadata-only`, `abstract-only`, `partial-full-text`, or `full-text`; record appendix/code coverage separately. Key judgments and numbers need source locations. Separate paper reports, inference and research hypotheses. Missing information stays explicit.

`reading_priority` (Tier A–D) guides reading effort independently of coverage. A core paper can remain abstract-only when its full text is inaccessible. Claims distinguish `paper-reported`, `cross-paper-synthesis`, `analyst-inference`, and `research-hypothesis`; evidence sufficiency is qualitative: strong, moderate, limited, conflicting, or insufficient evidence. See [Claim, matrix and conflict rules](references/evidence-synthesis.md).

## Evaluation

[Five benchmark protocols](benchmarks/README.md) cover deep reading, synthesis, gap verification, updates and Obsidian generation. Automated checks assess structure; experts assess evidence alignment, numbers, methods and research usefulness.

**No real-paper benchmark results are available.** Synthetic examples and validator tests do not establish research accuracy.

```bash
python -m pip install -r scripts/requirements.txt
python scripts/validate_templates.py
python scripts/validate_links.py
python -m unittest discover -s scripts/tests -v
python scripts/validate_vault.py path/to/vault
```

Python and PyYAML are needed only for validation. See [evaluation boundaries](benchmarks/README.md).

## Repository structure

| Location | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md), [agents/](agents/) | Workflow and Codex metadata |
| [assets/](assets/), [references/](references/) | Templates and detailed reading rules |
| [examples/](examples/) | Domain guides and labeled illustrative material |
| [benchmarks/](benchmarks/) | Tasks, rubric and result reporting |
| [scripts/](scripts/) | Offline validators and regression tests |
| [docs/](docs/) | Usage and presentation resources |

MIT licensed; see [LICENSE](LICENSE). Search reporting draws on [PRISMA-S](https://www.prisma-statement.org/prisma-search); using the skill does not itself constitute a complete systematic review. Git-based installations can update with `git pull --ff-only` after preserving local edits.

[Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md) · [Citation metadata](CITATION.cff) · [Repository setup recommendations](docs/repository-setup.md)
