# VSM template

This template intentionally contains only the portable core extracted from the larger `vsmlite` experiment.

Choose one shape:

- `min/` — one general prompt. Use when one agent can reason across all VSM functions and independent audit is not yet essential.
- `max/` — orchestrator plus repeated role prompts for S1, S2, S3, S3*, S4, and S5. Use when roles need independent context, concurrency, or audit separation.

Prefer `min`. Move to `max` only after measuring collisions, false positives, retries, or context pressure that the smaller topology cannot resolve.

The templates omit dashboards, benchmark adapters, heartbeats, fleet telemetry, maturation runtime, and provider-specific commands. Add them only when the project has an observed need.
