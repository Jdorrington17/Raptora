# Project status

**Snapshot:** 2026-10-21. This document is a point-in-time preparation status, not a production release certificate.

| Area | State |
| --- | --- |
| New repository | Public; initial README created |
| Repository governance | Bootstrap present on main; specialist framework and hardening changes remain feature-branch work pending independent review |
| Existing application migration | Not started |
| Legacy source and open-PR reconciliation | Future private audit; do not begin Step 3 until Step 2 is completed and reviewed |
| Public-source permission/security audit | Required before migration |
| Code build, unit tests, Windows CI | Not configured in this bootstrap |
| Installer, repair and rollback acceptance | Not tested by this bootstrap |
| Production deployment | Not authorised |

Existing separately managed Windows development builds are not validated by these documentation changes. Application acceptance requires independent evidence for build, functional, platform, integration and release checks.

## Immediate next decisions
1. Confirm authority to publish the intended application source and acceptable public scope.
2. Conduct a confidential audit of legacy source, history and outstanding changes.
3. Review the agent framework/hardening branch and verify the manual settings in CODEX_CONFIGURATION_REGISTER.md.
4. Define application-specific CI against actual source after migration clearance.

The engineering configuration register and validation record distinguish local checks, CLI skill discovery, manual Cloud fallback, hosted CI and unverified administrative settings. No product workflow is activated by Step 2.
