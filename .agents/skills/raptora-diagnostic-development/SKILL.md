---
name: raptora-diagnostic-development
description: Use when changing Raptora diagnostic rules, evidence contracts, camera correlation, technician investigations, or issue lifecycle behavior.
---
# Develop diagnostics from evidence

Confirm approved source and acceptance criteria exist; this skill does not authorize migration or new functionality. Read the current contracts and fixtures before designing a change.

Keep **condition, severity, confidence, applicability and issue state independent**. Qualify camera identity by recorder and evidence source/time. Missing, stale, contradictory or unsupported evidence remains Unknown/Review; query success does not prove healthy recording, policy compliance or a physical root cause.

Return this design record before implementation:

| Field | Required content |
| --- | --- |
| Requirement/contracts | Approved scope, affected producers/consumers and persisted compatibility |
| Evidence rule | Inputs, provenance/freshness, applicability and deterministic conclusion |
| Counterexamples | Healthy, adverse, unknown, stale, contradictory and duplicate-camera-across-recorder fixtures |
| Lifecycle | Detect → Diagnose → Correlate → Refine Diagnosis → Rectify → Verify → Monitor; explicit transitions and permissions |
| Verification | Commands, actual outcomes, Windows/connected gaps and review decisions |

Use synthetic fixtures only. Test false positives and recorder isolation alongside expected findings. Separate passive interpretation from active probes or remediation: those require explicit target/scope authorization. Preserve configuration and existing evidence. Do not invent continuous monitoring from isolated observations.

Apply raptora-verify-code for evidence reporting; stop dependent implementation if source or approvals are absent.
