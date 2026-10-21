# Agent usage

Start one primary Codex session in the repository. Ask it to select relevant roles; do not start five permanent workers.

Example requests:

```text
Review this approved contract change with architect. Return impacted modules and
compatibility risks before implementation; do not edit product code.

Implement issue <number> on this feature branch. Use developer for the scoped patch,
then qa-engineer for independent regression review. Keep at most three total threads.

Ask security-reviewer to assess this proposed public diff and dependency change.
Return a sanitized conclusion; keep confidential details outside the repository.

Ask windows-deployment for an installer update/repair/rollback acceptance plan.
Do not run installers or change the installed environment.
```

## Codex CLI

The setup was checked against CLI **0.163.0**, not assumed compatible with older releases. From the repository root, run `codex --version`, then `python3 scripts/validate-agent-config.py` (Windows: `py -3.11 scripts/validate-agent-config.py` with Python 3.11+). Start `codex` in the normal approved client. Project trust and managed policy must allow loading `.codex/config.toml`; do not bypass trust, hook approval, sandbox or policy to make roles load.

Ask the primary to delegate using the registered role names `architect`, `developer`, `security-reviewer`, `qa-engineer` or `windows-deployment`. These are role names for the model's supported spawn tool, not shell subcommands. There is no invented `codex agent run <name>` command. The installed CLI's `codex agents` command browses sessions; it is not a custom-role launcher.

Before relying on a new runtime/version, verify role loading, effective permissions and concurrency against its official documentation/source. In a disposable authorized session, request a read-only public-file review using one role and verify the worker's loaded role/instructions and returned result. Do not infer role loading from TOML syntax alone.

## Codex Cloud / host-provided tools

This Cloud session exposes generic spawn/message/wait tools. A scoped read-only specialist review completed during setup, showing generic delegation works. Its tool schema does not accept an `agent_type` or project role identifier. Automatic discovery/application of these TOML roles in this Cloud session is therefore **not verified**.

Fallback: the primary reads the selected role file and includes its `developer_instructions` in a scoped generic-worker task, along with the relevant public governance. This is instruction-based delegation, not verified native custom-role loading. If spawning is unavailable, the primary performs the relevant review sequentially and says so. Do not install a second orchestrator, add credentials or weaken permissions to simulate support.

The CLI cap is conservative: two child workers under V1, or two total threads under V2. In Cloud manually keep at most primary plus two workers, prohibit recursive delegation and avoid duplicate investigations. Permissions remain those enforced by the host; role prose does not create isolation.

## Cost and completion

Use a single agent for straightforward changes. Parallelize only independent questions with separate ownership. Reuse context, request concise evidence, stop duplicate work and report unresolved conflicts. Inherit the session model instead of pinning models or reasoning effort in role files. Activate five roles as needed across the workflow, not all at once.

The repository still contains governance rather than migrated application source. No application, Windows, installer or connected-system acceptance is implied. See [validation results](AGENT_VALIDATION.md), [architecture](AGENT_ARCHITECTURE.md) and [workflow](AGENT_WORKFLOW.md).

## Step 2 startup, skills and interrupted work

Use [CODEX_ENVIRONMENT.md](CODEX_ENVIRONMENT.md) and `python3 scripts/verify-development-environment.py` for the source-free engineering workflow. The four [project skills](AGENT_SKILLS.md) supply focused verification, diagnostic, Windows-review and PR-handover references. Actual CLI discovery is recorded separately from manual skill application and automatic Cloud loading.

Recover interrupted work through [AGENT_RECOVERY.md](AGENT_RECOVERY.md): inspect branch/HEAD/status, current worker ownership and pending command evidence first. Retain earlier results only for their exact tested source and platform; re-run affected checks after changes or uncertainty rather than claiming revalidation. When specialists disagree, compare evidence/acceptance criteria, serialize conflicting files and have the primary resolve scope; escalate unresolved security, architecture or release decisions to the maintainer. Do not launch recursive or recurring agents.
