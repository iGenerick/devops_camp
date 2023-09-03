# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

ENV AUTHOR "Сергей Андреевич Н."
ENV UUID "0dc82d1c-9958-4fbf-a088-851bd42d61b9"
ENV FLASK_RUN_PORT 8000
ENV FLASK_RUN_HOST 0.0.0.0

ENTRYPOINT ["python3"]
CMD ["webserver.py"]

EXPOSE 8000
