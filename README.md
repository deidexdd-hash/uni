# Unified Rod Platform — Software Architecture Book

This repository is the architecture repository for the future Unified Rod Platform product. It is intentionally documentation-first: every strategic, domain, technical, security, migration, and delivery decision is described before implementation starts.

## Purpose

The goal is to create a complete Architecture Book for a unified modular platform that combines Rod System, Tree, Tarot, Numerology, Practices, AI, Telegram, media, search, billing, analytics, and administration.

The book is written sequentially, chapter by chapter, without compressing the engineering rationale. Each chapter is designed to become directly usable by product owners, architects, backend engineers, frontend engineers, DevOps engineers, security reviewers, and future implementation teams.

## Repository structure

```text
unified-platform-architecture/
├── docs/                 # Architecture Book chapters grouped by volume
├── diagrams/             # Mermaid, C4, UML, ERD, and sequence diagrams
├── adr/                  # Architecture Decision Records
├── templates/            # Chapter, ADR, API, and diagram templates
├── api/                  # API specifications and examples
├── database/             # Database model and migration design
├── roadmap/              # Delivery roadmap and sprint planning
└── README.md
```

## Volumes

1. Volume I — Vision
2. Volume II — Domain
3. Volume III — Architecture
4. Volume IV — Backend
5. Volume V — AI Platform
6. Volume VI — Database
7. Volume VII — API
8. Volume VIII — Frontend
9. Volume IX — Infrastructure
10. Volume X — DevOps
11. Volume XI — Security
12. Volume XII — Migration
13. Volume XIII — Roadmap

## Chapter format

Every full chapter should include:

- detailed description;
- architectural decisions;
- Mermaid diagrams;
- C4, UML, ERD, or sequence diagrams where relevant;
- API examples where relevant;
- development rules;
- implementation recommendations;
- risks and trade-offs;
- acceptance criteria.

## Current writing status

- Chapter 01 — Vision and Product Strategy: drafted.
- Remaining chapters: planned in the master table of contents.
