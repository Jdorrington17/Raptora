# Architecture and trust boundaries

**Current repository state:** No application implementation has been imported. The following are intended design principles, not proof of an implemented or deployed architecture.

## Product principles
- A local-first technician application that remains usable without an external AI service.
- Read-only monitoring and diagnostic collection by default.
- Isolated adapters for security-system integrations, with explicit permissions for privileged actions.
- Clearly qualified evidence and device identity across collection, processing, investigation and reporting.
- Persistent application state with controlled backup, upgrade and rollback boundaries.
- Role- and site-aware access decisions enforced at the service/backend, not only in the UI.

## Documentation discipline
Actual modules, dependencies, services, data contracts, packaging and startup commands must be documented from inspected, cleared source during migration.

Do not publish private site topology, customer identifiers, operational paths/addresses, device credentials, diagrams or inventory exports.
