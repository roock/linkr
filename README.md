# Linkr

Linkr is a self-hosted read-later application built with Django, HTMX, PostgreSQL, and uv.

## Development environment

### Prerequisites

- Docker with Docker Compose
- VS Code with Dev Containers (optional but recommended)
- uv (for local execution)

### VS Code Dev Container

1. Open the repository in VS Code.
2. Run **Dev Containers: Reopen in Container**.
3. The container creates the environment and applies migrations.
4. Start the server:

   ```sh
   uv run python manage.py runserver 0.0.0.0:8000
   ```

Open <http://localhost:8000>.

### Docker Compose

```sh
cp .env.example .env
docker compose up --build
```

The web process starts automatically and PostgreSQL is available on port 5432.

### Local Python without Docker

PostgreSQL is still required. Either use Compose for the database:

```sh
docker compose up db -d
export DATABASE_URL=postgresql://linkr:linkr@localhost:5432/linkr
uv sync --dev
uv run python manage.py migrate
uv run python manage.py runserver
```

## Checks

```sh
uv run ruff check .
uv run ruff format --check .
uv run pytest
uv run python manage.py check
```

Django can also use SQLite when `DATABASE_URL` is unset. This is intended for isolated local checks, while development and deployment use PostgreSQL.
