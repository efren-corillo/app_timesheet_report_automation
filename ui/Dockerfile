# ui/Dockerfile
# Quasar (Vue 3) dev server. For prod, see "build" stage notes below.

FROM node:20-alpine AS base
WORKDIR /app

# Faster installs & reproducibility
ENV CI=1
RUN corepack enable

# Install dependencies first (cacheable)
COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* ./
# Choose one package manager; here we use yarn if present, else npm
RUN if [ -f yarn.lock ]; then yarn install --frozen-lockfile; \
    elif [ -f pnpm-lock.yaml ]; then corepack prepare pnpm@latest --activate && pnpm install --frozen-lockfile; \
    else npm ci; fi

# Copy source
COPY . .

# Expose Quasar dev server
EXPOSE 8080

# Dev command (edit if your script name differs)
# Quasar CLI usually: "quasar dev" or "yarn dev"
CMD if [ -f yarn.lock ]; then \
      yarn dev -H 0.0.0.0 -p 8080; \
    elif [ -f pnpm-lock.yaml ]; then \
      pnpm dev --host 0.0.0.0 --port 8080; \
    else \
      npm run dev -- --host 0.0.0.0 --port 8080; \
    fi

# -------- Production build example (optional) --------
# FROM base AS build
# RUN if [ -f yarn.lock ]; then yarn build; \
#     elif [ -f pnpm-lock.yaml ]; then pnpm build; \
#     else npm run build; fi
#
# # Then either:
# # 1) copy dist/ into a Caddy image and serve static files, or
# # 2) keep your reverse-proxy to the dev server in compose for local only
