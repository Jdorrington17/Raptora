# Raptora engineering-agent instructions

**Startup context:** Read [CODEX_CONTEXT.md](CODEX_CONTEXT.md) at the beginning of each new or resumed Codex task. Reconcile live GitHub issues/PRs and sanitised off-Codex findings before selecting work. The context file does not override the safety, source-migration or approval controls below.

## Scope and safety
This is a public repository. Treat every commit, pull request, Actions log and artifact as publicly accessible, including history after later deletion.

Never introduce customer names, site identifiers, camera/device IPs, captured configurations, screenshots of operational evidence, credentials, vendor tokens, unrestricted network diagrams, private repository contents, or internal commercial details. Use synthetic fixtures.

The application is intended to function independently of hosted AI or a developer's ChatGPT/Codex session. Preserve local-first, read-only-by-default behaviour and explicit human approval for intrusive or privileged operations.

## Source and migration
The repository currently contains governance files, not the verified application codebase. Do not invent or create a greenfield replacement as a shortcut.

Before moving legacy source into this public repository:
1. Obtain explicit approval for public source release and verify the right to publish it.
2. Review the full commit history **and** proposed files for credentials, customer data, internal network details, restricted vendor code and incompatible licences.
3. Reconcile exact development commits, outstanding pull requests and tested installer provenance.
4. Document exclusions and sanitisation evidence in a private review record, not this public repo.
5. Migrate only cleared source on a separate feature branch; require review before merge.

Do not modify legacy repositories, release tags, user data, deployed Windows services or connected customer systems as part of this bootstrap.

## Development workflow
- Use feature/fix/docs branches and narrowly scoped pull requests.
- Never force-push protected branches, push directly to main or auto-merge outside submissions.
- Keep minimal permissions on workflows and do not check out or run outsider-provided code in privileged `pull_request_target` jobs.
- Preserve operational state, update/rollback compatibility, data retention boundaries and evidence provenance when the application is introduced.
- Treat missing, stale or unsupported evidence as Unknown/Review rather than inventing healthy or faulty states.
- Enforce permissions at backend boundaries; UI filtering alone is insufficient.

## Validation and reporting
Until application source is migrated, CI checks only documentation/governance prerequisites. Do not claim functional, Windows installer, connected device or production acceptance.

When application source exists, inspect its own package manager and scripts before implementing actual code-validation workflows. Separate synthetic checks from Windows packaging, connected acceptance and release authorisation.

Every PR summary must record scope, files, test commands/results or not-run status, risks, security review, and outstanding approvals.

## On-demand Windows acceptance runner

- **Architecture:** Keep this public Raptora repository as the sole engineering source of truth. Use the **existing, single Windows acceptance VM** as an on-demand GitHub Actions self-hosted runner; do not create additional VMs or repositories for this purpose without a maintainer decision. Keep host identities, IP addresses, network topology and private build contents out of this public repository.
- **Availability:** The operator starts the VM only when Windows acceptance is needed and shuts it down afterward. Codex does not assume it is online, remotely power it on, or require it for unrelated design, documentation or source-level work. When the VM is offline, queue/plan acceptance separately and report those Windows checks as **NOT RUN** or **BLOCKED**, never PASS. An online runner must be verified before scheduling; a registered service alone is not proof of availability.
- **Runner registration:** The intended runner belongs to **this** repository, with the additional label `raptora-acceptance`. Its Windows service may start automatically **when the VM boots**; this is not permission to run arbitrary jobs. Runner registration, label, availability and repository association must be verified before claiming the integration works.
- **Triggering and trust:** Begin with `workflow_dispatch` only, initiated by an authorised maintainer against a reviewed, exact commit/build. Never send public `pull_request`, `pull_request_target`, fork, contributor-submitted or otherwise untrusted workflows/code to this persistent runner. Never give unreviewed PR code access to its workspace or credentials. Enforce trusted-branch/revision checks and minimal token permissions; public status and workflow files do not themselves authorize deployment.
- **Approval and safety:** Read-only smoke checks may precede installation tests. Installing, upgrading, stopping services, uninstalling, repairing or rolling back requires a named, reviewed test scope and explicit operator approval. Before destructive testing, verify a recoverable VM checkpoint/backup and preserve persisted application data. Do not target customer systems.
- **Evidence and traceability:** Every Windows acceptance attempt must identify the exact source commit, package hash and provenance, runner/test environment, executed commands, timestamps, results (PASS/FAIL/BLOCKED/NOT RUN) and any rollback or integrity checks. Keep raw logs, private builds and sensitive evidence outside public GitHub artifacts; publish only synthetic or sanitised summaries and links to applicable Raptora issues/PRs. Update tracked issues for defects, including off-Codex findings, with reproducible non-sensitive acceptance criteria.
- **Release gate:** Linux tests, governance CI or Cloud Codex results cannot substitute for verified Windows installer, service, upgrade or rollback acceptance. A candidate with pending Windows acceptance remains unverified for those capabilities; no automatic release approval. Current source-migration, rights and confidentiality gates remain in force.

