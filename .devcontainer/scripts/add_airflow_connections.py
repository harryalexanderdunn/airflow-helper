"""Script to setup default GCP connections."""

from __future__ import annotations

import json
import logging
import os

from airflow import settings
from airflow.models import Connection

GCP_PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]

CONNECTIONS = [
    {
        "conn_id": "bigquery_default",
        "conn_type": "google_cloud_platform",
        "extra": json.dumps({"extra__google_cloud_platform__project": GCP_PROJECT}),
    },
    {
        "conn_id": "google_cloud_default",
        "conn_type": "google_cloud_platform",
        "extra": json.dumps({"extra__google_cloud_platform__project": GCP_PROJECT}),
    },
    {
        "conn_id": "google_cloud_datastore_default",
        "conn_type": "google_cloud_platform",
        "extra": json.dumps({"extra__google_cloud_platform__project": GCP_PROJECT}),
    },
    {
        "conn_id": "google_cloud_storage_default",
        "conn_type": "google_cloud_platform",
        "extra": json.dumps({"extra__google_cloud_platform__project": GCP_PROJECT}),
    },
]


def add_connection(conn_config: dict[str, str]) -> Connection:
    """Add connection to the airflow database.

    Args:
        conn_config (Dict[str, str]):
            Dictionary containing connection details.

    Returns:
        Connection: Airflow connection added.
    """
    conn = Connection(
        conn_id=conn_config["conn_id"],
        conn_type=conn_config["conn_type"],
        extra=conn_config["extra"],
    )
    session = settings.Session()

    # Check if connection already exists
    conn_name = (
        session.query(Connection).filter(Connection.conn_id == conn.conn_id).first()
    )
    if str(conn_name) == str(conn.conn_id):
        logging.warning("Connection %s already exists", conn.conn_id)
        return None

    session.add(conn)
    session.commit()

    logging.info("Created connection: %s", conn)
    return conn


for connection in CONNECTIONS:
    add_connection(connection)
