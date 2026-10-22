# Raptora — Codex context and startup brief

**Context snapshot:** 22 October 2026  
**Audience:** Codex primary agent, specialist reviewers, engineering maintainers  
**Classification:** Public-safe engineering governance; no customer or private-source evidence  
**Purpose:** Provide a durable session entrypoint, current limitations, issue intake rules and release blockers. The authoritative details remain in linked repository documents and live GitHub records.

> **Read `AGENTS.md` first.** This document supplements—not supersedes—`AGENTS.md`, `SECURITY.md`, branch policies, actual source, and maintainer decisions. Nothing here grants permission for source publication, privileged execution, deployment, or an installer run.

## 1. Current repository reality

- This **public** repository contains governance, reference instructions, Codex agent/skill configuration and checking scripts. **The verified Raptora application source has not been migrated here.**
- Repository bootstrap/governance checks are not application builds, Windows service tests, installer tests, connected-device acceptance or production certification.
- Installed Windows development builds and their test observations exist outside this repository. Their lineage and outcome must be verified independently before a claim of readiness.
- The legacy application repository is a **read-only migration reference**, not automatically the newest or approved source. Reconcile exact branches, commits, releases, open PRs, packaging and provenance under the separately approved confidential audit procedure.
- Publishing any private source requires explicit ownership/licence permission and review of files **and full history** for secrets, client information, operational topology, restricted dependencies and incompatible licences. Do not invent replacement application code to circumvent that gate.
- Live GitHub issues, PRs, tested commit SHAs and evidence outrank a dated summary such as this file. If records conflict, document the discrepancy and ask the maintainer for the decision.

See [project status](docs/PROJECT_STATUS.md), [roadmap](docs/ROADMAP.md), [source activation plan](docs/SOURCE_ACTIVATION_PLAN.md) and [private migration audit procedure](docs/PRIVATE_MIGRATION_AUDIT.md).

## 2. Product and engineering invariants

Raptora is intended as a proprietary, **local-first** security-system monitoring, diagnostics, evidence and reporting application, operable without a ChatGPT/Codex session or hosted AI dependency.

Protect these boundaries:

- Read-only collection and diagnostics **by default**; request explicit, scoped human authorisation before intrusive device, network, operating-system or security-system changes.
- Separate the desktop interface, continuously operating Windows service and controlled worker/adaptor execution. Intended technologies include a React/TypeScript desktop interface, Windows service, PowerShell collectors and Milestone XProtect integration; **verify actual implementation from cleared source**, not from this summary.
- Persist configuration, history and evidence with explicit backup, integrity, compatibility and retention rules. Never delete or reset persisted application data as a routine upgrade or repair.
- Enforce authorisation at the service/backend boundary, not just through interface visibility.
- Preserve condition, severity, confidence, applicability and issue state as separate concepts. Unsupported or stale findings must be **Unknown/Review**, not silently Pass/Fail.
- Maintain the diagnostic lifecycle: **Detect → Diagnose → Correlate → Refine → Rectify → Verify → Monitor.**
- Keep client/site information, device names and addresses, credentials, network diagrams, captured configurations, private source, operational logs, evidence images and internal commercial information **out of this public repository**, its history, issues, PRs and CI artifacts. Use synthetic examples only.

See [architecture](docs/ARCHITECTURE.md), [integration safeguards](docs/INTEGRATION_SAFEGUARDS.md) and [security policy](SECURITY.md).

## 3. Live issue register — prioritise the GitHub tracker

These are **external Windows-development observations awaiting source-level investigation and formal Windows acceptance**; they are not verified fixes or proof that the public repository contains the affected code.

