# Migration preparation: synthetic replacement examples

Status: **proposed content rules**, not migrated fixtures or validated application inputs. Tracked by [issue #12](https://github.com/Jdorrington17/Raptora/issues/12). Preserve confidential originals locally; publish only newly authored or expressly cleared examples after private review. Follow [security policy](../SECURITY.md) and the [publication checklist](PUBLICATION_READINESS_CHECKLIST.md).

## Replacement categories

| Category requiring local review | Proposed synthetic replacement | Private validation before publication |
| --- | --- | --- |
| Customer/site/camera/recording-server names and IDs | Deterministic labels such as `example-site-01`, `example-camera-01` and unrelated synthetic IDs | No real-name aliases, source-derived IDs, rare identifying combinations or retained relationships |
| IPs, DNS names, URLs and topology | Reserved documentation addresses and `example.invalid`; invented minimal relationships | No actual addresses, encoded endpoints, customer topology or executable probes; preserve address-validation edge cases separately |
| Credentials, authentication and connection examples | No usable credential; describe credential acquisition without values | Remove secrets from nested fields, comments, screenshots, URI user-info, headers, error strings and metadata; rotate confirmed exposures privately |
| Local paths, accounts and service identities | Logical labels `APP_ROOT`, `DATA_ROOT`, `TECHNICIAN_ACCOUNT`; approved product identity only if cleared | No usernames, profile directories, host identities, shares or private evidence references |
| Diagnostics, logs, timestamps and reports | Newly authored fixed-date records with expected outcome and source category | No copied operational records, real incidents, timezone/location clues, hidden document properties or current-run claims |
| Camera imagery, screenshots, logos, icons and fonts | Purpose-made geometric image fixtures or licensed assets with origin/notice records | Visual review and metadata stripping; no footage, EXIF, screenshots of operational systems or unapproved branding |
| Installation, update, repair and rollback walkthroughs | Invented version/transaction labels in explicitly illustrative prose, and approved support/acceptance requirements | No actual transaction IDs, historical manifest hashes, private build locations or implied successful rollback |
| Vendor modules, SDK examples and binaries | Publicly licensed minimal examples or separately acquired prerequisites | Validate first-party authorship, vendor terms, notices and distribution rights; don't copy vendor samples by assumption |

Use RFC 5737 documentation address ranges (`192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`) and reserved `.invalid` names for static illustrations. Do not connect to them or interpret them as authorised test targets. Synthetic data still needs schema/semantic validation once cleared source exists.

## Newly authored illustrative records

This is a **documentation example schema**, not the application's configuration/API schema. No executable connection, authentication or installer command is provided.

```json
{
  "exampleOnly": true,
  "sourceCategory": "synthetic-documentation",
  "observedUtc": "2000-01-01T00:00:00Z",
  "siteLabel": "example-site-01",
  "cameraLabel": "example-camera-01",
  "endpointLabel": "camera-01.example.invalid",
  "condition": "unknown",
  "severity": "unassessed",
  "confidence": "unassessed",
  "applicability": "unverified",
  "issueState": "open",
  "reason": "No successful collection evidence is available."
}
```

Illustrative policy refusal text: `MachinePolicy=Restricted prevents the requested support-script operation. No override was applied. Contact the policy administrator.` This defines desired communication, not evidence that an installed build produces it.

## Required fixture scenarios after source clearance

| Scenario | Expected semantic assertion |
| --- | --- |
| Missing, failed or unsupported check | Unknown/unavailable or unsupported; never successful by default |
| Stale observation | Retains original time and stale status; a new UI build does not refresh evidence |
| Policy refusal or script-integrity failure | Run is unavailable/failed with actionable reason; no new successful collection |
| Explicitly disabled camera | Applicability is explicit; do not invent an outage or general health |
| Confirmed synthetic symptom with uncertain cause | Condition, severity, confidence, applicability and issue state remain independent |
| Two recorders with repeated camera labels | Preserve recorder-qualified identity; no cross-device correlation |
| Failed installer transaction | Represent recovery and data verification separately; a message alone cannot prove rollback |

Schema adaptation and regression execution are deferred until approved application source is present. Do not add placeholder tests or claim these proposed scenarios passed.

## Private sanitisation review

1. Identify a category and required behavior, then author the replacement from a clean public brief. Do not make substitutions within private captures and assume that removes all identifiers.
2. Keep private origin/rights records and an original-to-replacement decision map. Do not include confidential original hashes or paths in public examples.
3. Review source, comments, hidden metadata, embedded media, archive entries, test snapshots and generated output. Automated patterns support human review; a clean scan does not establish rights or anonymity.
4. Validate syntax, actual cleared schema, expected failure/unknown outcomes and build/test usage. Review images visually and verify required attribution/notices.
5. Have the authorised data/security and IP/asset owners approve exact replacement file hashes. Any new bytes require re-review and an updated allowlist. Only then include the cleared replacement in a migration PR.

Current result: replacement categories and fresh illustrative content are proposed; original operational examples have **not** been replaced or privately re-reviewed by this Cloud task.
