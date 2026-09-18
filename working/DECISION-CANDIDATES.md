# NodeFF Decision Candidates

## Purpose
Capture potential product or architecture decisions while they are still being discussed.

## Status
- Working document — **not SSOT**
- A candidate becomes authoritative only after explicit user approval and migration into `decisions/` or the appropriate `spec/` file.

## Candidates

_None yet._


## Candidate Decision — Rule Representation Strategy
Status: WORKING / NOT APPROVED

Question: should Layer 3 represent dynamic rules primarily as free-form restricted expression strings or as a typed declarative Rule AST?

Current evidence favors evaluating a typed Rule AST because it can improve static validation, allowlisting, dependency analysis, resource bounding, versioning and deterministic serialization.

This decision must be resolved before locking the detailed Layer 3 contract and instructing Cursor to implement the rule engine.

## Candidate Decision — Initial Rich Primitive Catalog
Status: WORKING / NOT APPROVED

The proposed initial 15 primitives are recorded in `working/APP-ARCHITECTURE.md`. Exact names, props, security policies and inclusion remain subject to detailed review before SSOT promotion.