| Issue | Concern | Required outcome |
| --- | --- | --- |
| [#4 — Locked files/running desktop processes](https://github.com/Jdorrington17/Raptora/issues/4) | Uninstall/update may encounter an Electron resource file-in-use / `EBUSY` condition while desktop processes are running. | Preflight detection, controlled application/service shutdown or a clear blocking prompt, safe failure/recovery, data preservation and upgrade/rollback regression coverage. |
| [#5 — Restricted PowerShell execution policy](https://github.com/Jdorrington17/Raptora/issues/5) | Default/restricted Windows PowerShell policies may block installer/maintenance scripts. | Supported install/maintenance without routine machine-wide policy changes; respect enforced organisational controls, use approved execution mechanisms, provide safe failure guidance and Windows policy-matrix tests. |

**Release position:** Treat unresolved critical installer/update/rollback failures as production-release blockers until the maintainer has reviewed reproducible fixes and genuine Windows platform evidence. Issue creation does not approve implementation, source migration or deployment.

At every session start, fetch **all currently open GitHub issues and relevant PRs**, not just the two entries above. Issue state may have changed since this snapshot. Check duplicates, linked code/reviews, explicit ownership, priorities and the actual accepted development baseline.

## 4. Mandatory external-issue intake

When a problem, improvement or design decision is identified **outside Codex**—for example in ChatGPT discussions, manually executed PowerShell checks, Windows installer trials, field feedback or stakeholder review—**create a GitHub issue or update the existing issue before treating it as part of an actionable Codex backlog**.

1. **Classify and sanitise first.** Decide whether the information can safely appear in this public repository. For confidential customer evidence, restricted source, credentials or security vulnerabilities, use approved private intake and `SECURITY.md`; publish only a generic non-sensitive tracking reference if appropriate.
2. **Search existing issues and PRs.** Add reproduction evidence or changed requirements to the canonical issue; avoid duplicates. If permissions prevent a GitHub update, explicitly report that tracking was **not** synchronised and prepare a public-safe draft for an authorised maintainer.
3. **Record at minimum:** concise title/component, affected build/version and OS (only when releasable), discovery date and source category, expected vs observed behaviour, sanitised reproduction steps, severity/priority, operational impact, evidence status, relevant dependencies, owner/approval status and measurable acceptance criteria.
4. **Separate fact from hypothesis.** Tag user-reported/manual evidence as external/unverified until the source and applicable test target have been inspected. State whether checks were synthetic, locally on Windows, or connected/authorised.
5. **Link implementation and verification.** Tie subsequent branches, commits, PRs, regression checks and release decisions to the issue. Update it when scope, priority or finding changes; close only with appropriate acceptance evidence or an explicit maintainer disposition.
6. **Synchronise the handover.** A fresh Codex session must read the tracker and identify any known off-Codex observations missing from GitHub. Chat memory alone is **not** issue synchronisation.

Use the [bug report form](.github/ISSUE_TEMPLATE/bug_report.yml) or [engineering task form](.github/ISSUE_TEMPLATE/engineering_task.yml). A submitted issue is a request for review, **not** blanket permission to modify live systems.

## 5. Codex startup sequence (every new or resumed session)

1. **Establish repository identity and state.** Confirm remote, default branch, current branch, HEAD, worktree changes, intended task and any unresolved prior handover. Preserve other work; do not reset, force-push, auto-stash, overwrite unknown files or start a duplicate PR.
2. **Read the current controls.** Start with `AGENTS.md`, this file, `CONTRIBUTING.md`, `SECURITY.md`, [environment setup](docs/CODEX_ENVIRONMENT.md), [agent workflow](docs/AGENT_WORKFLOW.md), [recovery](docs/AGENT_RECOVERY.md) and the [configuration register](docs/CODEX_CONFIGURATION_REGISTER.md).
3. **Reconcile live work.** Retrieve outstanding GitHub issues and PRs, linked branches, blockers and reviews. Check off-Codex findings have tracked issues; where they do not, prepare a public-safe issue or report the blocker. Select a narrowly scoped, explicitly approved requirement with acceptance criteria.
4. **Determine capabilities and permissions.** Verify actual accessible checkout, source availability, tools, role loading, sandbox and network restrictions. Never treat the existence of role/config files as proof a role is loaded. Keep at most **three total active agent threads** including the primary; use one for straightforward work.
5. **Run applicable bootstrap checks only.** Current governance baseline: `python3 scripts/verify-development-environment.py` (Windows: `py -3.11 scripts/verify-development-environment.py`) with Python 3.11+. Record command, platform, HEAD, outcome and limitations. Do **not** claim application or installer success from these checks.
6. **Plan, implement and review only within approved scope.** Use a focused branch/PR, relevant specialist review, synthetic fixtures, least privilege and explicit error handling. Source/Windows/connected actions remain subject to separate gates.
7. **Leave an evidence-based handover.** Include task/issue, branch/commit, changes, exact checks, Pass/Fail/Skipped/Blocked/Not run, unverified observations, risk, missing permissions, PR, owners and next required approval.

For interrupted work, follow [recovery guidance](docs/AGENT_RECOVERY.md) before repeating any previous operation.

## 6. Windows installer, update and rollback acceptance

Once **cleared application source** and an **authorised isolated Windows test environment** are available, evaluate the complete lifecycle: **Install → Configure → Validate → Operate → Update → Repair → Rollback**.

Minimum behavioural expectations:

- Record immutable candidate and previous-package identity, hashes, source lineage, schema compatibility, prerequisites and authorised backups before tests.
- Preserve service identity, installed component ownership and persisted configuration/history/evidence unless an **approved and tested** migration changes them.
- Handle running application windows, background processes, service stop/restart, locked packaged resources, restricted PowerShell policies and permission denial without corruption or silent partial success.
- Preserve data during failure, interruption, recovery and rollback. A failed upgrade must have an evidenced safe outcome; do not delete application data or unknown files to make removal succeed.
- Test actual Windows service, desktop start/stop, reboot/autorun, update/repair/rollback, version downgrade policy and user-visible failure guidance on isolated approved targets.
- Distinguish synthetic/unit checks, Windows platform validation, and separately authorised connected integration acceptance. None substitutes for another.

Current evidence is insufficient for production release from this public repository. Follow [build and release policy](docs/BUILD_AND_RELEASE.md) and the [source-gated activation plan](docs/SOURCE_ACTIVATION_PLAN.md).

## 7. Definition of done and reporting contract

For each change, provide:

- **Traceability:** approved issue/requirement, impacted modules, branch/commit and associated PR.
- **Change summary:** actual files, behaviour changed, compatibility and data migration impact.
- **Verification:** exact commands, environment, tested SHA, executed counts and outcome. Explicitly distinguish Pass, Fail, Skipped, Blocked and Not run; record what could not be tested.
- **Security and provenance:** confidential-data/rights check, permissions exercised, dependency or lifecycle risk, and synthetic versus real-Windows versus connected test scope.
- **Closure decision:** acceptance criteria met or outstanding; reviewer approval required; issue updated; release blockers identified. Do not self-merge or self-release.

**Do not declare release-ready** solely because governance CI passes, a GitHub issue is closed, a file checksum matches, a Linux suite passes or an installer script completes. Release requires appropriate source-level, Windows lifecycle, security and human approval evidence.

## 8. Canonical references

- [Engineering rules](AGENTS.md) · [Contribution policy](CONTRIBUTING.md) · [Security disclosure](SECURITY.md)
- [Project status](docs/PROJECT_STATUS.md) · [Roadmap](docs/ROADMAP.md) · [Architecture](docs/ARCHITECTURE.md)
- [Codex environment](docs/CODEX_ENVIRONMENT.md) · [Agent workflow](docs/AGENT_WORKFLOW.md) · [Agent usage](docs/AGENT_USAGE.md) · [Recovery](docs/AGENT_RECOVERY.md) · [Configuration register](docs/CODEX_CONFIGURATION_REGISTER.md)
- [Source activation](docs/SOURCE_ACTIVATION_PLAN.md) · [Build and release](docs/BUILD_AND_RELEASE.md) · [Migration safeguards](docs/INTEGRATION_SAFEGUARDS.md)
- [GitHub issues](https://github.com/Jdorrington17/Raptora/issues) · [GitHub pull requests](https://github.com/Jdorrington17/Raptora/pulls)

**Maintenance rule:** Update this document when the repository phase, critical workflow or canonical links change. Keep live issue details in their GitHub records, not in accumulating anecdotal chat summaries.
