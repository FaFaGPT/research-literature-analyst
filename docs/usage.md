# Installation and usage / 安装与使用

[English overview](../README.md) | [中文介绍](../README.zh-CN.md)

## Install in Codex

### Option A: Ask the skill installer

Paste this into Codex:

```text
$skill-installer Install the skill from
https://github.com/FaFaGPT/research-literature-analyst
Use the repository root (path .) and name it research-literature-analyst.
```

### Option B: Clone into your local skills directory

Choose one installation method. For manual installation, the current official Codex documentation lists `~/.agents/skills` as a user-level discovery location. The bundled installer may use the skills directory configured for your environment; do not install duplicate copies just to cover both locations. See [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills).

**Windows / PowerShell**

```powershell
$skillRoot = Join-Path $HOME '.agents\skills'
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
git clone https://github.com/FaFaGPT/research-literature-analyst.git (Join-Path $skillRoot 'research-literature-analyst')
```

**macOS / Linux**

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/FaFaGPT/research-literature-analyst.git "$HOME/.agents/skills/research-literature-analyst"
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


## 在 Codex 中安装

### 方法一：让 skill-installer 安装

在 Codex 中发送：

```text
$skill-installer 请从以下仓库安装 skill：
https://github.com/FaFaGPT/research-literature-analyst
使用仓库根目录（path .），安装名称为 research-literature-analyst。
```

### 方法二：克隆到本地 skills 目录

两种安装方式选一种即可。手动安装时，当前 Codex 官方文档列出的用户级目录为 `~/.agents/skills`；内置安装器可能采用当前环境配置的 skills 目录，不需要为覆盖不同路径而重复安装。参见 [OpenAI 官方 skill 文档](https://learn.chatgpt.com/docs/build-skills)。

**Windows / PowerShell**

```powershell
$skillRoot = Join-Path $HOME '.agents\skills'
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
git clone https://github.com/FaFaGPT/research-literature-analyst.git (Join-Path $skillRoot 'research-literature-analyst')
```

**macOS / Linux**

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/FaFaGPT/research-literature-analyst.git "$HOME/.agents/skills/research-literature-analyst"
```

安装后可用 `$research-literature-analyst` 调用；未出现时重启 Codex。本仓库由说明和模板组成，无需安装额外依赖包。

## 使用方法

skill 指令和模板使用中文，默认也输出中文。需要英文笔记时，在请求中明确写“所有解释和笔记标题使用英文”。

### 1. 围绕一个题目开始调研

```text
请使用 $research-literature-analyst 调研【研究主题】。
我的核心科学问题是【问题】。
种子论文是【论文链接、DOI 或本地文件路径】。
输出到【笔记目录或 Obsidian vault 路径】。
保留 Motivation 和研究内容两大部分，尽量形成五个有区别的研究方向，
深入解释核心方法及其实验结果。
```

可以只提供题目或论文开始。具体问题、种子论文、研究范围和输出路径有助于聚焦；未指定 vault 时，默认在当前工作目录创建 `research-notes/<主题短名>/`。

### 2. 精读一篇论文

```text
请使用 $research-literature-analyst 精读【论文链接或本地 PDF 路径】。
解释关键公式、符号、设计理由、训练或求解过程，
以及实验证据如何支撑论文结论。
需要包含 baseline、具体数值、消融与局限。
把笔记关联到【现有研究笔记目录】中的主题。
```

### 3. 哪里不够，就继续补查

```text
请使用 $research-literature-analyst 更新【研究笔记目录】。
第 2.2 部分理论依据不够，与最接近方法的比较也不清楚。
请继续检索、查阅并更新原笔记，说明哪些结论发生变化，
还有哪些证据缺口没有解决。
```

只希望分析自己的材料时，加一句：“仅使用我提供的文件，不联网检索。”
