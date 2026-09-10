# ref/bibliography.md — sources

## Primary (theory)

- **Stafford Beer** — *Brain of the Firm* (1972), *The Heart of Enterprise*
  (1979). The VSM canon: S1–S5 + S3\*, channels, the algedonic signal, variety
  engineering, recursion, the basta constraint.
  - Included in the template as PDFs: `Chapter 5_ The Viable System Model.pdf`,
    `bir2.pdf` (source materials).
- **Organizational Synthesis Model (OSM)** — the RFC (an extension of VSM:
  transformation primitives, synthesis phases, Assisted Viability). In the
  template: [`../synthesis/osm.md`](../synthesis/osm.md).

## Reference implementations (adaptations)

- **ViableOS** (`philipp-lm/ViableOS`) — a reference VSM implementation; the
  `vsm.yaml` schema (system_1..5 + budget + algedonic) is adapted from here. See
  the summary in the reference project `opensiro-arctic/vsm/ref/viableos-mapping.md`.
- **opensiro-arctic/vsm** — a mature implementation of a single controlling VSM
  (governing the Opensiro Collections pipeline through Claude subagents). The
  direct structural ancestor of vsmlite. See
  [`../meta/reference-mapping.md`](../meta/reference-mapping.md).
- **Future fleet aggregator** (not yet built) — a planned fleet-level consumer
  that would aggregate S3/S4 knowledge across many child VSMs. The design intent
  behind vsmlite's telemetry. The contract is in
  [`telemetry-contract.md`](telemetry-contract.md); the rationale is in
  [`../meta/fleet-digest.md`](../meta/fleet-digest.md).

## Internal template documents

| Document | Purpose |
|---|---|
| [`../CLAUDE.md`](../CLAUDE.md) | The vsmlite S5 constitution |
| [`../vsmlite.yaml`](../vsmlite.yaml) | The model (child, synthesis, systems, telemetry) |
| [`../synthesis/osm.md`](../synthesis/osm.md) | The OSM RFC |
| [`../synthesis/primitives.yaml`](../synthesis/primitives.yaml) | OSM primitives |
| [`../synthesis/phases.yaml`](../synthesis/phases.yaml) | Maturation phases |
| [`vsm-theory.md`](vsm-theory.md) | VSM (Beer), domain-agnostic |
| [`osm-theory.md`](osm-theory.md) | Pointer to OSM |
| [`telemetry-contract.md`](telemetry-contract.md) | Forward telemetry contract |
| [`../meta/fleet-digest.md`](../meta/fleet-digest.md) | Frontier-model context on fleet aggregation |
| [`../meta/osm-summary.md`](../meta/osm-summary.md) | OSM in three paragraphs |
| [`../meta/reference-mapping.md`](../meta/reference-mapping.md) | Map of borrowings |
