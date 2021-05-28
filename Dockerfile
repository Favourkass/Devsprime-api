FROM python:3.9.0-alpine as base

# Setup base image with require tools

RUN apk update && apk add \
  bash \
  curl \
  postgresql-dev \
  gcc \
  python3-dev \
  musl-dev 
  
# Add environment variables

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /devsprime

COPY Dockerfile ./.env* ./

COPY ./requirements.txt .

COPY ./project ./project

COPY ./bin/container ./bin

RUN bin/install

# Production Like Environment

FROM base as api-prod

# Huge image size alert !!!
RUN bin/manage collectstatic --clear --noinput
