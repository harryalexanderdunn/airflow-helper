# Airflow Helper

This is a starter code template, with helper code. The code here is to help you set up you own repo, not to be used as a repo itself.

## Initial WSL and project setup

1. Make sure you have a working WSL terminal (WSL2).
 * Gitbash installed https://git-scm.com/downloads

2. Clone the [repository](https://github.com/harryalexanderdunn/airflow-helper.git) **to your WSL terminal**.

3. Install just. Just is built using the Rust programming language ([just git repo](https://github.com/casey/just)).
There are installation instructions in the repo. We have found the most success using `cargo`.
You will also need to run `sudo apt install build-essential` this is to ensure you have a C linker installed.
To install cargo you can use [rustup](https://rustup.rs/) to install the rust toolchain (which cargo is a part of).
Once cargo is installed (ensure you follow the last command for setup `. "$HOME/.cargo/env"`) you can run `cargo install just`

4. Either run `just project-setup` or `just full-project-setup`. 
If this is your first time on WSL, `full-project-setup` will: 

* Install all the necessary packages for package manager
* Install Python3
* configure [Application Default Credentials](https://google-auth.readthedocs.io/en/latest/reference/google.auth.html#google.auth.default)
* Initialise SDK environment
* Install Docker
* Install Lazydocker
* Setup virtual environment and install libraries from requirements-dev.txt
* Create .env file

project-setup will do the project specific installation:

* Setup virtual environment and install libraries from requirements-dev.txt
* Install project specific python package
* Create .env file


## Running the Development Container

The project contains a configuration files for Visual Studio Code Development Containers in the `.devcontainer/` directory. To run the project with this locally, follow the below steps:

1. With the project open in VSCode open the folder in the development container by clicking the prompt in the bottom right corner or running "Reopen in Container" command via Command Palette (usually accessible with Ctrl+Shift+P).
2. First time starting the containers can be slow due to building the docker images, after it has opened validate it is working by navigating to localhost:8080 in your browser to find the airflow log in page (default username and password is 'airflow').

## Customising the Development Container

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

## Airflow with Docker

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

- The docs folder contains pre-written automated docs from this repo (written using lazydocs). Docs include code docs, unit test docs and code for data dictionary creation.
- In `docs/automation/data_dictionary` Edit line 56 to link to production datasets for data dictionary creation
- In justfile update-unit-test-docs section & update-python-docs add any folders or python scripts that you would like to be documented by lazydocs

- Run `just update-docs` to update all docs (python, unit tests, data dictonaries)

- Specific tests can be run using `just update-python-docs` `update-unit-test-docs` `update-data-dictionary-docs`

