# Development Container vs Docker

I have found that the best 2 ways to run/setup an airflow instance are with Development Containers (Dev Containers) or Docker. With the docker solution offering more flexibility and control and the Dev Containers solution offering simplicity.

I have found the docker solution to be more useful, mostly because I have paired it with justfile commands to make the process simple and with lazydocker I can fully understand how my instance is running and all the errors associated with it. However, the dev container method does give you a clean repo and is also easy to maintain. The choice is personal preference. This repo contains code for both solutions and I have documented the process below.

I have also written an article on the topic [here](https://medium.com/@harryalexdunn/deploying-airflow-locally-on-wsl2-with-docker-and-just-60f1bf95c8bd)

## Running airflow with a Development Container

The project contains a configuration files for Visual Studio Code Development Containers in the `.devcontainer/` directory. To run the project with this locally, follow the below steps:

1. With the project open in VSCode open the folder in the development container by clicking the prompt in the bottom right corner or running "Reopen in Container" command via Command Palette (usually accessible with Ctrl+Shift+P).
2. First time starting the containers can be slow due to building the docker images, after it has opened validate it is working by navigating to localhost:8080 in your browser to find the airflow log in page (default username and password is 'airflow').

### Customising the Development Container

Common changes you may wish to make:

- Any additional pip requirements you have can be added to `requirements.txt` or `requirements-dev.txt`.
- In the `.devcontainer/docker-compose.yml` file:
   - Set `PYTHON_VARIANT` variable to the version of python you wish to use e.g. '3.10'
   - Set `AIRFLOW_VERSION` variable to the version of airflow you wish to use e.g. '2.4.2'.
   - Set `GOOGLE_CLOUD_PROJECT` variable to GCP project you are using.
   - Add any additional airflow providers to `AIRFLOW_PROVIDERS`.
- In the `.devcontainer/.env` file (available after building container for first time):
    - Update `GCP_CREDENTIALS_LOCAL` to point at different location for a GCP credential file.

After making any of the above changes you will need to rebuid the container by running "Rebuild Container" command via Command Palette (usually accessible with Ctrl+Shift+P).

## Running Airflow with DOcker

To run airflow using Docker, instead Run `local-airflow` to create a local airflow instance for local testing.

Large airflow instance with redis, workers, triggerer, scheduler, postgres and webserer
```bash
just local-airflow
```
small airflow instance with postgres and webserver
```bash
just local-airflow-lite
```

To shutdown the airflow instance run
```bash
just destroy-airflow
```
or
```bash
just destroy-airflow-lite
```

The just file also has extra commands for docker & installation
```bash
# Docker commands
just clean-docker-containers
just force-remove-docker-containers
just show-running-containers
just show-all-containers

# Install requirements.txt on Virtual Environment
just install-libraries
just uninstall-libraries
```

## Automated testing

- In `docs/automation/data_dictionary` Edit line 56 to link to production datasets for data dictionary creation
- In justfile update-unit-test-docs section & update-python-docs add any folders or python scripts that you would like to be documented by lazydocs

- Run `just update-docs` to update all docs (python, unit tests, data dictonaries)

- Specific tests can be run using `just update-python-docs` `update-unit-test-docs` `update-data-dictionary-docs`

