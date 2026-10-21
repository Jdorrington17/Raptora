# Integration and migration safeguards

1. Treat the legacy repository as a read-only reference; do not assume its default branch is the current integrated candidate.
2. Compare exact branch SHAs and stacked pull-request parentage before selecting a migration baseline.
3. Perform an authorised private audit of source **and history** for ownership, credentials, customer material, confidential topology and third-party distribution rights.
4. Do not copy raw runtime configurations, recordings, evidence images, logs, unrestricted network inventories or proprietary third-party bundles.
5. Preserve installer compatibility, known-good source lineage, operational state and rollback protection when code is eventually cleared.
6. Keep synthetic test validation separate from authorised connected field and Windows acceptance.
7. Do not mutate external devices, Windows services, customer data or production systems during source migration.
8. Complete a reviewable pull request and explicit go/no-go approval before publishing cleared application code.

Once source is available, extend this guide with verified component interfaces, data-migration rules and acceptance checks. Do not speculate about an uninspected installed application.
