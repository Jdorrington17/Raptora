# Agent workflow

**Requirement → Architecture Review → Implementation → Security Review → Testing → Pull Request → Approval**

Apply relevant stages in proportion to risk. A documentation fix generally needs one agent and focused verification. A service/installer or public-source change needs specialist review and platform/security evidence. Do not invoke all roles automatically.

## Intake and delegation

1. Identify the approved requirement/issue, scope, acceptance criteria, affected modules and dependencies. Identify public/private information boundaries before reading or sharing sensitive evidence.
2. Inspect current files, instructions, status and remote branch context. Preserve user changes and existing governance. Work on a dedicated feature/fix/docs branch; never commit directly to main.
3. Choose only useful independent tasks. The primary keeps implementation dependencies sequential and a maximum of three total active threads. Give each worker this brief:

```text
Requirement/issue and approved scope:
Role and specific question/deliverable:
Allowed files / ownership (or read-only):
Inputs and information classification:
Acceptance criteria and checks:
Other workers / dependencies / stop conditions:
Permissions and approvals already provided:
```

4. Architecture review is required for changed module boundaries, technology or persisted contracts. Preserve the established service/UI/worker separation and compatibility unless an approved migration changes it.
5. Implement the approved slice, using typed contracts, explicit errors, synthetic fixtures and meaningful regression coverage. Coordinate before editing files owned by another worker.

## Review and evidence

Security review checks backend authorization, sensitive data, external code/dependency rights, public history/diffs and CI exposure as relevant. Private findings must never enter public issues, PRs, logs or artifacts. Use an approved private record; when unavailable, report the handling blocker without disclosing details. Source publication requires rights and migration clearance before the public PR is opened.

QA records each check as Pass, Fail, Skipped, Blocked or Not run with exact command, source target, count where applicable and limitations. Keep unit, synthetic, Windows platform and connected acceptance distinct. Do not equate Linux results with Windows service/installer acceptance or use bootstrap CI as product validation.

Windows review covers install/configure/validate/operate/update/repair/rollback, preserved service identity and paths, configuration/history/evidence and known-good recovery. Actual platform work requires a separately approved test target and backup/recovery plan. Agent setup grants no installed-machine changes, connected tests, signing, release or production authorization. Never delete ProgramData or reset configuration as routine maintenance.

## Integration and pull requests

The primary consolidates findings, resolves conflicts against evidence, reviews the combined diff, runs relevant checks and verifies acceptance. An implementer cannot approve its own changes. External contributions need security and ownership review; do not expose secrets to untrusted PR jobs or execute outside code in privileged `pull_request_target` workflows.

Prepare a focused draft PR describing requirement, scope/files, validation, security/ownership review, known limitations and approvals. Preserve existing branch protection and manual review; do not merge failing required checks, force-push protected branches or self-merge. Read protection/check status when available; an API denial means unverified, not disabled or waived.

Final report: what changed; files; tests/results and unrun checks; risks/approvals; PR link or precise publication blocker; next recommended action. A configuration parser accepting files is not evidence that a role was invoked. A role invocation is not evidence of every role's capabilities.

## Legacy migration hold

The private legacy repository remains unchanged and reference-only. Never assume its default branch is authoritative. Current installed development version is user-reported `0.9.0-development.3`; this framework does not verify its binary/source identity. Reconcile exact development commits, outstanding work, manifests, rights and sensitive history in a private approved audit before migration. Do not publish private audit details or create a replacement product to bypass that gate.
