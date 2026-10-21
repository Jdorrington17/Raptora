# Project status

**Snapshot:** 2026-10-21. This document is a point-in-time preparation status, not a production release certificate.

| Area | State |
| --- | --- |
| New repository | Public; initial README created |
| Repository governance | Proposed in the bootstrap branch and awaiting review |
| Existing application migration | Not started |
| Legacy source and open-PR reconciliation | Required before migration |
| Public-source permission/security audit | Required before migration |
| Code build, unit tests, Windows CI | Not configured in this bootstrap |
| Installer, repair and rollback acceptance | Not tested by this bootstrap |
| Production deployment | Not authorised |

Existing separately managed Windows development builds are not validated by these documentation changes. Application acceptance requires independent evidence for build, functional, platform, integration and release checks.

## Immediate next decisions
1. Confirm authority to publish the intended application source and acceptable public scope.
2. Conduct a confidential audit of legacy source, history and outstanding changes.
3. Review the governance PR and decide whether to adopt the initial monitoring workflow.
4. Define application-specific CI against actual source after migration clearance.
