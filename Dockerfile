FROM python:3.12.1-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apk update && \
    apk add --no-cache python3-dev gcc

ADD ./pyproject.toml /app

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app
COPY ./entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
