# Repository setup recommendations

These are recommendations for the repository owner. This document does not change GitHub settings or claim those changes have been made.

Current verified repository: [FaFaGPT/research-literature-analyst](https://github.com/FaFaGPT/research-literature-analyst). GitHub account ID: 72056684. The handle is the only author identity used; no real-world name or DOI is inferred. Topics were empty when checked on 2026-10-01.

## Suggested topics

```text
codex
codex-skills
literature-review
academic-research
paper-reading
obsidian
knowledge-management
research-assistant
```

## Suggested description

```text
科研文献精读、Claim–Evidence 综合与 Obsidian 研究地图 | A Codex skill for deep paper reading and persistent research synthesis.
```

## Social preview

Use the existing [English overview](images/overview.en.png) or [Chinese overview](images/overview.zh-CN.png) as a candidate, check its appearance in GitHub's preview UI, and adjust only if text becomes unreadable. Keep the [logo](images/logo.png) for project identity. No extra promotional graphics are needed, and no social preview setting has been applied by this guide.

## Release strategy

1. Keep development changes under `Unreleased` in the changelog until a release actually happens.
2. Before a first tagged release, run the validators and at least one documented real-paper walkthrough; report scientific limitations separately from structural checks.
3. Choose a version when publishing. Describe schema/workflow compatibility and any migration needed for existing vaults.
4. When publishing is scheduled, update CHANGELOG and citation metadata with the chosen version and actual release date, then tag the reviewed commit containing them. Never add an invented DOI; add one only after a real archival registration.
5. Later releases should link actual evaluation artifacts. A demo alone is not a benchmark, and a passing CI badge is not a citation-accuracy claim.

Repository settings and publishing a release require a separate owner action. Adding files through a commit does not set topics, social preview, branch protection, or a GitHub release.
