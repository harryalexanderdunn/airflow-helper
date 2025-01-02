# Airflow Helper

This is a starter code template, with helper code. The code here is to help you set up you own repo, not to be used as a repo itself. This code is to help you get started with initialising a local aiflow instance. A local airflow instance is useful for testing and debugging your airflow code. However, it should not be used for production deployments.

If you are using windows you will need to first install WSL2 and get your WSL instance setup.

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

`project-setup` will do the project specific installation:

* Setup virtual environment and install libraries from requirements-dev.txt
* Install project specific python package
* Create .env file

**You are now ready to spin up an airflow instance** 🚀 see [docs/airflow_setup](docs/airflow_setup.md) for more details