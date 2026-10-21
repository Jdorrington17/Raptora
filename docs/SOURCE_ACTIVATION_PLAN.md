# Source-gated engineering activation plan

**Status: designed, not activated.** Raptora currently has governance/agent infrastructure rather than the cleared application implementation. No placeholder application workflow, dependency manifest or successful-product badge is supplied. Follow [build and release policy](BUILD_AND_RELEASE.md), [private audit](PRIVATE_MIGRATION_AUDIT.md) and the [configuration register](CODEX_CONFIGURATION_REGISTER.md).

## Activation prerequisites

The primary must obtain an approved source-publication/migration scope, exact source and feature reconciliation, ownership/licence clearance, synthetic fixtures, dependency lockfiles and an approved module/parity map. Inspect the cleared repository's own scripts and pins before selecting commands; do not copy historical commands or invent passing checks. Map each required check to real source and an acceptance owner.

Record supported Windows editions/versions and architectures, PowerShell/runtime/compiler versions, collection versus service identities, installation/data paths and persisted-data compatibility. Establish an isolated Windows test target, external backups, exact previous packages and rollback plan before lifecycle execution. These prerequisites do not authorize modifying an installed or connected environment.

## Staged implementation

| Area | Activate only after | Required implementation and evidence |
| --- | --- | --- |
| Node.js and pnpm | Actual manifests, lockfile and supported pins are cleared | Pin approved versions, use frozen-lockfile installation and verified downloads, record runtime/package-manager identities and caches; no customer credentials or verification bypasses |
| TypeScript and React | Cleared modules and actual build scripts exist | Execute genuine typecheck and production frontend/backend builds; retain source SHA, command, exit status and output identity; a syntax or presence check is insufficient |
| Unit, integration and regression tests | Real tests, contracts and fixture provenance are inspected | Run relevant positive/negative/failure-path suites, verify executed counts and fresh results, preserve failures/skips; isolate temporary state and untrusted dependencies |
| Windows PowerShell | Supported policy/modules and Windows runner are approved | Parse and test actual scripts under required PowerShell versions, verify encoding and worker boundaries; separate mocks from platform execution and connected SDK behavior |
| Installer packaging | Clean Windows build and payload assembly are verified | Build complete packages, verify every payload hash and archive/manifest identity, retain notices/SBOM and source/toolchain provenance; directory and single-file formats need separate acceptance |
| Update, repair and rollback | Exact prior and candidate packages, target and backups are approved | Execute state-preserving lifecycle cases, wrong-version/tamper rejection, running-process locks, interrupted recovery, service/API/desktop restart and rollback compatibility; preserve ProgramData/configuration/history/evidence/unknown files |
| Dependency/source security | Cleared source and full dependency inventory are available | Inspect transitive licences/advisories, secrets/history, public fixtures/assets and provenance; triage findings privately and verify required remediation before publication/release |
| Automated PR quality gates | Real commands and stable check identities are established | Require relevant type/build/test/security outcomes with fail-closed aggregation; missing, failed or unexpectedly skipped required jobs block acceptance; governance-only changes retain proportionate checks |
| Versioning and release | Maintainer-approved version/schema/support policy exists | Define version/build IDs, changelog, immutable source tags, compatibility rules, package signatures/trust, durable manifests and release approvals; no release from an unverified branch or generic identity |

## Trust and execution identities

Public-PR validation runs unprivileged with read-only permissions, no production/signing credentials and no access to private source or customer inputs. Do not check out or execute contributed code in privileged `pull_request_target` jobs. Treat dependency install hooks and submitted workflows as untrusted code. Required fork approvals and trusted-runner policy must be administered explicitly.

Trusted packaging uses reviewed source and a separate approved Windows execution identity. Signing/publishing credentials belong only to separately gated trusted release jobs; never expose them to forks or promote an untrusted PR artifact as a release. GitHub environment protection, required reviewers, minimal token permissions, artifact retention and branch/ruleset enforcement require maintainer administration and verification.

Runtime credentials, collection identities and live SDK/site acceptance are independent of build identities. On-demand technician collection does not prove unattended operation. LAN exposure, service configuration, connected tests, signing and deployment remain separately authorized actions.

## Evidence and release decision

For every check retain the exact source/tested SHA, tools/OS/identity, actual command, outcome, counts where applicable, artifact hashes and limitations. Label Pass, Fail, Skipped, Blocked or Not run, and distinguish unit/synthetic, Windows platform and actual connected acceptance. Linux success does not validate Windows installers or services; a package hash does not authenticate its publisher.

A release review covers fresh install/configure/validate/operate/update/repair/rollback, failure recovery, reboot, persisted schemas, offline operation, backend authorization and storage limits. Unresolved required checks remain blockers. The primary consolidates evidence for maintainer approval and does not self-merge, sign, publish or deploy as a side effect of source activation.

## Automated Windows versus isolated-target evidence

GitHub-hosted Windows runners can perform actual builds, PowerShell parsing, mocked contracts, synthetic transaction tests and payload-integrity checks once real source/jobs exist. They do not establish installed customer identity or connected Milestone behavior. An approved disposable physical machine or VM must cover UAC/session launch, SCM/ACLs, process locks, startup/reboot, actual install/update/repair/rollback and interrupted/power-loss recovery with ProgramData/configuration preservation. Connected SDK/site acceptance needs a separate scoped approval; no such tests are part of Step 2.
