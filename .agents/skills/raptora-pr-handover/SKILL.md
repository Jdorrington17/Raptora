---
name: raptora-pr-handover
description: Use when preparing a Raptora pull request, handing engineering work to a reviewer, or resuming an interrupted task before submission.
---
# Hand over a reviewable change

Inspect actual branch/HEAD, status/diff, active ownership and existing remote work. Preserve unexpected edits; resume from docs/AGENT_RECOVERY.md instead of resetting or duplicating work. Use a focused feature branch and the existing PR template.

Produce the description in this order:

1. Approved requirement, concrete problem and resulting behavior.
2. Scope, affected files/contracts and compatibility or regression exposure.
3. Exact checks, tested SHA/dirty state, outcomes/counts and unrun gates. Label prior evidence and platform limits explicitly.
4. Public-safe security/ownership conclusion, risks, required independent reviews/approvals and next action.

Exclude credentials, customer material, private source and confidential findings from every public field, commit message, log and artifact. A draft PR is publication, not private storage. No source import without explicit rights/security clearance. Do not claim a green suite from zero tests or accept Windows behavior from Linux results.

When authorized, create a draft using a structured API argument or `gh pr create --draft --body-file <prepared-file>`; preserve real newlines. Never self-merge. If API access is denied, retain the prepared description and report **branch, commit, attempted operation, exact blocker and create/compare link labelled as such**. Do not invent a PR URL or treat a pushed branch as an opened PR.
