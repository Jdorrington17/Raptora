# Reproducible Codex environment

Current repository scope: engineering governance/configuration, not a migrated application. Setup needs Git and Python **3.11+** (standard library only). Codex CLI **0.163.0** is the inspected compatibility baseline; hosting Cloud tools can have separate capabilities. No Node, pnpm, Windows SDK, secret or dependency installation is needed for the current checks.

## Existing-checkout startup

1. Use the existing isolated checkout; inspect `git status --short`, current branch/HEAD and remote work before editing. Do not create a worktree unless explicitly requested. Preserve other-task changes and coordinate file ownership.
2. Read AGENTS.md, docs/AGENT_USAGE.md and the configuration register. Use an approved feature branch; extend active work rather than duplicating its framework or opening competing PRs.
3. Run `python3 scripts/verify-development-environment.py` (Windows: `py -3.11 scripts/verify-development-environment.py`). It verifies governance prerequisites and local policy without downloads, installation or state changes. Missing Codex in ordinary GitHub CI is explicitly Not run, not a product-test success.
4. Optionally run `python3 scripts/check-codex-runtime.py` with the inspected CLI installed. It uses temporary config without user credentials to verify settings and skill discovery, makes no model turn and does not certify native roles or Cloud loading. This check is not required in ordinary CI.
5. In the approved Codex client, verify project trust, actual sandbox/tool access, model availability and role/skill discovery. Do not alter managed permissions, extract credentials, run model-login flows or bypass trust to simulate support. Follow the manual fallback when automatic discovery is unavailable.

A fresh checkout of an approved branch plus these commands reproduces the governance checks. This does not reproduce a Cloud filesystem snapshot, authenticate a CLI session or prove application rebuilds. Record OS, Python/Git/Codex versions, HEAD/dirty state and command outcomes. The current files introduce no model pin, secrets, third-party executable hook or permission override.

## Cloud administration and isolation

Keep one authoritative environment setup. An administrator should reconcile existing cloud install/start instructions with this source-free phase; do not add a second script that attempts nonexistent application installs. Project files do not automatically change Cloud startup, network allowlists, secret bindings or concurrency enforcement. Those require settings access and validation in a new task before claiming restoration.

Public contribution tasks must not receive the private legacy checkout, credentials, confidential audit artifacts or write-enabled tokens. Git read access and read-only agent prose are not data-isolation controls: a checkout visible to untrusted code can be read and exfiltrated. Use a separate approved private audit environment with scoped access, private output and trusted reviewers. Preserve existing private checkouts; do not delete or expose them as part of public-task setup.

Use platform-injected authentication only for authorized operations. Do not request or print token values. Git proxy access does not establish GitHub API/admin access. Network/package access should be added only for the later reviewed source workflow. Nothing here changes installed software or performs connected tests.

Future dependencies, Windows tools and product commands are activation-gated in [SOURCE_ACTIVATION_PLAN.md](SOURCE_ACTIVATION_PLAN.md). See [configuration register](CODEX_CONFIGURATION_REGISTER.md) for actual evidence and manual settings.
