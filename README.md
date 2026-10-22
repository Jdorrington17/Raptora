# Raptora

Raptora is a security-system diagnostics and reporting application under active development.

**Status:** Public repository governance bootstrap. Application source has not yet been migrated or validated in this repository. This repository is **not** a production release, installation package, or a source of customer operational data.

## Development model
- Changes are proposed on branches and reviewed using pull requests.
- External contributions are reviewed before acceptance; opening a PR does not confer deployment or merge authority.
- CI currently checks repository governance only. It does **not** compile, test, install, or certify the application.
- Code migration is on hold until the legacy source has been reviewed for intellectual-property, licence, credential and customer-data exposure.

## Documentation
- [Contribution process](CONTRIBUTING.md)
- [Security disclosures](SECURITY.md)
- [Engineering agent instructions](AGENTS.md)
- [Project status](docs/PROJECT_STATUS.md)
- [Architecture and boundaries](docs/ARCHITECTURE.md)
- [Build and release policy](docs/BUILD_AND_RELEASE.md)
- [Integration safeguards](docs/INTEGRATION_SAFEGUARDS.md)
- [Roadmap](docs/ROADMAP.md)
- [Public activity monitoring](docs/EXTERNAL_ACTIVITY.md)

## Rights and safety
No software licence is granted by the presence of source code in this public repository. Copyright and contribution-licensing decisions must be documented before outside code is integrated.

Do not submit credentials, customer data, recordings, evidence images, access details or confidential architecture diagrams.


## Codex engineering setup

Start with [AGENTS.md](AGENTS.md), then read the [Codex context and issue-intake brief](CODEX_CONTEXT.md) and reconcile the live GitHub issue tracker. Off-Codex observations must be sanitised and tracked as issues; chat history is not an implementation backlog.

The current tree provides governance and agent/skill infrastructure, not migrated application source. See the [configuration register](docs/CODEX_CONFIGURATION_REGISTER.md), [environment startup](docs/CODEX_ENVIRONMENT.md), [agent/skill usage](docs/AGENT_USAGE.md) and [validation results](docs/AGENT_VALIDATION.md). Application and Windows release checks remain source-gated; no installed behavior is certified by these files.
