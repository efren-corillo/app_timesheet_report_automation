# ui/Dockerfile
FROM node:20-alpine AS base
WORKDIR /app
ENV CI=1
RUN corepack enable

# Copy manifests if they exist (won't fail if some are missing)
COPY ../ui-back/package.json ./
COPY yarn.lock* ./
COPY package-lock.json* ./
COPY pnpm-lock.yaml* ./

# Install deps with the best available manager/lockfile
RUN if [ -f yarn.lock ]; then \
      yarn install --frozen-lockfile; \
    elif [ -f pnpm-lock.yaml ]; then \
      corepack prepare pnpm@latest --activate && pnpm install --frozen-lockfile; \
    elif [ -f package-lock.json ]; then \
      npm ci; \
    elif [ -f package.json ]; then \
      npm install; \
    else \
      echo "No package.json found; skipping install"; \
    fi

# Then copy the rest of the sources
COPY ../ui-back .

# CMD if [ -f yarn.lock ]; then \
#      yarn dev -H 0.0.0.0 -p 8080; \
#    elif [ -f pnpm-lock.yaml ]; then \
#      pnpm dev --host 0.0.0.0 --port 8080; \
#    else \
#      npm run dev -- --host 0.0.0.0 --port 8080; \
#    fi

# -------- Production build example (optional) --------
# FROM base AS build
# RUN if [ -f yarn.lock ]; then yarn build; \
#     elif [ -f pnpm-lock.yaml ]; then pnpm build; \
#     else npm run build; fi
#
# # Then either:
# # 1) copy dist/ into a Caddy image and serve static files, or
# # 2) keep your reverse-proxy to the dev server in compose for local only

EXPOSE 8080
CMD sh -lc '\
  if ! npx --yes quasar -v >/dev/null 2>&1; then \
    echo "Installing Quasar locally..." && npm i -D @quasar/app-vite quasar vue; \
  fi; \
  npx quasar dev -m spa --host 0.0.0.0 --port 8080'