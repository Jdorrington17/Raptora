# Agent architecture

This is an engineering framework, not a Raptora application component. The installed product must remain independent of Codex, ChatGPT and external AI. This change adds no application code, telemetry, services or private-source import.

## Roles and ownership

| Role name / file in `.codex/agents/` | Primary output | Boundaries |
| --- | --- | --- |
| `architect` / `architect.toml` | Architecture, dependency and contract assessment; scoped design recommendation | Analysis/review first; major structural or technology changes require approval |
| `developer` / `developer.toml` | Focused implementation, tests and documentation tied to acceptance criteria | Approved requirement and branch only; no self-approval |
| `security-reviewer` / `security-reviewer.toml` | Sanitized security, ownership and public-exposure assessment | Detailed findings stay in an approved private location outside the public repository; no unapproved active probes |
| `qa-engineer` / `qa-engineer.toml` | Acceptance matrix, regression results and coverage gaps | Separate implementation/test ownership; never turn synthetic results into operational claims |
| `windows-deployment` / `windows-deployment.toml` | Lifecycle compatibility, provenance and Windows acceptance requirements | Analysis only during setup; no installer execution, service changes or deployment |

The primary agent owns triage, task boundaries, delegation, conflict resolution, integration and final verification. Specialists advise or implement scoped tasks; they cannot grant approvals, delegate recursively or independently widen scope. Every specialist inherits the parent model and actual runtime permissions; no model, sandbox, network, approval-policy or credential override is configured.

## Concurrency and isolation

Use at most three active threads including the primary, and one agent for straightforward work. Assign at most two independent specialist tasks at a time. Do not let workers edit the same files; serialize dependent work and integration. Reuse an existing specialist when its context is useful; end or reuse idle work before creating more. Pause and report unexpected edits rather than reverting someone else's work.

CLI 0.163.0 gives `agents.max_concurrent_threads_per_session` different accounting between backends: V1 limits spawned children; V2 includes the primary. The configured value **2** conservatively permits primary plus two children in V1 or two total in V2. `max_depth = 1` constrains V1; V2 ignores it, so instructions also forbid recursive delegation. No experimental backend is forced. Cloud may ignore these project settings; the primary must enforce the three-total budget itself.

Agents are not security principals or separate workspaces. A review-only instruction is not a read-only sandbox. Parent/managed permissions, actual tool access and trusted-project policy determine capabilities independently. Use the existing isolated Cloud checkout; do not create a worktree unless explicitly requested. Do not copy private source into public prompts, PRs or worker artifacts.

## Supported configuration

Each file declares `name`, `description` and `developer_instructions`, supported by the official 0.163.0 role-file loader. That release discovers TOML files under a loaded configuration layer's `agents/` directory. Project settings live in `.codex/config.toml`; no duplicate role registration or legacy `max_threads` key is used. Role metadata is distinct from the main configuration schema.

See [usage](AGENT_USAGE.md) for invocation and [validation](AGENT_VALIDATION.md) for evidence and limitations. Project configuration must be loaded by a supporting, trusted client; storing files does not establish that an existing Cloud session reloaded them.
