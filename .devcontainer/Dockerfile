FROM ghcr.io/astral-sh/uv:python3.13-bookworm

WORKDIR /workspace

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --dev
