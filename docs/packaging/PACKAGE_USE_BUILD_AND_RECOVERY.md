# Raptora package use, build, maintenance and recovery

Document: **PKG-DOC-02**. Status: **DRAFT FOR CONTENT REVIEW — NOT APPROVED AS A PACKAGING INPUT**. Newly authored for [issue #15](https://github.com/Jdorrington17/Raptora/issues/15). These are intended operating requirements, not verified commands or a release certificate. Package-specific implementation, supported versions, identities and recovery controls must be confirmed from the reviewed candidate; none is invented here.

## PU-01: Reviewed prerequisites and build identity

Use only an authorised source snapshot or complete candidate with recorded source commit, build identity, dependency lockfile/toolchain and approved provenance. Confirm the candidate's supported Windows edition/architecture, runtime/compiler, PowerShell, vendor prerequisites, available disk space and operator rights against its reviewed requirements. Unknown or missing prerequisites are blockers; do not download arbitrary binaries or change dependencies to force success.

Trusted build work uses a clean reviewed revision, pinned approved tools and frozen dependencies with source/asset clearance. Keep public PR validation unprivileged. Windows builds or acceptance on the existing on-demand runner require approved exact revisions and manual scheduling; do not dispatch unreviewed PR code. This draft supplies no runnable build/install commands because the public repository's application source/build contract is not yet cleared. Building does not authorise distributing the result.

## PU-02: Complete-package verification and launch

Obtain the entire approved package and its required companion identity/integrity documents through the approved delivery path. Verify archive/installer/manifest hashes, complete inventory, documentation and actual signing status before launch. Preserve original download/zone metadata. Extract or stage the complete layout as specified by the reviewed candidate; do not rename or launch an isolated executable while leaving required support files behind.

Use only the candidate's documented entrypoint and approved operation. If the entrypoint, layout or identity is unknown, stop and request a reviewed package-specific handover instead of guessing paths or flags. Reject missing, unreadable, empty or incomplete required guidance before treating a package as complete. Check that outer and embedded guidance copies match the approved revisions; a cached older document is not an acceptable replacement.

## PU-03: Elevation and identity boundaries

Verify the initiating technician, expected elevated helper, service account and application launch identity against the approved plan. Confirm any elevation prompt belongs to the reviewed candidate and requested operation. Cancellation or insufficient permissions must stop safely with an actionable result; a missing result must not be assumed successful. Do not start the application under a different privileged identity simply to conceal a permissions defect.

Run ordinary use and diagnostics with the intended least privilege. Installation/service changes require explicit operator scope and a recoverable baseline. No remote access, production change, credential collection or unsolicited device/network probe is authorised by this guide. Keep identity evidence private and publish only cleared role-level summaries.

## PU-04: Application and data separation

Preserve registered installation and data roots, service identity and persisted configuration/history/evidence contracts. Application binaries and controlled workers belong to the protected application area; configuration and operational records belong to the existing data area. Use the candidate's registered identity rather than guessed locations. An approved schema/path migration must specify compatibility and recovery separately.

Take approved external backups and record synthetic data inventories/hashes before maintenance. Retain unknown/operator-owned files and current data across supported operations. Never delete the data area, reset user configuration, copy private evidence into source or use a source checkout as a substitute for an installed application's data store.

## PU-05: Supported, unavailable and unverified capabilities

Read the reviewed candidate's capability and acceptance record. A menu option, supported manifest entry or completed installer step is not proof of functional, service or vendor integration acceptance. Unsupported features must be labelled unavailable; missing/stale evidence or a failed diagnostic must not become a healthy result. Keep condition, severity, confidence, applicability and issue state separate in interpretation.

Use approved synthetic inputs for offline smoke testing. Live Milestone/device collection requires separately authorised connectivity and reviewed capability requirements. Do not infer playback, retention, camera availability or storage health from the service running or a successful package hash check. Report untested paths explicitly and preserve their limitations in the handover.

## PU-06: Update, repair and uninstall maintenance

Select a supported operation for the exact installed/candidate identities. Verify registered roots, prior package availability, backups and permitted scope. Use a complete reviewed external package when required; do not repair with another version or edit ownership manifests to make it fit. Verify the resulting payload, registration/service, application and persisted data rather than relying on a completion message.

For running applications, services or locked files, use the reviewed graceful-shutdown/preflight flow and bounded safe refusal. Do not kill unrelated processes, disable protection or delete arbitrary files. Repair should restore only authorised managed content. Uninstall should remove only owned components and follow the approved data-retention choice while protecting unknown files; neither repair nor upgrade routinely clears configuration/data. Acceptance cases are defined in the accompanying *Raptora Windows acceptance and limitations* guide, using the approved package inventory to locate its delivered copy. Do not assume the packaged guide retains its source filename.

## PU-07: Rollback provenance and compatibility

Before rollback, identify the exact eligible prior release and matching installer-managed transaction/backup records. Verify integrity, version/data-schema compatibility, supported downgrade policy and current installation identity. Retain original prior packages and protected provenance; a generic build label or unrelated backup is insufficient.

Use the reviewed rollback mechanism only after operation-specific approval. Verify actual restored version/files, service/registration, UI/reboot behavior and preservation of data written since update. A VM checkpoint, transaction log saying restored or matching backup hashes is not proof of executed installer rollback. If the target is unverified, missing or incompatible, stop and record BLOCKED rather than resetting data to permit downgrade.

## PU-08: Interrupted operation and recovery

Stop repeated maintenance attempts when an incomplete transaction, conflicting lock or uncertain installed state is detected. Preserve the exact failed candidate/transaction identity, journals, verified backups and logs privately. Confirm the original installer process is no longer active using the approved recovery method. Do not delete lock files, pending state, journals or backups just to unblock a wizard, and do not rewrite historical manifests.

Follow the exact reviewed candidate's recovery instructions with explicit operator approval and a verified recovery baseline. This generic guide cannot supply transaction commands or paths for an unreviewed implementation. If recovery instructions or trustworthy state are unavailable, stop and escalate to the maintainer. After recovery, independently verify payload, service/application behavior and data; report partial or unverified recovery honestly. Destructive interruption testing needs a separately reviewed test plan.

## PU-09: Logs and diagnostic evidence

Retain necessary operation/diagnostic logs, immutable source/build identity, timestamps, scope/policy observations, exit outcomes and integrity/data comparisons in approved protected local storage. Apply the approved access and retention policy; do not assume that a log created successfully has suitable Windows permissions. Avoid credential values and unnecessary customer data in diagnostics.

Use outcome-specific guidance to locate evidence from the reviewed candidate; no private machine path or raw log is needed in public issues. Report only sanitised expected-versus-actual behavior, exact public revision when cleared, counts and limitations. Failed logging or missing evidence can leave an outcome unverified; it cannot be replaced with an invented PASS. Confidential evidence custody remains independent of the public GitHub workflow.

## PU-10: PowerShell policy, signing and final limits

PowerShell policy follows scope precedence: MachinePolicy, UserPolicy, Process, CurrentUser, LocalMachine, then the platform default. Record actual scope/effective observations and identify a blocking scope/value. A process-scoped mechanism cannot override Group Policy and must not weaken explicit restrictions, WDAC/AppLocker, signing requirements or file-zone trust. Do not make routine persistent policy changes or remove zone metadata to force an unsigned script to run.

Checksums and internally consistent manifests establish integrity, not publisher authenticity or legal distribution rights. Verify signatures/trust independently and keep unsigned candidates within their expressly approved test scope. Actual installer/diagnostic policy behavior remains unverified until the precise delivery and execution paths pass authorised Windows tests. Maintainer, build-engineering, Windows/QA and security/IP review must approve exact guide revisions before packaging adoption; release distribution, source publication and deployment require their separate approvals.
