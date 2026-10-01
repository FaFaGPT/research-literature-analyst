# Contributing / 贡献指南

Keep this a focused Codex research skill. Preserve Motivation, theoretical foundations, and evidence-supported research directions; each direction keeps its own motivation papers and concrete content.

## Make a focused change

1. Read the relevant part of [SKILL.md](SKILL.md), [references](references/), and [templates](assets/) before editing. Reuse existing concepts instead of adding parallel fields for the same function.
2. Put shared decisions in SKILL.md and detailed or conditional guidance in a focused reference. Maintain existing installation methods, default Chinese output and explicit English output.
3. Keep [English](README.md) and [Chinese](README.zh-CN.md) introductions synchronized. Keep the homepage concise; place detailed procedures in docs.
4. If changing note properties, explain migration and preserve stable IDs, creation dates and user annotations. Update templates, relevant examples and validator rules together.
5. Add a regression test when a validator changes behavior. Use temporary fixtures; do not mistake those tests for scientific evaluation.

## Run checks from the repository root

```bash
python -m pip install -r scripts/requirements.txt
python scripts/validate_templates.py
python scripts/validate_links.py
python -m unittest discover -s scripts/tests -v
python scripts/validate_vault.py examples/psychology/vault
python scripts/validate_vault.py examples/machine-learning/vault
python scripts/validate_vault.py examples/interdisciplinary/vault
git diff --check
```

The validators use Python 3.9+ and PyYAML. They do not assess whether a paper exists or whether a scientific claim is true. Review source alignment and research usefulness using the [expert rubric](benchmarks/rubrics/expert-review.md).

## Examples and evidence

- Keep illustrative/synthetic notes explicitly labeled at both directory and note level.
- A real example needs accessible sources, actual output, execution conditions and a source-based review. Preserve failed and partial results.
- Do not invent papers, DOIs, experimental numbers, benchmark scores, screenshots, user counts or testimonials.
- Use [the demo guide](docs/demo/README.md) for real recordings and [the result contract](benchmarks/results/README.md) for evaluations.
- Do not redistribute restricted PDFs or private notes. Link to lawful sources instead.

## Propose the change

Explain the problem, resulting behavior, changed workflow or schema, and checks actually run. State remaining limitations. Add substantive changes to [CHANGELOG.md](CHANGELOG.md). Avoid claiming a GitHub CI run passed when only local commands were executed.

GitHub settings, topics, social preview and releases are separate maintainer actions; see [repository setup recommendations](docs/repository-setup.md).

中文要点：保留研究主结构；同步模板、示例与中英文说明；结构检查与科研评测分开；合成示例必须标明；引用与实验结论必须能回到真实来源。
