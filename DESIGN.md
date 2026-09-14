# Workflow boundary decision

## Decision

Keep `assess-vsm-harness` focused on one repository at one pinned revision. Document ordered cross-catalog comparison separately in `SYNTHESIS.md`.

## Rationale

A standalone assessment is repository-relative and should remain stable when the catalog changes. A comparison signature is cohort-relative and may change when an older harness is inserted. Mixing them would make evidence artifacts depend on unrelated catalog membership.

Within one assessment, S1-S5, S3*, recursion, variety, escalation, topology, token cost, and intervention analysis still share one boundary and evidence chain, so they remain one skill.

Cohort synthesis reads completed assessments and preserves their autonomy states. Ranking is a deterministic projection of those states rather than another interpretive workflow.
