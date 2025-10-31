# api/Dockerfile
# Masonite (Python) — dev/lean prod image
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    APP_HOME=/app

WORKDIR ${APP_HOME}

# System deps (add others your project needs, e.g. libpq-dev for Postgres, default-libmysqlclient-dev for MySQL C client)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl ca-certificates git \
 && rm -rf /var/lib/apt/lists/*

# (Optional) separate layer for dependencies cache
FROM base AS deps
COPY requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip \
 && pip install -r requirements.txt

# Runtime
FROM base AS runtime
# Create non-root user
RUN useradd -u 10001 -m appuser
COPY --from=deps /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=deps /usr/local/bin /usr/local/bin

# Copy app
COPY . ${APP_HOME}
RUN chown -R appuser:appuser ${APP_HOME}
USER appuser

# Masonite default dev server binds via "python craft serve"
# For prod, consider gunicorn/uvicorn if applicable to your Masonite version.
EXPOSE 5000

# Health endpoint suggestion: add a /health route in your app
ENV APP_HOST=0.0.0.0 APP_PORT=5000
CMD ["bash", "-lc", "python craft serve --host ${APP_HOST} --port ${APP_PORT}"]
