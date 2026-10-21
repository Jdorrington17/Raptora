# Focused engineering skills

Project skills live in `.agents/skills/<name>/SKILL.md`, the repository discovery path verified in official Codex 0.163.0 source. They are concise references, not extra agents, permission grants or recurring automation. Load only the relevant skill body.

| Skill | Invoke when | Output |
| --- | --- | --- |
| `raptora-verify-code` | Verifying changes or CI conclusions | Affected modules and target-qualified command/result/limit record |
| `raptora-diagnostic-development` | Reviewing diagnostic evidence, correlation or lifecycle rules | Evidence-qualified design and synthetic counterexample matrix |
| `raptora-windows-release-review` | Reviewing services, packaging or installer maintenance | Provenance and actual Windows acceptance/approval matrix |
| `raptora-pr-handover` | Preparing a draft PR or resuming before submission | Focused change/test/risk/approval handover with truthful publication status |

In a supporting client, name the skill explicitly, for example: “Use $raptora-verify-code to verify this branch.” Confirm discovery before relying on native invocation. If Cloud does not list these project skills, read the specific SKILL.md and follow it manually; report manual application rather than automatic discovery. The installed CLI can list skill metadata through app-server `skills/list`; listing proves discovery, not execution or policy enforcement.

Four reference scenarios were checked before authoring and dry-run against the written skills: source-free green governance CI, conflicting recorder-qualified evidence, Linux installer mocks with a release request, and interrupted PR handover with API denial. Baseline behavior was already safe. These checks show reference usability; they do not establish a measured behavior improvement, automatic Cloud loading or product acceptance. The verification skill was clarified to match CI evidence to its exact tested SHA.

Run `python3 scripts/verify-development-environment.py` to validate role/skill structure and negative configuration cases. This deliberately restricted stdlib validator accepts this project's simple frontmatter subset; it is not a general YAML validator or an upstream Codex schema replacement. See [configuration register](CODEX_CONFIGURATION_REGISTER.md) and [agent usage](AGENT_USAGE.md).
