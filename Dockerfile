FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    NODE_VERSION=20

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        postgresql-client \
        curl \
    && curl -fsSL https://deb.nodesource.com/setup_${NODE_VERSION}.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install debugpy

COPY . .
WORKDIR /app/annotation_tool

WORKDIR /app/annotation_tool/frontend
RUN rm -rf node_modules package-lock.json \
    && npm cache clean --force \
    && npm install \
    && npm rebuild
RUN npm run build

# RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
#     DEBIAN_FRONTEND=noninteractive apt-get install -y mailutils postfix && \
#     postconf -e "myhostname = yourdomain.com" && \
#     postconf -e "mydestination = yourdomain.com, localhost.localdomain, localhost"

WORKDIR /app/annotation_tool
