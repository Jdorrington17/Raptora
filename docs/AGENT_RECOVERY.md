# Interrupted-task recovery and validation records

Keep public-safe task checkpoints in an approved task record or PR description. Confidential audit/security records belong in private storage outside this checkout. Before stopping, record requirement, branch/HEAD, dirty files, ownership, completed actions, exact checks/results, live worker state, pending commands, blockers and required next action. Never include secrets or customer evidence.

On resume:

1. Read the checkpoint and current instructions. Inspect branch, HEAD, `git status --short` and diff before trusting prior claims. Check remote branches/PRs where accessible; an API denial leaves PR/check state unverified.
2. Inspect available agent/session state and ask existing workers for scoped status before creating new workers. Keep at most three total active threads; do not repeat completed work or edit another worker's files. If the previous session's workers are unavailable, mark them unavailable and reconstruct ownership from evidence.
3. Reconcile unexpected files/commits without resets, automatic stashes, deletion or force-push. Preserve unknown changes and escalate an ownership conflict while continuing independent work.
4. Determine whether a pending command finished from its tool/session status and fresh artifacts/results. Do not infer completion from a PID, log tail, old output or previous green CI. Re-run only checks invalidated by changes or uncertainty; record tested SHA and dirty state.
5. Resume the earliest incomplete dependent step. Never restart installers, recover Windows transactions, change services or touch ProgramData from a coding-task checkpoint; those require a separately approved target and exact recovery evidence.
6. Revalidate the combined result and prepare a draft PR. If creation fails, record the branch/commit, prepared description and exact failure; a compare/create URL is not an existing PR. Do not merge or deploy.

## Result contract

| Field | Record |
| --- | --- |
| Target | Requirement, source HEAD, dirty-tree state, affected modules/files |
| Check | Exact command, working directory, environment/platform and tested SHA |
| Outcome | Pass, Fail, Skipped, Blocked or Not run; counts and underlying exit status |
| Evidence/limit | Current-run evidence, synthetic vs actual Windows vs connected scope; unavailable inputs |
| Handover | Remaining steps, ownership, approvals, PR URL or publication blocker |

A configuration check returning zero validates only its stated governance scope. Zero executed application tests never establishes product readiness. See the verification and PR-handover skills and [AGENT_USAGE.md](AGENT_USAGE.md).
