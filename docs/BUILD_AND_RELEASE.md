# Build, CI and release policy

## Current bootstrap
The repository presently has no application build script, lockfile or test suite. The bootstrap workflow checks governance prerequisites and agent/skill configuration. It is intentionally **not** a simulated application build or release gate.

## Before application CI is enabled
- Validate the migrated source, package manager/runtime versions and lockfile.
- Pin workflow permissions to the minimum needed.
- Separate untrusted public-PR validation from trusted packaging jobs; fork code must not receive secrets.
- Run static analysis and tests on relevant platforms, including Windows for Windows-specific behaviour.
- Avoid publishing installers as artifacts without explicit release review.
- Declare skipped, blocked, synthetic and connected tests accurately.

## Release gate
A release candidate requires recorded source commit and dependency provenance, deterministic build artifacts, unit/integration evidence, Windows installation/update/repair/rollback and state-preservation evidence, security review and approved release authority.

Do not deploy to customer systems, sign a production release or publish private runtime material as part of development CI.

## Engineering framework checks

The feature-branch framework extends bootstrap validation to agent/skill metadata and governance environment checks only. It adds no application-success placeholder, product build, Windows packaging or release job. Use [SOURCE_ACTIVATION_PLAN.md](SOURCE_ACTIVATION_PLAN.md) to activate real checks after source clearance, and [CODEX_CONFIGURATION_REGISTER.md](CODEX_CONFIGURATION_REGISTER.md) for verified versus manual/deferred controls. Existing public-activity metadata handling remains separate and does not check out contributed code.
