# Contributing to Raptora

This public repository accepts issue reports and proposed pull requests for review. Submissions are not automatically accepted or incorporated.

## Proposing a change
1. Check open issues and existing pull requests to avoid duplicate work.
2. Open a clearly scoped issue or a branch-based pull request.
3. Explain expected behaviour, changes, verification performed, and any impact on existing users.
4. Use synthetic data only; never submit operational customer artifacts or access details.
5. Be prepared for security, ownership, licence and compatibility review.

## Outside code
Contributors must have the right to contribute all submitted code. Do not copy proprietary employer, customer or vendor material. Repository maintainers must resolve an appropriate inbound/outbound licence or contributor agreement before accepting outside code.

All outside PRs require manual review and must not receive write credentials, production privileges or unrestricted CI execution. Do not post exploit details in public issues; use the process in [SECURITY.md](SECURITY.md).

## Verification
Current automated checks verify governance prerequisites and agent/skill configuration only. They do not prove application correctness. When source is introduced, follow the documented project-specific test matrix.

## Codex-led work and review

Before implementation, link an approved requirement and acceptance criteria; an opened issue is not itself authorization. Check existing tasks/branches/PRs and coordinate ownership before creating duplicate work. Use the [agent workflow](docs/AGENT_WORKFLOW.md), [focused skills](docs/AGENT_SKILLS.md) and [environment requirements](docs/CODEX_ENVIRONMENT.md). Keep at most three total threads including the primary, and use one for straightforward changes.

Use the issue forms for public-safe bugs/requirements and the existing PR template for review evidence. Confidential security reports follow SECURITY.md; never attach operational logs, source from the private repository or actual evidence. External contributions need independent security/ownership review before acceptance.

Run `python3 scripts/verify-development-environment.py` for current governance/configuration checks. Application build/tests are deferred until cleared source defines real commands; see the [activation plan](docs/SOURCE_ACTIVATION_PLAN.md). Document all outcomes, including Not run, and use [recovery guidance](docs/AGENT_RECOVERY.md) after interruption. Review [manual administration requirements](docs/CODEX_CONFIGURATION_REGISTER.md); documentation does not enable GitHub protection or approve publication.
