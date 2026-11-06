# Windows candidate preflight (manual, read-only)

This workflow complements the existing [Windows runner smoke](../.github/workflows/windows-acceptance-smoke.yml). It is **not** an installer execution test, application CI, recovery procedure, or release approval.

## Scope and trust

- Workflow: `.github/workflows/windows-candidate-preflight.yml`.
- Runs only on a manual `workflow_dispatch` from the reviewed `main` branch, initiated by the repository owner.
- Uses the already registered runner labels `self-hosted, Windows, X64, raptora-acceptance`; does not provision infrastructure.
- Requires one reviewed SHA-256 of an unsigned candidate. The candidate **must remain off the public checkout**.
- Checks local staged file integrity, installed platform/journal state and existing Raptora process count. It never starts setup, kills processes, installs, updates, uninstalls, repairs or recovers.
- Publishes only a sanitised JSON summary without local paths, private binary content or command lines.
- The workflow is on a feature branch until explicitly reviewed and merged. Only then can an authorised maintainer dispatch it from Actions.

## One-time VM-side configuration (operator controlled)

The Windows runner VM must have the following **machine-scope environment variables**, configured outside GitHub and available to the runner service:

- `RAPTORA_ACCEPTANCE_CANDIDATE`: full local path to the reviewed staged x64 setup executable.
- `RAPTORA_ACCEPTANCE_APP_ROOT`: local installed application root where `.installer` journals would be found.

Do not place their values in this public repository, issue comments or workflow inputs. Do not configure the runner to point to operational/customer systems. Ensure the runner service can read the candidate without changing Windows execution policies persistently. If variables are missing, the workflow reports `BLOCKED` rather than guessing locations.

The operator must ensure the VM is powered on and the registered runner is online. A runner smoke PASS proves connectivity only, not that the candidate or VM is safe for application execution.

## How to use after review/merge

1. Stage a privately produced candidate on the authorised runner VM and verify provenance independently. Do not move private source to public GitHub.
2. In **Actions → Raptora Windows Candidate Preflight → Run workflow**, select `main`.
3. Enter the exact candidate SHA-256 into `expected_sha256`. Do not submit host paths.
4. Review the job summary and the sanitised preflight artifact.

Interpretation:

| Result | Meaning |
| --- | --- |
| `PASS` | File hash and limited read-only runner-state gates passed. **No installer was executed.** |
| `FAIL` | Candidate SHA-256 mismatch. **Do not execute.** |
| `BLOCKED` | Missing configuration, pre-existing processes, incomplete platform/journal state, or other uncertain prerequisite. Operator review required. |

The known incomplete Development.8 transaction and running installer processes should block progression on an unchanged acceptance VM. **Do not delete journals, terminate processes or restore a checkpoint automatically** to force a passing result.

## Next engineering gate

A separate reviewed workflow/harness must test actual Windows dual-launch behaviour using a known-good, isolated state and confirm its packaged app identity. A self-hosted runner operating as a Windows service may not have an interactive desktop session. Do not represent a headless job as proof that two GUI windows were handled correctly.

Before any real install/maintenance test, obtain the operator's explicit approval of the exact scenario, verify a recoverable checkpoint, preserve application and customer data baselines, and record acceptance evidence privately.

Tracked defects: [#25 — duplicate setup/concurrent maintenance](https://github.com/Jdorrington17/Raptora/issues/25) and [#4 — installer recovery and file locking](https://github.com/Jdorrington17/Raptora/issues/4).
