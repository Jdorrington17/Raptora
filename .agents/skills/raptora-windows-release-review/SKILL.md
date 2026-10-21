---
name: raptora-windows-release-review
description: Use when reviewing Windows services, PowerShell compatibility, installer packaging, update, repair, rollback, or Raptora release readiness.
---
# Review Windows release evidence

Review source/manifests and permissions without executing installers or touching an installed environment. A review request does not authorize platform changes, signing, packaging publication or deployment.

Return a matrix with **gate, exact candidate/source identity, available evidence, required target evidence, outcome and approval owner**:

- Build/toolchain and frozen dependency provenance; PowerShell 5.1 parsing and mocks.
- Complete desktop/setup payload and transferred manifest/hash integrity; publisher authenticity is separate from checksums.
- Fresh install/configure/validate/operate: UAC, identity/ACLs, paths, service/API/desktop and offline operation.
- Update from each supported exact prior package; preserve configuration, history, evidence, unknown files and installation identity.
- Exact-version repair, known-good rollback, locked executables, ordinary failure and interrupted/reboot recovery; verify real restored behavior and state, not only backup hashes.
- Signing/trust, dependency licences/security, release approval and separately authorized connected acceptance.

Use Pass/Fail/Skipped/Blocked/Not run. Linux mocks cannot accept Windows behavior. Actual journeys require an approved disposable Windows target, synthetic data, external backup and verified previous packages. Never delete ProgramData, reset configuration or change policy to force a pass.

Use docs/SOURCE_ACTIVATION_PLAN.md. No cleared source means a review plan, not a package build or release certificate.
