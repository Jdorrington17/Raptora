# Hybrid Codex coordination and Windows acceptance handover

**Status:** proposed working agreement; see [issue #10](https://github.com/Jdorrington17/Raptora/issues/10). Maintainer review is required before adoption.

## Purpose and boundaries

Use **Codex Cloud** for reviewed Raptora application development, and a **trusted local Codex desktop environment** for local data-management tooling, Windows verification, and confidential evidence handling. GitHub issues, PRs and reviewed commits are the shared engineering record. Native Codex Remote Control supports an authorised human operator interacting with a host; it is **not** an automatic cloud-agent-to-local-agent execution link.

This public repository must never contain confidential data, internal host names, device addresses, credentials, private build contents or original customer evidence. Use synthetic fixtures and sanitised summaries only. See `AGENTS.md`, `CODEX_CONTEXT.md`, and `SECURITY.md`; those controls take precedence over this workflow.

## Responsibility matrix

| Capability | Cloud Codex | Local Codex / Windows operator | Maintainer |
| --- | --- | --- | --- |
| Scope and engineering issue | Propose, investigate, link evidence | Submit sanitised findings | Approve scope/priority |
| Application changes | Implement on reviewed feature branch and PR | Do not create competing feature branch for the same change | Review and merge |
| Tests with synthetic data | Run in cloud where source and commands are available | Optional independent verification | Review evidence |
| Windows lifecycle acceptance | Request approved test with exact SHA/package hash | Confirm target/backup, perform authorised test, capture local evidence | Approve intrusive test scope and release decision |
| Confidential evidence | No direct public repo access | Retain local evidence and private supporting detail | Approve any publication of a redacted summary |
| Remote session | Not assumed to control local agent directly | Pair/manage remote connections and approve interactive commands | Retain release/deployment authority |
| Production deployment | Not authorised implicitly | No unattended customer-system changes | Explicit release/deployment approval |

## Two separate connection paths

### 1. Interactive remote access

An authorised device owner installs the supported ChatGPT/Codex desktop app on a trusted Windows host, signs in, and sets up **Settings > Connections > Control this PC**. Pair the controlling device with the on-screen QR code. Test that a local project and an approval prompt can be accessed from the controlling device. Keep the host awake, online, and running the app.

Remote approval and workspace permissions stay in effect. This step is completed **outside GitHub**, so do not mark it successful based on a PR or documentation commit. See [official remote connections guidance](https://learn.chatgpt.com/docs/remote-connections).

### 2. Repeatable Windows checks

Reuse the **existing single on-demand Windows acceptance runner** and `.github/workflows/windows-acceptance-smoke.yml`. It is deliberately `workflow_dispatch` only, scoped to trusted `main` and an authorised owner. Do not enable pull-request/fork triggers, pass arbitrary shell commands from workflow inputs, assume offline runner readiness, or expose persistent host credentials to unreviewed code.

The successful runner smoke proves connectivity and runner-service operation **only**; it does not prove installer or data-preservation acceptance. As application source is cleared and reviewed, add task-specific Windows tests in separate reviewed PRs, never by weakening this trust boundary.

## Standard GitHub handover record

Use one GitHub issue as the canonical unit of work and link associated PRs. For development-to-Windows acceptance, add the following fields in the PR body or a public-safe issue comment:

```text
RAPTORA HANDOVER
Issue/PR:
Requesting environment: Cloud / Local operator
Task and acceptance criteria:
Reviewed source branch and exact commit SHA:
Candidate package ID and SHA-256 (if applicable):
Test type: synthetic / Windows platform / connected (separate approval)
Required operations: read-only / install / update / repair / rollback / other
Human approval reference: pending / granted (no private details)
Expected results:
Known dependencies/blockers:
Evidence location: public sanitised summary / private local record (no path)
Outcome: NOT RUN / BLOCKED / PASS / FAIL
Observations and exclusions:
Next responsible owner and action:
```

Do not put passwords, addresses, customer/system identifiers, sensitive paths, raw installer logs or captured evidence in this record. Where package provenance is not yet cleared for publication, mark the public reference **RESTRICTED / HELD LOCALLY**.

## Operating sequence

1. **Select:** Review live open issues, PRs and `CODEX_CONTEXT.md`. Verify the actual source baseline; public repository bootstrap files are not the application.
2. **Build:** Cloud Codex works only in an approved, scoped feature branch. It submits a reviewed PR with exact checks and non-executed checks disclosed.
3. **Request:** When Windows work is needed, attach a handover record with exact reviewed source commit and package provenance. A request does not authorise execution.
4. **Approve:** The operator verifies runner availability, test isolation, backup/checkpoint, permissions and the requested commands. Installer/service/data changes require explicit approval.
5. **Run:** The operator starts the existing VM on demand and dispatches only the approved workflow against trusted code. Remote Codex sessions are controlled independently by the authorised user.
6. **Record:** Preserve original logs and sensitive evidence locally. Publish only appropriate sanitised status, counts, provenance, exclusions and issue references.
7. **Close:** Maintainer verifies acceptance criteria and appropriate tests. Failed, missing, blocked or skipped checks do not become PASS. No autonomous merge, signing, release or customer deployment.

## Bootstrap checklist

- [ ] Windows host remote connection paired and verified by operator (outside GitHub).
- [ ] Local Codex project/checkout and current branch/HEAD verified.
- [ ] Cloud Codex environment bound to the approved repository; startup instructions loaded.
- [ ] Existing runner smoke rechecked when Windows acceptance is next needed.
- [ ] First non-destructive, synthetic handover rehearsed with exact SHA and sanitised PASS/FAIL result.
- [ ] Source migration/rights clearance and installer issue #4/#5 remediation tracked independently.

**Release position:** Engineering coordination can proceed without migrated product source; application builds, lifecycle acceptance and release approval remain gated by the existing source-activation and Windows-test policies.
