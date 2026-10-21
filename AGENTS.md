# Raptora engineering-agent instructions

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

## Outside contributions
Public activity is monitored at the metadata level. Handle reports and PRs professionally; do not attempt to identify anonymous visitors, collect IP addresses, or disclose security reports publicly.
