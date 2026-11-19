# OpenSiro Local — quickstart

**Audience:** an owner working in a local, private, or self-hosted AI-agent harness repository. This is an experimental agent skill; it is **not** a standalone command-line program.

## Install for a supported Agent Skills client

Copy the entire `skills/opensiro-local/` directory into that client's supported skills directory (for example `.claude/skills/opensiro-local/` for Claude Code). Install the **entire** `skills/assess-vsm-harness/` directory alongside it so the pinned Profile and Methodology references are available. The agent must also have access to the current [Upstream Capability Roadmap](https://github.com/opensiro/upstream/blob/main/docs/CAPABILITY_ROADMAP.md) for the full roadmap stage.

Installation is client-specific; simply viewing this repository does not install a slash command.

## Copy/paste entry prompt

> Use the installed `opensiro-local` skill on **this repository only**. First show the system-in-focus, source revision/dirty state, model/data privacy considerations, and available commands. Start with a **read-only assessment**, using the installed `assess-vsm-harness` methodology. Do not change files, run unsafe commands or publish anything without my explicit permission. If the methodology or repository cannot be inspected, say what remains blocked instead of guessing.

Then request, as separate actions:

- `/opensiro-local assess` — independently classify S1/S2/S3/S3*/S4/S5 with primary evidence.
- `/opensiro-local roadmap` — research existing native alternatives and a defensible C construction, or finish `NO_QUALIFIED_C_TARGET`.
- `/opensiro-local upgrade` — **only after explicitly choosing a specific proposed case for implementation**.
- `/opensiro-local validate` — perform authorized native tests and compare to a predeclared baseline.
- `/opensiro-local reassess` — new source-pinned assessment, no automatic promotion.
- `/opensiro-local status` — report local artifact/readback state.

If the client cannot register the slash commands, use plain requests such as "Use opensiro-local: roadmap for this project".

## Private-project model boundary

A private worktree does **not** imply offline inference. Before sending source to a hosted model or network tool, check the AI provider's data handling and the project owner's policy. Never store API keys or secrets in Markdown reports. Do not publish or sync `.opensiro/` as a side effect of creating it; Git may include it in future commits unless deliberately excluded.

## What to expect

A completed local assessment is **LOCAL_UNREVIEWED**, not an accepted Index record. A qualified roadmap is **PLAN_ONLY** even when its proposal verdict is GO. The local three-document handoff is described in [local-artifacts.md](local-artifacts.md); it does not require any OpenSiro account, fork, or public GitHub issue.
