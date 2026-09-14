# Token and coordination overhead

Run this analysis only when a representative workload and sufficient model/topology evidence exist. Do not fabricate precision.

## Evidence priority

1. provider-reported usage per request/run;
2. traces containing input, cached input, reasoning/output, and call counts;
3. exact tokenizer over reconstructed serialized messages;
4. compatible tokenizer or provider counting endpoint;
5. calibrated character/token range;
6. qualitative result only.

Record model IDs, workload, source level, cache treatment, assumptions, and confidence.

## Workload boundary

Keep task class, run count, topology, models by role, shared and role context, expected turns, tool schemas, retries, and output range together. Do not compare totals from different workloads without prominently stating the mismatch.

For call `i`:

```text
T_i = new_input_i + cached_input_i + output_i + reported_reasoning_i
T_run = sum(T_i across calls and roles)
```

Show raw traffic separately from provider-billed equivalents. Cached tokens still consume context and transport even when discounted.

## Duplication

1. Normalize line endings and trailing whitespace without changing code or meaning.
2. Split context into stable semantic blocks.
3. Hash exact blocks for a conservative lower bound.
4. Detect near-duplicates separately and report a reviewable range.
5. Build the invocation matrix showing which blocks reach each role, call, and turn.
6. Separate required replication of identity/safety/permissions from avoidable repeated background, schemas, and examples.

```text
sent_tokens = sum(tokens(block) × transmissions(block))
exact_duplicate_tokens = sum(tokens(block) × max(transmissions(block)-1, 0))
avoidable_duplication_rate = avoidable_duplicate_tokens / sent_tokens
```

Compare current, MIN, MODULAR, and MAX scenarios using low/base/high call counts, context growth, retries, cache rate, and latency. MAX is justified only when reduced collisions, retries, missed failures, or human coordination exceed added token, latency, and governance cost.

Treat prices, cache rules, context limits, and model behaviour as time-sensitive; verify them from official provider sources and record the retrieval date.
