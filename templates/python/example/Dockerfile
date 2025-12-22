# syntax=docker/dockerfile:1
FROM python:3.11-slim as base

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=0

WORKDIR /app

# Install ca-certificates and build tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Use BuildKit secret to inject the CA bundle and update trust store
RUN --mount=type=secret,id=INTERMEDIATE_CA_BUNDLE \
    cp /run/secrets/INTERMEDIATE_CA_BUNDLE /usr/local/share/ca-certificates/internal-ca.crt && \
    update-ca-certificates

COPY pyproject.toml README.md ./
COPY app ./app

# Any pip install commands from here on will trust your internal registry/proxies
RUN pip install --upgrade pip && pip install .

EXPOSE 8000
ENV FLASK_APP=app.main
CMD ["gunicorn", "app.main:app", "--bind", "0.0.0.0:8000"]