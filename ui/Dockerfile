FROM node:20-alpine AS base
WORKDIR /app
ENV CI=1
RUN corepack enable

# 1) Copy only manifests first
COPY package.json ./
COPY yarn.lock* ./
COPY package-lock.json* ./
COPY pnpm-lock.yaml* ./

# 2) Install deps WITHOUT running postinstall scripts
RUN if [ -f yarn.lock ]; then \
      yarn install --frozen-lockfile --ignore-scripts; \
    elif [ -f package-lock.json ]; then \
      npm ci --ignore-scripts; \
    elif [ -f package.json ]; then \
      npm install --ignore-scripts; \
    else \
      echo "No package.json found; skipping install"; \
    fi

# 3) Now copy the rest of the project (this includes quasar.config.*)
COPY . .

# 4) Run prepare now that the config is present (best-effort)
RUN npx quasar prepare || true

EXPOSE 8080
CMD if [ -f yarn.lock ]; then \
      yarn dev -H 0.0.0.0 -p 8080; \
    elif [ -f pnpm-lock.yaml ]; then \
      pnpm dev --host 0.0.0.0 --port 8080; \
    else \
      npm run dev -- --host 0.0.0.0 --port 8080; \
    fi
