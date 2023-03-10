FROM python:3.9-alpine
LABEL maintainer="Marcio Woitek"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [[ "$DEV" == "true" ]]; then \
        /py/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    addgroup -g 1000 django && \
    adduser -u 1000 -D -H -S -G django django-user

ENV PATH="/py/bin:$PATH"

USER django-user
