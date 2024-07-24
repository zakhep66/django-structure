FROM python:3.12.1-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apk update && \
    apk add --no-cache python3-dev gcc musl-dev

COPY pyproject.toml poetry.lock* /app/

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

COPY . /app

RUN chmod +x /entrypoint.sh
