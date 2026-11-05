# Raptora Windows acceptance and limitations

Document: **PKG-DOC-01**. Status: **DRAFT FOR CONTENT REVIEW — NOT APPROVED AS A PACKAGING INPUT**. Newly authored for [issue #15](https://github.com/Jdorrington17/Raptora/issues/15). This is an intended acceptance procedure, not a record of tests passed. Source publication, package distribution, signing, main merge and production deployment remain separately gated. No version's installed behavior is certified by this guide.

## WA-01: Authorisation and isolation

Obtain an approved test plan identifying the exact reviewed candidate, permitted operations, expected results and responsible operator. A request to build or review documentation does not authorise installation, service control or connected diagnostics. Confirm the target is the existing approved isolated Windows acceptance environment and contains synthetic data only. Do not target deployed applications, customer systems or the development host's working installation.

The operator verifies isolation and target identity privately before work. Do not enable networking, connect Milestone systems, change policy or create additional environments to make a test pass. Use the existing on-demand runner only through approved manual dispatch against reviewed exact code; never run unreviewed public PR or fork code there. If the target is offline, unapproved or unverifiable, record BLOCKED/NOT RUN and stop the affected operation.

## WA-02: Recoverable baseline and backups

Preserve the existing acceptance baseline and prior rollback reference. Before an operation that changes installation or service state, verify a recoverable checkpoint or backup covers the necessary disks, installation identity and persisted application data. Record the approved recovery method and its verified availability privately. Do not overwrite the baseline or use its only copy for destructive testing.

Record the exact prior package and installed identity, supported version/schema compatibility and a before-test inventory of synthetic configuration, diagnostic history, evidence and unknown sentinel files. Compare protected data bytes, logical records and relevant access permissions after each operation. A checkpoint is disaster recovery; restoring it is not evidence that installer-managed rollback works.

## WA-03: Package integrity and publisher trust

Verify the candidate's source/build identity against the approved handover. Independently calculate the supplied archive, installer and manifest hashes and reconcile the complete declared file inventory. Check embedded and companion manifests, archive entries, duplicate/unexpected paths, and missing or mismatched files. A partial extraction, stale output or unverifiable identity is a blocking result. Preserve historical manifests; do not regenerate them to conceal disagreement.

Hashes demonstrate byte consistency, not publisher identity. Check actual Authenticode/signature status and the approved trust policy independently. Treat an unsigned, invalidly signed or untrusted package according to its explicit test-only authorisation; never describe it as an authenticated production release. Record original download/zone metadata and do not strip it to force execution. Build integrity and signing/trust have separate outcomes.

## WA-04: Installation and unavailable outcomes

On the approved clean target, follow the reviewed complete-package procedure in the [package-use guide](PACKAGE_USE_BUILD_AND_RECOVERY.md). Verify elevation and cancellation behavior, expected service identity/account/start mode, protected installation paths, data access permissions, registration, service startup and application launch. Confirm actual versions and health identity refer to the selected installation, then verify the approved reboot/startup behavior. Preserve branding only where its rights and exact content are approved.

Record PASS, FAIL, BLOCKED or NOT RUN for every case with expected and observed results. A process launch or Running service alone does not prove a usable application, successful PowerShell diagnostics or device health. Missing, failed, stale, unsupported or unavailable checks must remain qualified Unknown/Review, unsupported or failed as appropriate; never silently turn them into success. Use synthetic smoke inputs when connected integration is unavailable.

## WA-05: Update and application-data preservation

Use independently identified prior and candidate packages that represent an approved supported upgrade path. Test an in-place update from the preserved representative baseline with the desktop/service initially running and with controlled stopped-state cases. Verify graceful shutdown or a safe actionable refusal, payload/version/registration integrity, correct service recovery and subsequent UI usability. Do not assume uninstall/reinstall is a supported upgrade substitute.

Compare configuration, history, evidence, post-update records, unknown files and permissions against the before-test record. Confirm installation/data roots, service identity and persisted-data semantics remain compatible unless a separately approved migration explicitly changes them. Never delete application data or reset configuration to make update or repair succeed. Unexpected data loss, relocation or corruption stops acceptance and requires preservation of the failed state.

## WA-06: Repair, recovery and executed rollback

Test exact-version repair using a separately reviewed synthetic missing/corrupt managed-file case; verify wrong-version or untrusted repair inputs refuse safely. Check actual restored payload hashes, service state, application usability and data preservation. Include locked packaged resources, failed shutdown and permitted failure-injection cases. Persistent locks must produce bounded actionable refusal or evidenced recovery; do not terminate unrelated processes or disable protection.

Execute installer-managed rollback to the reviewed eligible prior release using its verified transaction/backup provenance. Verify target identity, restored inventory, service/registration state, application launch after reboot and preservation of current synthetic data. A recovery message or intact backup hashes alone do not prove rollback execution. For interrupted operations, follow the exact candidate's approved recovery procedure and preserve journals/backup evidence; do not improvise power cuts, clear pending state or edit transaction records. Missing instructions or unsafe compatibility means BLOCKED.

## WA-07: Uninstall ownership boundaries

Exercise approved uninstall scenarios with desktop/service running and stopped, plus a deliberately held managed file under an authorised test case. Confirm safe shutdown/refusal, bounded lock handling, correct removal of owned files and service/registration state, and a usable recovery outcome on failure. Releasing a test lock and retrying must not require data deletion or unrelated process termination.

Verify configured preservation of application data and retention of unknown/operator-owned files. Never interpret a directory name as authority to delete its entire contents. Reinstall only under an approved case and confirm retained configuration/history/evidence remain usable. Uninstall success is not established solely by the desktop disappearing or a progress bar completing.

## WA-08: Policy, signatures and diagnostic limitations

Record effective PowerShell policy and all scopes before and after relevant operations. Verify precedence and clear scope-specific refusal when organisational or explicit local restrictions block execution. An approved child-only default-policy mechanism must not become a persistent machine/user policy change or a bypass of Group Policy, WDAC/AppLocker, file trust, signing or other enforced controls. Inspect original delivery-path zone behavior; do not weaken controls to claim compatibility.

Test actual installer support scripts, finish checks, dashboard-triggered diagnostics and their permitted subprocess chain. A service starting does not prove those scripts execute. Blocked policy, signature/integrity failure or unavailable vendor capability must produce an honest unavailable outcome. Live Milestone collection and vendor-specific capabilities need their own explicit connected-acceptance authorisation and evidence; this guide grants none.

## WA-09: Evidence limits and release decision

For each test retain exact candidate/prior identity, approved target and operation, commands, timestamps, expected/actual outcome, relevant hashes, data-preservation result and limitations in protected local evidence. Return only sanitised summaries to the tracked issue/PR. Never upload customer material, private paths, full logs, original captures or uncleared builds to public GitHub artifacts.

Keep unit/synthetic checks, packaging integrity, actual Windows lifecycle, signing/trust and connected acceptance distinct. No check marked BLOCKED, skipped or NOT RUN is a PASS. Maintainer, Windows/QA, build-engineering and security/IP content reviews are required before this draft is adopted, and separate release authority is required after actual acceptance. Installer issues remain open until their criteria are verified; neither this guide nor a successful build authorises release or production deployment.
