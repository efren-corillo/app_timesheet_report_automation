#!/usr/bin/env bash
# Run from the repository root to build & start the stack consistently.

set -euo pipefail

PROJECT_NAME="${PROJECT_NAME:-timesheetapp}"
COMPOSE_FILE="deployment/docker-compose.yml"
ENV_FILE="deployment/.env"
export LOCAL_UID="${LOCAL_UID:-$(id -u)}"
export LOCAL_GID="${LOCAL_GID:-$(id -g)}"

usage() {
  cat <<'EOF'
Usage: ./run.sh [build|up|down|restart|logs|ps] [--rebuild]

Commands:
  build       Build images (respecting cache)
  up          Start or recreate containers in the background
  down        Stop and remove containers, networks (keeps volumes)
  restart     Restart all services
  logs        Tail caddy logs (change as needed)
  ps          Show container status

Options:
  --rebuild   Force rebuild without cache

Env vars:
  PROJECT_NAME=timesheetapp (default)
EOF
}

cmd="${1:-up}"
shift || true

REBUILD_FLAG=""
if [[ "${1:-}" == "--rebuild" ]]; then
  REBUILD_FLAG="--no-cache"
  shift || true
fi

dc() {
  docker compose -p "$PROJECT_NAME" -f "$COMPOSE_FILE" --env-file "$ENV_FILE" "$@"
}

case "$cmd" in
  build)
    dc build $REBUILD_FLAG
    ;;
  up)
    dc build $REBUILD_FLAG
    dc up -d
    ;;
  down)
    dc down
    ;;
  restart)
    dc down
    dc up -d
    ;;
  logs)
    dc logs -f caddy
    ;;
  ps)
    dc ps
    ;;
  -*|help|--help)
    usage
    ;;
  *)
    echo "Unknown command: $cmd"
    usage
    exit 1
    ;;
esac
