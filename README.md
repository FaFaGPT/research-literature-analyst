# Research Literature Analyst

[English](README.md) | [简体中文](README.zh-CN.md)

A Codex skill for reading research papers in depth and building a growing Obsidian literature library around a research question.

It connects motivation, theory, methods, experimental evidence, and possible research directions. Each paper has its own note, while a topic map explains how the papers fit together.

## What it does

- **Build a research map:** organize the topic into motivation, theoretical foundations, and, where evidence supports them, five possible research directions.
- **Read papers in depth:** summarize every included paper and examine the core papers at the level needed for doctoral research.
- **Explain methods and experiments:** cover assumptions, equations, design choices, algorithms, baselines, numerical results, ablations, and failure cases.
- **Keep evidence traceable:** record source locations and separate reported findings, analytical inferences, and proposed research.
- **Continue from feedback:** turn requests such as “section 2.2 needs stronger theory” into targeted searches and updates to existing notes.
- **Write Obsidian notes:** generate Markdown files with YAML properties, internal links, tags, paper cards, and a further-reading queue.

## The research structure

The skill preserves this outline. Critical analysis and research opportunities support it rather than replacing it.

```text
Research topic
1. Motivation
   1.1 Motivation papers
       Paper A: question, importance, gap, contribution, relevance
       Paper B: ...
   1.2 Theoretical foundations
       Origins, constructs, assumptions, mechanisms, boundaries
2. Research content and related work
   2.1 Possible research direction 1
       ① Papers motivating this specific direction
       ② Concrete research content
   2.2 Possible research direction 2
       ① Papers motivating this specific direction
       ② Concrete research content
   ... Aim for five distinct directions when justified by evidence
```

Theory papers emphasize concepts, mechanisms, theoretical development, and boundaries. Method papers require concrete mathematical or procedural explanations and an examination of the supporting experiments. The workflow also adapts to research outside machine learning.

## Install in Codex

### Option A: Ask the skill installer

Paste this into Codex:

```text
$skill-installer Install the skill from
https://github.com/Wangmou1234/research-literature-analyst
Use the repository root (path .) and name it research-literature-analyst.
```

### Option B: Clone into your local skills directory

Choose one installation method. For manual installation, the current official Codex documentation lists `~/.agents/skills` as a user-level discovery location. The bundled installer may use the skills directory configured for your environment; do not install duplicate copies just to cover both locations. See [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills).

**Windows / PowerShell**

```powershell
$skillRoot = Join-Path $HOME '.agents\skills'
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
git clone https://github.com/Wangmou1234/research-literature-analyst.git (Join-Path $skillRoot 'research-literature-analyst')
```

**macOS / Linux**

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/Wangmou1234/research-literature-analyst.git "$HOME/.agents/skills/research-literature-analyst"
```

After installation, invoke `$research-literature-analyst`. If it does not appear, restart Codex. This repository contains instructions and templates; it has no package dependencies to install.

## Usage

The instructions and templates are written in Chinese, and Chinese is the default output language. Request English explicitly when needed. The examples below specify it.

### 1. Start a topic review

```text
Use $research-literature-analyst to investigate [research topic].
My core research question is [question].
Seed papers: [paper URLs, DOIs, or local file paths].
Write all explanatory prose and note headings in English.
Save the notes to [output directory or Obsidian vault path].
Preserve the motivation and research-content structure. Aim for five
distinct research directions, and deeply explain the core methods and experiments.
```

You can start with just a topic or a paper. A specific question, seed papers, scope, and output path help focus the work. Without a vault path, the skill creates `research-notes/<topic>/` in the current working directory.

### 2. Read one paper deeply

```text
Use $research-literature-analyst to read [paper URL or local PDF path].
Write the note in English. Explain the key equations, symbols, design choices,
training or solution procedure, and how the experimental evidence supports
the claims. Include baselines, numerical results, ablations, and limitations.
Connect it to the existing topic at [notes directory].
```

### 3. Continue where the review is weak

```text
Use $research-literature-analyst to update the review at [notes directory].
Section 2.2 needs stronger theoretical support and a clearer comparison
with the closest methods. Search for additional evidence, update the
existing notes, and explain which conclusions changed and what is still missing.
Keep the output in English.
```

For a review limited to your own materials, add: “Use only the files I provided; do not search online.”

## Output in Obsidian

```text
research-notes/<topic>/
├── 00-研究地图.md                 # Topic map
├── 01-Papers/                    # Independent paper notes
├── 02-Directions/                # Research directions
├── 03-Concepts/                  # Reusable theories, methods, datasets
└── 90-补读与检索记录.md           # Further reading and search history
```

Open the generated directory as an Obsidian vault, or ask the skill to write into your existing vault. Existing naming conventions take priority; English names can be requested. No community plugin is required.

The `assets/` files are templates for the agent to fill, not finished literature notes or scripts. Their `{{...}}` placeholders should be replaced in generated notes.

## Evidence and reading depth

Every paper records its actual reading coverage: `metadata-only`, `abstract-only`, `partial-full-text`, or `full-text`. Appendix and code coverage are recorded separately.

Key findings and numbers should point back to a section, equation, figure, or table in the source. Missing details stay marked as unreported, not found, inaccessible, or not applicable. Proposed experiments remain clearly labeled as proposals.

Online retrieval and PDF inspection depend on the tools available in the host environment and access to the source material. An abstract-only note cannot establish the same detail as a full-paper reading. Generated research judgments still need researcher review.

## Repository contents

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Main workflow and research structure |
| [agents/openai.yaml](agents/openai.yaml) | Codex display information and default prompt |
| [references/reading-depth.md](references/reading-depth.md) | Theory, method, experiment, and reviewer analysis |
| [references/search-and-update.md](references/search-and-update.md) | Search, citation tracking, and incremental updates |
| [references/obsidian-format.md](references/obsidian-format.md) | Note layout, metadata, naming, and linking |
| [assets/topic-map.md](assets/topic-map.md) | Topic-map template |
| [assets/paper-note.md](assets/paper-note.md) | Paper-note template |
| [assets/direction-note.md](assets/direction-note.md) | Research-direction template |
| [assets/concept-note.md](assets/concept-note.md) | Theory, method, or dataset template |
| [assets/reading-queue.md](assets/reading-queue.md) | Further-reading and search-log template |

## Update a Git-based installation

Run `git pull --ff-only` inside the installed skill directory. If you have edited the skill locally, review and preserve those changes before updating.

## Design references and validation

The search log borrows reporting practices from the [PRISMA 2020 checklist](https://www.prisma-statement.org/prisma-2020-checklist) and [PRISMA-S](https://www.prisma-statement.org/prisma-search). This does not make every review produced by the skill a complete systematic review. Note formatting follows [Obsidian internal links](https://help.obsidian.md/links) and [properties](https://help.obsidian.md/properties).

The initial package has passed skill-format, template-YAML, and local-resource-link checks. It has not yet been evaluated on a complete real-paper review.
