# Required-section contract and Local Codex handover

Status: **DRAFT FOR REVIEW**. Implements the drafting deliverable of [issue #15](https://github.com/Jdorrington17/Raptora/issues/15), using [PR #13 at 654f671](https://github.com/Jdorrington17/Raptora/pull/13) as the planning reference and the maintainer's sanitised contract in [issue #12](https://github.com/Jdorrington17/Raptora/issues/12). Actual private integration/validation belongs to [issue #16](https://github.com/Jdorrington17/Raptora/issues/16). No confidential original, private path, source extract or historical test claim was used as substitute content.

## Draft traceability matrix

| Dependency | New document | Intended generic packaging destination role | Required sections | Current disposition |
| --- | --- | --- | --- | --- |
| PKG-DOC-01 | [Windows acceptance and limitations](WINDOWS_ACCEPTANCE_AND_LIMITATIONS.md) | Distributed Windows acceptance/limitations guidance accompanying the candidate | WA-01 through WA-09 | Newly authored draft; content review and packaging validation pending |
| PKG-DOC-02 | [Package use, build, maintenance and recovery](PACKAGE_USE_BUILD_AND_RECOVERY.md) | Distributed package-use/build/maintenance/recovery guidance accompanying the candidate | PU-01 through PU-10 | Newly authored draft; content review and packaging validation pending |

Both roles remain required. Do not remove a document or reclassify the confidential original as public. The local build reviewer must confirm the existing destination roles, consumer/link requirements, supported variants and any embedded/outer copies privately. Actual filenames, private consumers and implementation paths are intentionally absent from this matrix. These unresolved mappings prevent adoption, not drafting.

## Structured content contract

[`required-sections.json`](required-sections.json) is the proposed version-1 contract. Its file paths refer only to these public drafts, not private originals or future package destinations. Each mandatory section has a stable ID, exact heading and human-reviewed required topics. Contract changes require review with the guide revisions; silently weakening the contract to accept incomplete content is prohibited.

The local validator must implement the following behavior before treating a candidate package as complete:

1. Bind the exact guide/contract revision and hashes to recorded maintainer, build-engineering, Windows/QA and security/IP decisions. Both `draft-for-review` and `packagingAdoptionApproved: false` mean this contract is **not adopted**, regardless of structural success. Use an explicitly approved adoption record for exact hashes; a changed status field alone is not authorisation. Do not reuse approvals after bytes change.
2. Read both files and the reviewed contract. Missing, inaccessible, invalid-encoding, empty or whitespace-only input is a failure. Unexpected schema/version, malformed contract, duplicate IDs or absent contract entries must fail closed. Do not fall back to excluded originals, bundled stale guidance or a default green result.
3. Decode UTF-8 with optional BOM and normalise line endings for parsing only. Retain original bytes for hashes. Require one matching top-level title and exactly one occurrence of each required `## ID: heading`, in contract order. IDs/headings must match case and punctuation. Duplicate required IDs, even with different heading text, are failures.
4. Ignore fenced-code content and HTML comments when detecting headings and prose. A required heading shown only as an example or in a comment does not satisfy the contract. Parse section boundaries at the next level-one/two heading. Require substantive body content for each mandatory section; empty, comment-only or placeholder-only text fails. Do not count a nested heading, separator, image/link-only line or empty checklist as substantive guidance.
5. Check relative links against the reviewed input document set and again against every approved delivery layout. A renamed/copied document can break a link despite a passing source check. Check external reference intent during human review; remote availability does not establish confidential-data clearance.
6. Require human review of every `requiredTopics` entry for accuracy, safety and complete intended meaning. Structural checks and keyword matches cannot prove semantic completeness, operational correctness, confidentiality, rights or Windows acceptance. Preserve draft/untested limitations; reject false successful-acceptance or signing claims.
7. On any read/validation/hash/approval error, fail the affected assembly before final success. If partial output exists, mark it incomplete/unusable and prevent acceptance of success manifests or distributable output. Preserve private failure evidence. Record failure accurately rather than claiming no filesystem writes occurred.

This PR supplies documents and a contract only; it does not install a package validator, change a workflow, execute a build or claim the private packager now enforces these rules. Cloud document checks may establish structure and links; issue #16 owns actual fail-closed integration.

## Review and adoption record

| Review role | Required decision on exact guide/contract hashes | Current status |
| --- | --- | --- |
| Maintainer | Content scope, required roles, exact adoption revision and handover disposition | PENDING |
| Build engineering | Consumer/destination mapping, complete input closure, variants and packaging enforcement | PENDING |
| Windows/QA | Procedure safety, prerequisites, lifecycle/recovery coverage and evidence limitations | PENDING |
| Security/IP | Newly authored content, confidentiality, publication/rights and trust wording | PENDING |

Independent Cloud documentation review is supporting evidence, not the above owners' sign-off. A merged documentation PR alone does not adopt these documents as installer inputs or authorise application source publication. All four decisions must be recorded for exact content before local packaging adoption. Keep confidential evidence and any private source IDs/hashes locally; return only approved public references.

## Private integration test matrix

Run each negative input independently against **each document**, keeping the other valid, to prove both are mandatory. Capture command, approved revision, injected condition, expected/actual outcome and limitations privately.

| Case | Required result |
| --- | --- |
| Missing file | Assembly fails; no completed distributable/success manifest accepted |
| Unreadable file | Real read failure refuses assembly; don't infer this from chmod alone under a privileged account |
| Zero-length / whitespace-only file | Both cases refuse; non-empty file existence is insufficient |
| Missing or renamed required section | Refuses and identifies missing/invalid section ID |
| Duplicate ID / empty body / placeholder-only body | Refuses even if other sections are complete |
| Heading only inside a code fence or comment | Does not satisfy completeness; refuses |
| Invalid encoding / malformed or unapproved contract | Refuses; no permissive fallback |
| Stale document with all headings present | Refuses when exact approved hash/revision differs |
| Valid reviewed inputs; excluded originals unavailable | Clean private assembly succeeds only after approved integration and full closure checks |
| Stale output/cache present | Cannot reintroduce excluded or obsolete content into a successful package |
| Every supported package variant | Required embedded/outer copies, relative links, inventory/archive entries and approved hashes agree |

Actual Windows installer/service/upgrade/repair/rollback and persisted-data acceptance are separately scoped; this drafting task runs none. Any intrusive test needs an exact plan, authorised operator and verified recovery baseline. Keep the existing acceptance VM off until explicitly scheduled. No distribution, signing, connected acceptance or production deployment follows from the build test matrix.

## Local handover and unresolved assumptions

After reviews, provide the public documentation commit, both public guide paths and SHA-256 hashes, contract path/hash/version, section IDs, generic destination roles, reviewer decisions and this matrix to issue #16 through the approved handover. Before adoption the local reviewer must resolve actual package mapping, link layout, version/platform prerequisites, candidate-specific entrypoint/recovery instructions and Windows evidence. The guides deliberately contain no invented runnable commands for unverified source.

Any edit that changes required meaning, section IDs or delivered bytes requires a new content/hash review and updated provenance. Reconcile application-source changes after earlier local inventories; these guides do not approve a proposed source-file count or source manifest. Preserve confidential originals and historical build identities without editing them to mask differences. Issues #12, #15 and #16 remain open until their own review/acceptance dispositions are recorded; installer issues #4/#5 and the remaining publication gates are independent.
