# NodeFF — SSOT

> Single Source of Truth for the NodeFF project.

## Status

- Project: NodeFF
- Repository: `NFF98/NodeFF`
- Default branch: `main`
- Specification status: Initial structure

## Purpose

This file defines the authoritative project structure and governance rules for NodeFF.

## SSOT Rules

1. Product decisions are recorded in `spec/` or `decisions/`.
2. Execution status is recorded in `execution/`.
3. No parallel or duplicate source of truth should be created.
4. Code must follow the approved specifications.
5. Material changes to product behavior must update the relevant specification before implementation.
6. `decisions/` records decisions that materially affect architecture, product direction, or constraints.
7. `execution/CHANGELOG.md` records shipped or committed changes.

## Project Structure

```text
SSOT.md
README.md
spec/
  01-PRODUCT.md
  02-PROBLEM.md
  03-REQUIREMENTS.md
  04-USER-FLOWS.md
  05-DATA-MODEL.md
  06-SYSTEM.md
  07-API.md
  08-UI.md
  09-SECURITY.md
  10-NON-FUNCTIONAL.md
  11-ACCEPTANCE.md
decisions/
  .gitkeep
execution/
  BACKLOG.md
  SPRINT.md
  CHANGELOG.md
```

## Authority Order

1. `SSOT.md`
2. `spec/`
3. `decisions/`
4. `execution/`
5. Implementation code and tests

## Change Control

If a proposed implementation conflicts with the current specification, stop implementation and resolve the specification or record an explicit decision first.
