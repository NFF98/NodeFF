# NodeFF Product Discussion

## Purpose
Working notes for NodeFF product discussions before decisions are approved into the official specification.

## Status
- Working document — **not SSOT**
- Nothing here is an approved product decision unless explicitly moved into `spec/` or `decisions/` after user approval.

## Discussion Notes

### Top Mission / Game-Changing Reason
The user identified the following source material as the starting point for NodeFF's top mission / game-changing reason:

- NodeFF aims to challenge the traditional App model by reducing or eliminating the friction created by apps as isolated containers.
- **Zero Cross-App Friction:** a user's natural-language intent can potentially chain multiple C2C APIs/data capabilities in the background, instead of requiring manual app switching, copying, and pasting.
- **Intent-adaptive UI / Disposable UI:** instead of forcing users through fixed app pages, the interface can be dynamically composed around the user's current intent and only expose the capabilities needed for that task.
- The proposed ecosystem shift is from users finding and operating individual apps toward users expressing intent while underlying capability providers become composable services/APIs.
- The source describes a possible end state in which users care less about which app provides a function and more about whether the generated experience solves the immediate problem; creators can focus on individual capability blocks/APIs.
- The technical direction described in the source uses LLMs as a declarative compiler: natural language is transformed into structured logic/UI/data-flow specifications rather than arbitrary raw code, with a reusable runtime/player rendering those specifications.
- The source specifically describes semantic parsing, delta editing/JSON Patch, and declarative logic synthesis as key AI capabilities.

### Five Key Principles
Current working keys identified by the user:

| # | Key |
|---:|---|
| 1 | **No install setup** |
| 2 | **Everyone is the creator** |
| 3 | **Sharable, linkable** |
| 4 | **Intent Commerce** |
| 5 | **Fun and socialable** |

**Important:** These are captured as working discussion points, not yet approved NodeFF product requirements, architecture decisions, or claims of market outcome.
