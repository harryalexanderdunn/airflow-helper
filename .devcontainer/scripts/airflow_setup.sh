#!/bin/bash

function ver() {
    printf "%04d%04d%04d%04d" ${1//./ }
}
airflow_version=$(ver $(airflow version))

echo "INFO: Initialising airflow db"
if ((airflow_version < $(ver "2.7.0"))); then
    airflow db init
else
    airflow db migrate
fi

echo "INFO: Creating admin user"
airflow users create \
       --username "airflow" \
       --firstname "Airflow" \
       --lastname "Admin" \
       --email "airflowadmin@example.com" \
       --role "Admin" \
       --password "airflow"

echo "INFO: Creating default airflow connections"
python .devcontainer/scripts/add_airflow_connections.py
