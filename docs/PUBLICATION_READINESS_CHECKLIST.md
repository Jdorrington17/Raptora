# Raptora source publication-readiness checklist

Decision: **BLOCKED**. This checklist prepares [issue #12](https://github.com/Jdorrington17/Raptora/issues/12); it grants no publication, source transfer, build distribution, main merge or deployment authority. An unchecked gate is outstanding, not implicitly waived. Named approvers and confidential evidence references remain in protected local custody; publish only approved summaries.

The local report states 392 source files reverified, 271 proposed inclusions, 121 proposed exclusions and 8/8 private-record hashes passing. These are operator-reported counts, not independent Cloud verification, confirmed publication rights or approval of 271 files.

## Gate register

| Gate | Responsible role | Evidence required | Current decision |
| --- | --- | --- | --- |
| Exact source/provenance | Maintainer and local source reviewer | Exact current source/tree identity, approved transformations, file hashes and source-to-destination mapping; reconcile work after the local review | REQUIRES FURTHER REVIEW |
| PKG-DOC-01 | Local build reviewer, security/IP owner, maintainer | Individual disposition and dependency-closure validation under the [packaging plan](MIGRATION_PACKAGING_DEPENDENCIES.md) | BLOCKED |
| PKG-DOC-02 | Same roles, independent decision | Individual disposition and dependency-closure validation | BLOCKED |
| Operational examples | Local reviewer and data/security owner | [Synthetic replacements](MIGRATION_SYNTHETIC_EXAMPLES.md), actual schema/semantic checks and human confidentiality review | REQUIRES FURTHER REVIEW |
| IP/contributor rights | Authorised rights holder and maintainer | Authority to publicly distribute exact included code; approved proprietary/source-available or other licence and inbound rights | BLOCKED |
| Branding/assets | Brand/IP/licensing owner | Per-asset origin, permission, attribution and redistribution terms | BLOCKED |
| Third-party/vendor dependencies | Dependency maintainer and licensing owner | Lockfile-derived transitive inventory, notices/SBOM, advisory dispositions and SDK/module/sample/binary distribution rights | REQUIRES FURTHER REVIEW |
| Security/history | Security and data owners | Findings adjudication, sanitisation, confirmed-exposure remediation and relevant history/metadata review; disclose no confidential findings publicly | REQUIRES FURTHER REVIEW |
| Approved public manifest | Maintainer with rights/security sign-off | Exact allowed public paths and SHA-256 hashes, approved exclusions/deferred functionality and dependency closure | BLOCKED |
| Final source publication | Authorised rights holder and maintainer | Explicit recorded permission for the exact snapshot and migration PR scope before a public branch push or draft PR | BLOCKED |

No named owner approval has been recorded in this Cloud preparation. Technical screening, hash integrity, dependency presence and accepted assessment counts are not approval decisions. A public repository does not by itself grant an open-source licence.

## Publication acceptance

- [ ] Local reviewer reconciles the exact candidate with all later engineering changes and records the immutable identity privately. A prior file list cannot clear changed bytes.
- [ ] Both packaging document dependencies have separate approved dispositions and validated build/package closure; excluded originals cannot reappear through cached/generated output.
- [ ] Required collector/runtime inputs and legacy compatibility tests remain in the approved dependency closure, or approved alternatives have demonstrated parity. Folder age is not an exclusion criterion.
- [ ] Operational examples are replaced/sanitised and privately re-reviewed; fixture outcomes preserve unknown/failure semantics.
- [ ] Code ownership, contributor rights, intended licence, branding/asset permissions, vendor redistribution and mandatory notices are resolved for every included component.
- [ ] Transitive dependencies, frozen lockfile, build-tool versions, download/install hooks, advisory findings and reproducibility are reviewed; no silent dependency upgrade to avoid clearance.
- [ ] Security review covers proposed files, relevant full history and exposed metadata. Confirmed credential findings are handled privately; deletion alone is not remediation.
- [ ] A publishable file manifest identifies exact approved paths/hashes. Confidential exclusion reasons, operational records, private paths/hashes and unapproved provenance metadata stay local.
- [ ] Private provenance and feature maps account for all retained, excluded, incomplete and deferred work. Source-history preservation remains in the legacy reference; no unreviewed private Git history is imported.
- [ ] Rights/security approvers and maintainer explicitly authorise public disclosure of the exact snapshot, approved transformations, notices and provenance summary. Any scope/byte change is re-reviewed.
- [ ] Only then create a dedicated Raptora source-migration branch/PR from current main, retaining destination governance and requiring independent review. A draft public PR is already publication.

## Engineering gates after cleared source exists

These are separate from source-publication permission. They do not justify distributing a release or accepting Windows behavior.

- [ ] Real application type/build/current/legacy/UI/fixture checks run on the destination revision; report commands, counts, failures and skips. Source-free governance CI is not application validation.
- [ ] Source/toolchain/dependency identity, approved source inputs, new build identity and complete package/manifests/ZIP hashes agree. Never regenerate historical manifests to erase provenance gaps.
- [ ] Public PR CI is unprivileged and has no private evidence, signing credentials or persistent-runner access. No application jobs are activated by this documentation PR.
- [ ] Existing single on-demand Windows runner is verified separately. Use maintainer `workflow_dispatch` against an approved exact revision; no untrusted PR/fork execution. Runner/remote-host pairing is not inferred from a document or registered service.
- [ ] Named operator, approved scope and recoverable baseline/checkpoints precede installation or service changes. Preserve the existing acceptance baseline, prior rollback reference and persisted data. Offline/unrun Windows gates stay NOT RUN/BLOCKED.
- [ ] Actual Windows compilation, original-download policy/zone behavior, service/desktop/reboot, clean install/update/repair/uninstall/recovery and executed rollback/data-preservation checks meet approved criteria. Linux mocks and checksums cannot substitute.
- [ ] Issues [#4](https://github.com/Jdorrington17/Raptora/issues/4) and [#5](https://github.com/Jdorrington17/Raptora/issues/5), including outstanding launch-integrity and policy acceptance concerns, are independently verified before closure.
- [ ] Signing/publisher trust, live integration, build distribution, release publication, main merge and production deployment receive their separate required approvals.

## Public-safe completion record

For each gate publish only: gate ID, responsible role, approved/pending/blocked disposition, publishable revision/manifest reference when authorised, verification category and result, limitations and next action. Keep the signature/rights evidence and confidential audit detail locally. Unknown or inaccessible evidence remains unknown.

This task changes documentation only. It has not resolved the two packaging implementations, modified operational examples, approved assets/dependencies, verified a local checkout or migrated source. Closing issue #12 requires its actual acceptance evidence, not merely merging this checklist. See [private audit](PRIVATE_MIGRATION_AUDIT.md), [source activation](SOURCE_ACTIVATION_PLAN.md), [build/release policy](BUILD_AND_RELEASE.md) and [coordination issue #10](https://github.com/Jdorrington17/Raptora/issues/10).
