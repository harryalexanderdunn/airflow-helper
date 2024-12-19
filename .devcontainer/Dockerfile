# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG PYTHON_VARIANT=3.9
FROM mcr.microsoft.com/devcontainers/python:${PYTHON_VARIANT}

ENV PYTHONUNBUFFERED 1

ARG LOCAL_UID=1000
RUN usermod -u ${LOCAL_UID} vscode && \
    mkdir -p /workspace/airflow/dags && \
    mkdir -p /workspace/.config/gcloud && \
    chown -R vscode:vscode /workspace
USER vscode

COPY --chown=vscode requirements.txt requirements-dev.txt /workspace/tmp/

# Install airflow
ARG AIRFLOW_VERSION=2.4.2
ARG AIRFLOW_PROVIDERS=apache.beam,cncf.kubernetes,dbt.cloud,google,hashicorp,mysql,postgres,sendgrid,ssh
RUN export PYTHON_SHORT_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)" && \
    pip3 --disable-pip-version-check --no-cache-dir install  "apache-airflow[${AIRFLOW_PROVIDERS}]==${AIRFLOW_VERSION}" \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_SHORT_VERSION}.txt" && \
    pip3 --disable-pip-version-check --no-cache-dir install -r /workspace/tmp/requirements.txt -r /workspace/tmp/requirements-dev.txt
