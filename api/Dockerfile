# api/Dockerfile
# Masonite (Python) — dev/lean prod image
FROM python:3.11-slim AS base

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
WORKDIR /tmp/build
COPY requirements.txt ./requirements.txt

# Pin pip to avoid metadata parsing issues with Masonite 4 wheels
RUN python -m pip install --upgrade "pip<24.1" \
 && pip install -r requirements.txt

FROM base AS runtime
RUN useradd -u 10001 -m appuser
WORKDIR ${APP_HOME}
COPY --from=deps /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=deps /usr/local/bin /usr/local/bin
COPY . ${APP_HOME}
RUN chown -R appuser:appuser ${APP_HOME}
USER appuser

EXPOSE 5000
ENV APP_HOST=0.0.0.0 APP_PORT=5000
CMD ["bash", "-lc", "python craft serve --host ${APP_HOST} --port ${APP_PORT}"]