# ================================== BUILDER ===================================
ARG INSTALL_PYTHON_VERSION=${INSTALL_PYTHON_VERSION:-3.12}

FROM python:${INSTALL_PYTHON_VERSION}-slim-bookworm AS builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache --upgrade pip && \
    pip install --no-cache -r requirements.txt

# ================================= PRODUCTION =================================
FROM python:${INSTALL_PYTHON_VERSION}-slim-bookworm as production

WORKDIR /app

# Create non-root user
RUN useradd -m appuser && \
    mkdir -p /app/instance && \
    chown -R appuser:appuser /app
USER appuser
ENV PATH="/home/appuser/.local/bin:${PATH}"

# Copy Python dependencies and install
COPY requirements.txt ./
RUN pip install --no-cache --user -r requirements.txt

# Copy application code
COPY --chown=appuser:appuser . .

# Create instance directory for runtime data
RUN mkdir -p instance

EXPOSE 5000
ENV FLASK_APP=autoapp.py
ENV FLASK_ENV=production
ENV DATABASE_URL=sqlite:///instance/prod.sqlite3

# Use gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "autoapp:app"]


# ================================= DEVELOPMENT ================================
FROM builder AS development

# Install development dependencies
RUN pip install --no-cache -r requirements-dev.txt

# Copy application code
COPY . .

# Create instance directory for development database
RUN mkdir -p instance

EXPOSE 5000
ENV FLASK_APP=autoapp.py
ENV FLASK_ENV=development
ENV DATABASE_URL=sqlite:///instance/dev.sqlite3

# Use Flask development server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--debug"]
