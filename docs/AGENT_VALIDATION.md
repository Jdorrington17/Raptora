# Agent configuration validation

Validation date: 21 October 2026. This record concerns engineering configuration only; no application source was migrated and no installed application was changed.

## Evidence

| Check | Result | Limit |
| --- | --- | --- |
| Installed CLI version | `codex-cli 0.163.0` | Does not identify the Cloud host backend/version |
| Official version-matched schema | Project config and all five role configuration layers passed JSON Schema validation | Role `name`/`description` metadata validated separately against the official role loader; not root config keys |
| CLI strict parser smoke check | Isolated `codex app-server --strict-config --listen stdio://` initialization and `config/read` accepted enabled agents, concurrency 2 and depth 1 | Temporary user-layer copy of project settings; no credentials/model turn, project-trust bypass or native role invocation |
| Repository validator | `python3 scripts/validate-agent-config.py` passes | Deliberately restricted local policy/TOML check, not full upstream schema validation |
| Negative configuration cases | Nine cases rejected in disposable copies: unknown permission field, increased concurrency, missing role, mismatched name, nested role, missing guide and three invalid setting types | Independent review found the initial Python equality type-confusion defect; exact boolean/integer checks corrected it and the three cases passed on rerun |
| Cloud delegation | One scoped read-only governance review completed and returned findings | Generic host-provided worker, not native TOML role recognition |
| Cloud custom roles / automatic reload | Not verified | Exposed spawn tool has no custom-role selector; use documented instruction-based fallback |
| Effective review-only sandbox | Not configured or claimed | Role instructions inherit parent permissions; managed controls remain authoritative |
| GitHub protection, PR/check state | Unverified: API requests returned Forbidden | No protection settings were changed or assumed disabled |
| Windows/application/installer/connected acceptance | Not run; outside scope | No product implementation or production tests |

The strict parser initially returned additional null default fields beyond the requested settings. The smoke assertion was corrected to compare the three requested fields; the rerun passed. No production configuration change was needed.

## Reproduce the repository check

Use Python 3.11+ from the checkout root:

```sh
python3 scripts/validate-agent-config.py
```

The check rejects unknown project/role fields, changed concurrency policy, missing/duplicate/nested role files, mismatched names, empty instructions and missing guidance. Existing bootstrap CI now runs it in its unprivileged job with `contents: read` and checkout credentials disabled. This is agent/governance validation, not product CI. A future upstream schema or policy update requires an intentional review of this restricted validator.

Native custom-role invocation still needs a trusted, supported CLI session test. Verify which role was loaded and returned evidence; do not mark all five roles exercised after one generic worker succeeds. Cloud configuration files alone do not establish runtime enforcement of the concurrency setting.

## Official references

The documentation website returned HTTP 403 from this environment. The official OpenAI Codex Git repository was accessible through the existing Git proxy, so validation used its version-matched schema/loader and current source rather than an unverified tutorial:

- [Codex multi-agent documentation](https://developers.openai.com/codex/multi-agent/)
- [Codex configuration reference](https://developers.openai.com/codex/config-reference/)
- [0.163.0 configuration schema](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/core/config.schema.json)
- [0.163.0 role-file parser](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/agent-roles/src/agent_role_config.rs)
- [0.163.0 role discovery](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/agent-roles/src/loader.rs)
- [0.163.0 concurrency accounting](https://github.com/openai/codex/blob/rust-v0.163.0/codex-rs/core/src/config/mod.rs)

Release tag `rust-v0.163.0` resolves to `83086188ae0614bd882818ff1aa23f3194962012`. Current official source was also inspected at `c7234c1174b27d9c55199fba0d546dc27d1b0415`; the configured fields and role parser agreed with the installed-release reference. No upstream code was copied into this repository.

## Step 2 hardening evidence

- Same five role files and project settings preserved; the version-matched schema still validates them. Project instructions were read by the primary and scoped reviewers; automatic instruction loading in a fresh Cloud client remains unverified.
- CLI 0.163.0 strict app-server initialization/config-read smoke passed in an isolated user-layer copy. `python3 scripts/check-codex-runtime.py` passed. Installed CLI `skills/list` discovered all four project skills at their repository paths as enabled, with zero project skill errors. No model turn, login, trust bypass or custom-role invocation was performed by that smoke test.
- Four reference scenarios were dry-run via generic delegated workers using explicit skill instructions. All produced the expected evidence/approval boundaries. Existing baseline answers were already safe; no measured behavioral improvement or automatic Cloud invocation is claimed.
- `python3 scripts/verify-development-environment.py` passed, including eight engineering-configuration regression tests (three invalid-type subcases). Four skill rejection tests first failed against the older role-only validator, then passed with skill validation implemented. These are governance tests, not application unit tests.
- Current tools observed: Git 2.52.0, Python 3.12.14, Node 24.19.0, Codex CLI 0.163.0. pnpm/Corepack command paths exist but pnpm activation/version was not run; Windows PowerShell and dotnet were not found on PATH. Node/pnpm are unnecessary for the source-free check and no caches or dependencies were added.
- Current branch protection, scanning settings, hosted checks and PR status remain unverified because GitHub API reads returned Forbidden. No administration was changed. Existing workflow permissions and metadata-only public-activity handling were preserved.

See the [configuration register](CODEX_CONFIGURATION_REGISTER.md) for manual/deferred settings, [source activation plan](SOURCE_ACTIVATION_PLAN.md) for future Windows/application checks, and [private audit procedure](PRIVATE_MIGRATION_AUDIT.md) for the separately approved Step 3. No private legacy content was inspected or migrated during Step 2.

Independent Step 2 review found and corrected an invalid plain-YAML description accepted by the restricted validator, plus locale-dependent test-file reads/writes. A failing colon-in-description regression now passes; tests use explicit UTF-8. Actual Windows execution remains Not run. The review also aligned older bootstrap wording with governance/configuration scope.
