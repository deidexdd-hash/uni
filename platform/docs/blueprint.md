# Unified Platform Blueprint

## Goal

Create a single modular platform that combines Rod System, Tree, Tarot, Numerology, Practices, AI, and Telegram.

## Architectural principles

- Modular Monolith
- Plugin Architecture
- Event Bus
- Domain Driven Design (Light)
- Clean Architecture
- API First

## Technology stack

### Backend

- Python 3.13
- FastAPI
- SQLAlchemy 2
- Alembic
- Pydantic v2

### Frontend

- Next.js
- TypeScript
- Tailwind CSS
- shadcn/ui
- TanStack Query

### Infrastructure

- PostgreSQL
- Redis
- RabbitMQ
- Qdrant
- MinIO
- Docker
- GitHub Actions

## Roadmap

| Sprint | Scope |
| --- | --- |
| 1 | Repository, Docker, CI/CD, database |
| 2 | Shared, Auth, Users |
| 3 | AI, Telegram |
| 4+ | Domain modules, UI, admin, optimization |
