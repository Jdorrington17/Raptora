# Codex engineering configuration register

Snapshot: 21 October 2026. Scope: Step 2 development hardening, based on the existing Step 1 five-agent framework. This is a feature-branch assessment, not confirmation that main, a new Cloud task or an installed application has adopted these settings. No private legacy audit is started by this task.

## Completed and validated locally

| Setting/capability | Evidence/status | Security and usage implication |
| --- | --- | --- |
| Five specialist roles and metadata | Existing files preserved; version-matched 0.163.0 schema validated | No additional model, credentials, sandbox or approval overrides |
| Project agent settings | Strict CLI parser accepted enabled agents, cap 2, depth 1 in an isolated user-layer copy | V1 two children plus primary; V2 two total; at most three total by orchestration policy |
| Cloud generic delegation | Scoped public-file governance and reference reviews returned results | Instruction-based fallback works; shared workspace and inherited permissions remain authoritative |
| Project instructions | Primary and reviewers read current AGENTS.md; safeguards retained | Manual reading verified; automatic loading in a new client/task is not inferred |
| Four project reference skills | Frontmatter/structure and scenario dry-runs validated; installed CLI discovered all four enabled, zero project errors | No extra agents or continuous automation; load only relevant reference |
| Environment requirements | Git, Python 3.11+, inspected Codex CLI 0.163.0; read-only verifier and negative configuration tests | No Node/pnpm install, dependency cache, secrets or product scaffold in source-free phase |
| Existing bootstrap Actions | Read-only token, credential-free checkout, engineering-config verification only | No product checks, artifact upload or privileged PR execution added |
| Public-activity workflow | Metadata-only `pull_request_target`; no source checkout/execution | Preserve this boundary; do not turn it into a validation/deployment job |
| Contribution/issue/PR workflow | Public-safe bug/task forms and template review evidence supplied | Issue/PR creation is not approval; outside code still needs ownership/security review |
| Recovery and handover | Branch/HEAD/dirty state, worker ownership and check outcome contract documented | Preserve unknown changes; no automatic reset, installer recovery or self-merge |

## Configured or designed, not operationally verified

| Item | Missing evidence / next action | Owner |
| --- | --- | --- |
| Native custom-role invocation | Trusted client must demonstrate each loaded role/instructions and returned result; Cloud spawn schema has no role selector | Codex administrator and lead |
| Automatic Cloud skill/instruction loading and hard concurrency enforcement | Verify in a new approved task; local CLI discovery does not establish Cloud loading | Codex administrator |
| Fresh Cloud restoration/startup | Reconcile existing environment install/start settings, then test a new task | Environment administrator |
| GitHub Actions results for current SHA | Local equivalent commands are distinct from a hosted run; inspect current tested SHA/check conclusion | Maintainer/QA |
| Draft PR and current remote reviews/checks | Git push access works; API reads/creation returned Forbidden; prepare description and report actual result | Maintainer with API/UI access |
| Private legacy audit | Procedure only; Step 3 must wait for Step 2 completion and review plus approved private scope/storage | Security/IP owners and lead |

## Manual GitHub/Codex administration — unverified

API administration requests returned Forbidden. No server-side settings were modified or declared enabled.

| Control | Required administrative decision/verification |
| --- | --- |
| Branch protection/rulesets | Protect main; require independent PR review and stable applicable checks; dismiss stale approvals, restrict bypass/force-push/deletion and verify administrator policy |
| Required checks | Bind actual governance check identities now; add product gates only after real source/jobs exist; never require nonexistent green placeholders |
| Review ownership | Nominate actual maintainers/CODEOWNERS and backup reviewers; no invented team handles or self-approval |
| Actions/forks | Default read-only token; approve outside workflow runs per policy, restrict allowed actions, prohibit secrets/private mounts in untrusted jobs and review runner trust |
| Reporting/scanning | Verify private vulnerability reporting/contact, secret scanning/push protection and dependency alerts where available; do not enable paid products without approval |
| Cloud isolation | Keep public contributor tasks separate from private checkouts, audit evidence and credentials; prose is not access control |
| Permissions/trust/network | Verify actual project trust, managed sandbox/tool access, scoped Git/API authorization and network policy; never extract tokens or bypass controls |
| Usage/artifacts | Confirm Actions/Codex budgets, cancellation and retention policy; no recurring workers or unnecessary artifact uploads/caches |

## Deferred until cleared source migration

Node/pnpm versions and frozen install/cache keys; TypeScript/React builds; real unit/integration/regression tests; Windows PowerShell/SDK validation; Electron/installer packaging; update/repair/rollback acceptance; dependency/licence/SBOM/security gates; release tags/signing/provenance and fail-closed product PR gates are **designed, not activated** in [SOURCE_ACTIVATION_PLAN.md](SOURCE_ACTIVATION_PLAN.md).

No application dependency manifests or test-success placeholders are introduced. Detailed private IP/secrets/customer/history/provenance clearance is planned in [PRIVATE_MIGRATION_AUDIT.md](PRIVATE_MIGRATION_AUDIT.md), with results outside this public repository. Source publication, connected testing, signing and deployment need separate approvals.

## Evidence and readiness decision

See [AGENT_VALIDATION.md](AGENT_VALIDATION.md) for exact local/runtime outcomes and [CODEX_ENVIRONMENT.md](CODEX_ENVIRONMENT.md) for reproducibility. Governance checks may be operational locally while native Cloud discovery, hosted CI and admin controls remain unverified. Step 2 becomes a reviewed baseline only after maintainer review; this register does not authorize Step 3, source import or product release.
