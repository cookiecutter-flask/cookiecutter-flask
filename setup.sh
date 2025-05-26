#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------
# Bootstrap script executed by the devcontainer's postCreate step.
# Mirrors container setup when run locally.
# -------------------------------------------------------------
set -euo pipefail

printf "\n🔧  Setting up PromptYoSelf development environment…\n\n"

# 1. System-level dependencies -------------------------------------------------
if [ "$(id -u)" = "0" ]; then
  # We are root (inside postCreate). Install minimal build tools + sqlite.
  apt-get update -y && \
  apt-get install -y --no-install-recommends \
    build-essential \
    sqlite3 libsqlite3-dev \
    curl ca-certificates && \
  apt-get clean && rm -rf /var/lib/apt/lists/*;
fi

# 2. Python tooling ------------------------------------------------------------
python -m pip install --upgrade pip

# 3. Project dependencies ------------------------------------------------------
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
fi
if [ -f "requirements-dev.txt" ]; then
  pip install -r requirements-dev.txt
fi

# 4. Environment variables for Flask ------------------------------------------
export FLASK_APP="app:create_app"
export FLASK_ENV=${FLASK_ENV:-development}
export DATABASE_URL=${DATABASE_URL:-sqlite:///instance/dev.sqlite3}

# 5. Database initialization ---------------------------------------------------
mkdir -p instance
if command -v flask >/dev/null 2>&1; then
  echo "📜  Running database migrations…"
  flask db upgrade || echo "⚠️  Alembic not configured yet – skipping upgrade"
fi

# 6. Smoke tests ---------------------------------------------------------------
if command -v pytest >/dev/null 2>&1; then
  echo "🧪  Running test suite (quiet)…"
  pytest -q || echo "⚠️  Tests failed – investigate before pushing commits"
fi

printf "\n✅  Setup complete.\n"