## Outside contributions
Public activity is monitored at the metadata level. Handle reports and PRs professionally; do not attempt to identify anonymous visitors, collect IP addresses, or disclose security reports publicly.

## Preserved product engineering requirements

# Raptora product engineering requirements

## Product
Raptora is a proprietary, local-first security monitoring,
diagnostics, evidence and reporting platform.

The installed application must operate independently of
ChatGPT, Codex and external AI services.

## Architecture
Preserve and improve the existing architecture:
- React/TypeScript desktop interface
- Continuously operating Windows core service
- Isolated worker/adaptor execution
- Milestone XProtect integration
- PowerShell collectors behind controlled boundaries
- Persistent configuration, diagnostic history and evidence
- Controlled Windows installation, update, repair and rollback

Do not replace established technologies without evidence,
a migration plan and explicit approval.

## Development ownership
This repository is the primary Raptora source of truth.
The legacy Certis-Milestone repository is read-only
migration reference material.

Never assume the legacy main branch is the newest baseline.
Inspect source branches, releases and manifests first.

## Engineering requirements
1. Inspect existing code before making changes.
2. Prefer minimal, maintainable and testable changes.
3. Preserve existing working functionality.
4. Keep the interface, service and workers separated.
5. Use typed contracts and explicit error handling.
6. Maintain backward-compatible persisted data where feasible.
7. Never hardcode credentials or client information.
8. Do not commit runtime data, logs, secrets or evidence.
9. Use test fixtures or synthetic data for development.
10. Update relevant documentation when changing behavior.

## Diagnostic lifecycle
Detect → Diagnose → Correlate → Refine Diagnosis →
Rectify → Verify → Monitor

Represent condition, severity, confidence, applicability
and issue state independently.

## Windows deployment
Maintain support for:
- Install
- Configure
- Validate
- Operate
- Update
- Repair
- Rollback

Preserve service identity, installation paths and stored
configuration until an approved migration changes them.

Never delete ProgramData or reset user configuration
as a routine repair or upgrade action.

## Quality gates
For every substantive change:
- Identify impacted modules.
- Run relevant existing tests.
- Add regression coverage where practical.
- Report tests that could not run.
- Validate Windows-specific changes on Windows.
- Confirm installer and rollback compatibility when impacted.
- Document known limitations.

Do not claim that Linux test success validates Windows
service or installer functionality.

## Git workflow
- Do not commit directly to main.
- Use focused feature or fix branches.
- Use pull requests for integration.
- Do not force-push protected branches.
- Do not merge failing required checks.
- Preserve release tags and source provenance.

## Work reporting
At the end of each task, report:
1. What changed
2. Files affected
3. Tests executed and results
4. Risks or unresolved issues
5. Recommended next action

## Security
Treat client site information, camera names,
IP addresses, credentials, access control data
and security topology as sensitive.

Do not introduce telemetry, external connections,
remote access or production deployment without approval.

## Specialist orchestration

The primary agent coordinates the five roles in `.codex/agents/`: `architect`, `developer`, `security-reviewer`, `qa-engineer` and `windows-deployment`. Read [agent architecture](docs/AGENT_ARCHITECTURE.md), [workflow](docs/AGENT_WORKFLOW.md) and [usage](docs/AGENT_USAGE.md).

Keep at most three active threads including the primary; use fewer for straightforward work. Delegate independent tasks only, assign file ownership and acceptance criteria, prohibit recursive delegation and consolidate evidence before integration. Role instructions do not grant permissions or guarantee sandbox isolation. CLI configuration is not proof of Cloud role loading.

Use Requirement → Architecture Review → Implementation → Security Review → Testing → Pull Request → Approval, applying the relevant stages. Work on a focused branch, preserve existing safeguards and require maintainer review; do not self-merge. Configuration setup does not authorize private-source migration, product implementation, connected tests or deployment.

## Engineering hardening references

Use the focused project skills under `.agents/skills/` when relevant; see [skill usage](docs/AGENT_SKILLS.md). Start with [environment verification](docs/CODEX_ENVIRONMENT.md) and report current evidence using [recovery and handover](docs/AGENT_RECOVERY.md). The [configuration register](docs/CODEX_CONFIGURATION_REGISTER.md) distinguishes verified, manual and deferred controls. Keep disagreements evidence-based: the primary resolves scope/ownership conflicts and escalates unresolved safety or acceptance decisions to the maintainer without inventing approval. Do not start the private legacy audit until Step 2 is completed and reviewed; its public-safe procedure grants no access or publication authority.
