# Migration preparation: packaging document dependencies

Status: **BLOCKED for source publication**. This document is a public-safe plan for [issue #12](https://github.com/Jdorrington17/Raptora/issues/12), not a source import, packaging change or release approval. Follow [engineering instructions](../AGENTS.md), the [private audit procedure](PRIVATE_MIGRATION_AUDIT.md) and [source activation gates](SOURCE_ACTIVATION_PLAN.md).

## Evidence and scope

The local reviewer reports 392 source files reverified, 271 proposed inclusions, 121 proposed exclusions and 8/8 private review-record hashes verified, with originals unchanged. Cloud has read the sanitised GitHub handover; it has not independently verified those local files, hashes or approvals. Proposed inclusion does not authorise publication. An exact current snapshot must be reconciled whenever source changes after that review.

Two excluded documents reportedly remain installer-packaging inputs. Their names, contents, paths and exact consumers are not cleared in the public handover. Treat them as two distinct blockers, not as approved files. The generic dependency relationship is: **package assembly requires a document input currently outside the proposed public allowlist**. This does not establish that either document affects executable behavior, or that it is optional.

## Dependency decisions

| ID | Verified public evidence | Recommended disposition | Information still required | Status / responsible role |
| --- | --- | --- | --- | --- |
| PKG-DOC-01 | One of two excluded documents is reported as a packaging input | Prefer a newly authored public-safe equivalent if the document is required; otherwise remove the reference after proving it unnecessary | Sanitised consumer/purpose, required sections, destination role, missing-input behavior and validation method | BLOCKED: local build reviewer; security/IP reviewer; maintainer decision |
| PKG-DOC-02 | A second excluded document is reported as a packaging input | Evaluate independently using the same rule; do not assume the same consumer or substitute | Sanitised consumer/purpose, required sections, destination role, missing-input behavior and validation method | BLOCKED: local build reviewer; security/IP reviewer; maintainer decision |

Selection order for each input:

1. **Remove** only if the local reviewer demonstrates no required build, runtime, contractual notice, user-support, acceptance or recovery obligation depends on it. Update all references and validate package contents; an unchecked copy omission is not resolution.
2. **Substitute** when guidance is required but private wording is unnecessary. Write new content from public engineering requirements, with a local mapping of required sections. Do not paraphrase confidential evidence or silently omit installation, failure, recovery or rollback warnings. Regenerate references, manifests and source hashes after the approved change.
3. **Clear the original** only if an authorised owner expressly approves the exact content for publication and security/licensing review passes. A build dependency is not a publication right. If rights or a necessary substitute cannot be established, keep migration blocked.

Recommended public replacement roles, subject to the local contract: generic package-use guidance and a Windows acceptance/limitations guide. These are proposed roles, **not findings about the two originals**. Newly authored content must distinguish build integrity, publisher trust, actual Windows acceptance and production authorisation. Include exact candidate identity fields only when cleared; never fill them with invented historical values.

## Sanitised Local Codex return contract

Return one record per ID through issue #12 or a scoped review comment. Do not send original documents, private filenames/paths, raw source, customer examples, confidential hashes or private evidence locations.

| Field | Public-safe response |
| --- | --- |
| Dependency ID | PKG-DOC-01 or PKG-DOC-02 |
| Purpose and consumer | Generic role such as packaging copy, generated guidance, UI help, notice or integrity inventory; no private implementation excerpt |
| Requiredness | Required / optional / unknown, with a sanitised reason |
| Contract | Required topics, encoding/format, destination role and whether content is rendered, executed, hashed or simply distributed |
| Failure behavior | What happens when the input is absent; any fail-closed requirement |
| Selected disposition | Remove / newly authored substitute / exact-content clearance / blocked |
| Review | Responsible role, disposition approved or pending, and publishable decision reference |
| Validation | Exact reviewed revision when cleared, check category, result and limitations; original evidence remains private |

## Dependency closure acceptance

Both rows remain open until the local reviewer and maintainer record a decision and evidence for each separately. Required evidence after an authorised source change:

- No remaining references to excluded inputs in assembly, packaging, tests, release notes, archive creation or user-facing links.
- Required guidance/notices remain available in every supported package format; any omission is explicitly approved. Missing required guidance fails packaging rather than yielding a green partial package.
- A clean source build succeeds without the excluded originals and without reading outside the approved source/asset allowlist.
- The package contains only approved files; manifests, declared inventory, ZIP contents, file hashes and documentation links agree. Confirm stale build directories cannot reintroduce excluded material.
- Required collector/runtime source dependencies remain in the approved build closure or are replaced by separately reviewed, functionally verified equivalents. Do not exclude executable dependencies merely because their names are historical.
- New hashes and provenance bind the final replacement/removal to the exact snapshot; no editing historical build identities to hide a discrepancy.

No application build, Windows test or packaging change is executed by this documentation. Public source transfer remains blocked until the [publication-readiness checklist](PUBLICATION_READINESS_CHECKLIST.md) is approved. Issues [#4](https://github.com/Jdorrington17/Raptora/issues/4) and [#5](https://github.com/Jdorrington17/Raptora/issues/5) retain their independent installer acceptance criteria. Coordination is tracked by [#10](https://github.com/Jdorrington17/Raptora/issues/10); this plan does not configure remote access or a runner.
