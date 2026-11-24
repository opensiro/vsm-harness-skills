# Candidate interpretation calibration (proposed 0.3.10)

**Status:** experimental proposal, not a released Methodology or an active default requirement. Apply only under an explicitly pinned candidate assessment contract. Profile 0.2.4 and Methodology 0.3.9 remain authoritative for existing assessments. This guide proposes compatible application clarifications; it does not prescribe target grades, redefine a VSM function, alter ownership notation, ranking, or introduce a new evidence threshold.

## 1. Boundary and assessment question

Before mapping, identify the assessed system, recursion, operational outcomes, and supported first-party modes. Distinguish a supported optional installation/configuration or explicitly integrated companion from a development/dogfood/CI/evaluator or downstream system. Repository co-location is neither necessary nor sufficient: when an integration is material, establish the responsibility it supplies, its reachability in the declared mode, and source/version provenance where available. Do not borrow an external host's autonomous actor merely because a tool or adapter is available. Do not combine incompatible recursions as one organization.

If two judgments describe different supported scopes, state the scope difference before treating them as contradictory. A negative finding is limited to the actually reviewed boundary; an unresolved plausible supported mode is material evidence uncertainty, not proof of absence. Documentation may be primary evidence under the existing rules; describe the limits of a closed or inaccessible implementation instead of claiming source inspection.

**Contrast:** A first-party integration explicitly ships an optional, versioned companion with a reachable operating loop; examine that supported mode. A README merely points to a third-party tool that might implement a loop; no ownership is established by the link.

## 2. Function before ownership; distinguish the regulated relation

A component can realize more than one function, but each mapping needs its own disturbance, decision right, owner and return. Neither a separate named component nor multiple S1 units is a universal prerequisite for S3–S5; S2 specifically requires distinct S1 units.

- **S1:** retain 0.3.9's configuration-versus-composition distinction. Name the missing autonomy element if proposing C; ordinary activation/configuration of supplied autonomy is not that element.
- **S2:** the concrete inter-S1 interference can be prevented rather than observed as a realized incident. Show the specific disturbance and how an intended coordination relation affects later S1 behavior. A lock, worktree isolation or dependency ordering may be function-specific evidence where a collision mode and relation are established. Generic messaging, sequencing, delegation and the abstract possibility of conflict do not suffice.
- **S3:** distinguish whole-current regulation of resources, priorities, commitments, constraints or accountability from a local operational plan. Planning can qualify only when it actually exercises the requisite organizational right and closes into current operation. Retry/tier/queue/budget enforcement alone does not supply the decision owner or the function-specific constructor.
- **S4:** distinguish outside-and-then sensing and adaptation from ordinary research, search, internal optimization or remembered history. Identify the environmental or future-relevant distinction, prospective adaptation judgment/option, and return into present capability. The same actor may own both S1 and S4, but task completion or use of an external tool alone is not evidence of adaptation. User feedback may be an external distinction if the remaining loop is established.
- **S5:** identify the identity/ultimate-policy issue, legitimate authority, authoritative decision and return into subsequent operation. Self-editing capacity, a persona, an approval gate or a static system prompt alone is insufficient. Human ordinary task authority is not ultimate policy authority.

**Contrasts:** An agent chooses a dependency constraint to prevent identified shared-file interference; investigate S2 ownership. A fixed workflow simply sequences tasks; no S2 follows. A planner chooses whole-team commitments on the basis of current resources and returns them into execution; investigate S3. A task planner only decomposes one request; no S3 follows. A literature search informs a present deliverable; it can remain S1. Evidence of externally informed prospective adaptation of capability may support S4. Editing an ordinary instruction does not by itself establish S5.

## 3. A versus C versus support

Identify the actual decisive owner using the Profile's counterfactual owner test; separate judgment from deterministic enforcement. A supported optional mode is not C simply because a developer enables, installs, configures or supplies an ordinary model binding. A requires the supplied autonomous actor, actual authority and reachable function-specific closure. C requires a first-party, intentionally exposed function-specific path and identification of the remaining composition step for autonomous actor, authority, independence or closure. General extensibility is insufficient.

If a proposed A is not established, independently test C rather than automatically downgrading it. Apply bounded absence or unknown adjudication if neither is established. Do not equate a deterministic mechanism with C without the required function-specific path.

