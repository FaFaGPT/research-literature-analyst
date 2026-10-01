# Results reporting contract

**No research benchmark results have been produced yet.** The examples are synthetic format fixtures. Local validators and their regression tests check engineering behavior only.

For each future run, create a directory named for its date and task ID. Include:

- `manifest.yaml`: task ID, run date, task/prompt version, skill commit, model identifier, model settings actually known, tool/network access, source cutoff, source IDs/versions/checksums, and output location.
- Exact prompt and source manifest. Link restricted inputs instead of redistributing them.
- Original generated notes and the relevant execution/search record.
- Validator commands, exit codes and logs, including failures.
- Expert ratings using the rubric, reviewed item counts and denominators, reviewer information, exclusions, and unresolved disagreements.
- A short outcome explaining what worked, what failed, and what the run cannot establish.

Use null or `not recorded` for unknown run settings. Never reconstruct precise timing, model parameters, or scores from memory. Do not copy this reporting contract as if it were a completed result.

Keep closed-pack and open-web runs distinguishable. Comparisons between skill versions must use the same inputs and evaluation rules, or clearly state the differences. A single demonstration is not evidence of general performance.
