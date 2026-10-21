---
name: raptora-verify-code
description: Use when verifying a Raptora change, evaluating CI results, or preparing a claim that code or configuration works.
---
# Verify a change

Read AGENTS.md and inspect the current branch, diff, manifests and existing test commands. Identify affected contracts before selecting checks.

| Observable state | Verification |
| --- | --- |
| Governance/configuration only; no application manifests | Run `python3 scripts/verify-development-environment.py`; claim only governance/configuration validation |
| Cleared application source with documented commands | Run impacted existing checks, meaningful regressions and required CI gates; retain underlying exit status |
| Windows or connected behavior | Require separately authorized platform evidence; Linux/synthetic success is insufficient |

Record source HEAD and whether the tree is dirty. Match any CI result to its tested SHA; label earlier results as stale rather than applying them to new changes. For each check return **command/target, result (Pass/Fail/Skipped/Blocked/Not run), counts, evidence and limit**. Confirm tests actually executed; a zero-test run is not functional validation. Diagnose failures and report them without weakening assertions or concealing pre-existing defects. Keep sensitive evidence outside this public repository.

Example: bootstrap CI passing in a source-free tree supports “governance checks passed”; application, Windows and connected checks remain Not run.

Use docs/SOURCE_ACTIVATION_PLAN.md before enabling new application jobs. Do not invent scripts or placeholder successes. See docs/AGENT_RECOVERY.md for interrupted checks.