**Contrast:** A shipped optional reviewer that is already autonomous, has independent evidence and returns actionable findings can qualify for A; an explicitly supplied audit constructor requiring an auditor or feedback binding can qualify for C. A generic callback that could host arbitrary future review does not qualify merely by possibility.

## 4. Claim-relative S3* independence

Identify the ordinary report or claim, the complementary evidence access, the audit judgment owner and independence from the producing claim, and the feedback into legitimate control. Neither use of another vendor nor another invocation/prompt alone is sufficient or necessary. Inspect how the actor obtains materially different access and can challenge the original report. A separate review call using the same model is not automatically independent or non-independent. An independent auditor need not have its own S3 decision authority; findings must return into a relevant control/operation path under existing criteria. Distinguish a specifically supplied constructor from a generic hook. S3* does not take P, A(P), or C(P).

**Contrast:** A judge sees only a producer's self-report and repeats routine acceptance scoring; independent evidence is not established by the label judge. A fresh actor can inspect the actual artifacts or raw trace and return corrective findings; test claim-relative independence and authority under the declared mode. A separate provider receiving no complementary evidence does not establish S3* solely by being separate.

## 5. Explicit alternative ownership-mode review for S3/S4/S5

For each established or plausible function, independently investigate (a) supported autonomous closure, (b) function-specific constructor, (c) supported parent closure. Each candidate needs function-specific decisive right, owner, reachability and return. Enumerate plausible shipped modes before concluding no additional positive mode is established. Distinguish a legitimate parent decision from ordinary intervention/approval. An identified parent mode is not a reason to skip the base-mode inquiry, and vice versa.

Apply the existing decision order and symbols: A(P) or C(P) only when both respective modes are positively established for the same function at the same recursion. Use standalone P when the parent mode is the only established positive mode. If a material additional mode remains unresolved, preserve the established positive finding and document the unresolved alternative in existing Evidence gaps / caveats rather than inventing a composite or claiming a proven absence of that mode. If no positive mode is established and the gap prevents a defensible negative, use ?. Record the existing mode matrix for composites; this proposal adds no required schema field.

**Contrast:** an autonomous current-control path plus an independently evidenced operator-owned whole-current path can support A(P). A constructor plus the latter may support C(P). Operator permission to stop a run does not establish P by itself. Absence of a qualifying parent mode is not a deficiency.

## 6. Competing interpretations and honest evidence

For a material contested judgment, reconstruct the strongest plausible alternative, then identify the concrete rule, boundary or source witness that distinguishes it. If evidence is insufficient, state the gap. A clear rule violation is not a competing valid interpretation. Internally coherent prose cannot substitute for source evidence. Verify pinned paths and relevant symbols where possible; distinguish actual reads from inference and inaccessible code. Apply the existing bounded three-part absence scope for negative conclusions. Do not choose marks to match a prior assessment or achieve a frequency. Preserve uncertainty; validate the function-specific state alphabet before submission.

A disagreement review may distinguish scope mismatch, missing evidence, misapplication, unresolved same-scope ambiguity, and genuinely defensible scope-relative claims. A prior accepted assessment is not an adjudication oracle. The same rule applies symmetrically to agreeing and disagreeing assessments. The guide is an analytical aid using existing fields; no new mandatory executable trace, runtime experiment, proof burden or artifact schema.

## Compatibility and release gate

The candidate is compatible only if the existing definitions, publication state set, evidence thresholds, structural artifact contract, synthesis and ranking remain unchanged. A historical label may be corrected through ordinary source re-review, but no automatic regrade or provenance rewrite is authorized. If resolving a genuine same-scope normative ambiguity requires changing the valid classification predicate or publication contract, stop and propose a separately versioned semantic change (potential 0.4.0); do not hide it in a patch.

Before release, verify the wording against the Profile, autonomy states, existing positive/negative calibration guides and contrasting cases. Review independent source-grounded reassessments under the old and candidate rules, including counterexamples and missing-evidence cases. Agreement alone is not acceptance. Preserve unresolved cases and negative results. A structural checker cannot adjudicate semantic truth. Only after review and release approval update the version/changelog, validator compatibility and release metadata and run the existing tests. Until then this candidate is not the active Methodology.
