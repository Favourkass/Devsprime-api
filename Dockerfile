# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install requirements
WORKDIR /app
ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY Dockerfile ./.env* ./

# Copy aaplication codebase
COPY project .

CMD tail -f /dev/null