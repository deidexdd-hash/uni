# Unified Platform

Unified Platform is a modular monolith blueprint for Rod System, Tree, Tarot, Numerology, Practices, AI, and Telegram capabilities.

## Architecture

The repository is organized around a backend modular monolith, frontend app, admin app, documentation, and deployment assets.

```text
platform/
  backend/
    app/
    shared/
    modules/
    infrastructure/
  frontend/
  admin/
  docs/
  docker/
```

## Development order

1. Foundation
2. Shared
3. Auth
4. Users
5. AI Core
6. Telegram Core
7. Domain Engines
8. Frontend
9. Admin
10. Production

## Quick start

```bash
cd platform/backend
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

## Docker

```bash
docker compose -f platform/docker/docker-compose.yml up --build
```
