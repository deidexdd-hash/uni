# ADR 0001 — Use a documentation-first architecture repository

## Status

Accepted

## Context

Unified Rod Platform combines multiple domains, AI, Telegram, frontend, backend, database, infrastructure, security, migration, and roadmap concerns. Starting with implementation before stabilizing architecture would increase the risk of fragmented modules and inconsistent product decisions.

## Decision

Create a dedicated architecture repository with chapters, diagrams, ADRs, API specifications, database design, templates, and roadmap documents before creating the production implementation repository.

## Consequences

- Product and engineering decisions are documented before implementation.
- The implementation repository can be generated from stable architecture decisions.
- Architecture work can proceed chapter by chapter.
- Documentation must be maintained as a first-class artifact.
