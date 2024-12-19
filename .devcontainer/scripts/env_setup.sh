#!/bin/bash

# Set the default .env file for the container

env_file=.devcontainer/.env
if [ ! -e $env_file ]; then
    # File doesn't exist so create an empty one
    touch $env_file
    echo "INFO: Created $env_file file"
fi
if ! grep -q ^LOCAL_UID= "$env_file"; then
    # UID to set remote user to
    echo LOCAL_UID=$(id -u) >> $env_file
    echo "INFO: Added missing LOCAL_UID variable to $env_file"
fi
if ! grep -q ^WORKSPACE_NAME= "$env_file"; then
    # Workspace name passed as parameter
    echo WORKSPACE_NAME=$1 >> $env_file
    echo "INFO: Added missing WORKSPACE_NAME variable to $env_file"
fi
if ! grep -q ^GCP_CREDENTIALS_LOCAL= "$env_file"; then
    # Workspace name passed as parameter
    echo GCP_CREDENTIALS_LOCAL=~/.config/gcloud/application_default_credentials.json >> $env_file
    echo "INFO: Added missing GCP_CREDENTIALS_LOCAL variable to $env_file"
fi
