# Security policy

## Scope
This repository is public and currently contains a development governance bootstrap, not an accepted or deployed software release.

## Reporting a vulnerability
Do **not** disclose vulnerabilities, credential exposures or customer-specific findings in public issues, discussions, pull requests or Actions logs.

Use GitHub's private vulnerability reporting feature if enabled for this repository, or contact the repository maintainer through an established private channel. Do not upload sensitive logs or evidence until a suitable secure transfer method is agreed.

Provide a minimal, safely redacted reproduction, the affected revision/component, observed outcome and impact. Do not test against customer networks or devices without permission.

## Development protections
- No credentials, tokens, operational evidence or customer information in source, history or CI artifacts.
- Public pull requests cannot trigger privileged deployment.
- Avoid `pull_request_target` checkout or execution of untrusted code.
- Enforce explicit authorisation for active network diagnostics, operating-system configuration changes and connected acceptance.
- Security issues are triaged privately. Disclosure timing and remediation are assessed case by case.

GitHub public visibility does not imply an open-source licence or permission to access operational systems.
