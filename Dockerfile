# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install requirements
ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm requirements.txt

COPY Dockerfile ./.env* ./

# Copy aaplication codebase
WORKDIR /app
COPY project .
