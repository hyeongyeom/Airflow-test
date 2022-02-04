import logging
from airflow import DAG
from airflow.decorators import task
from airflow.models import Variable
from datetime import datetime


@task
def variable_set():
    Variable.set(
        key="ssh_secret", value={
        "desktop": "sshpass -p 1111 ssh -tt -p 0000 user1@example.iptime.org -o StrictHostKeyChecking=no",
        "laptop": "sshpass -p 111 ssh -tt -p 0000 user1@example.iptime.org -o StrictHostKeyChecking=no"
    }, 
    serialize_json=True
    )

@task
def variable_get():
    logging.info(Variable.get(key="ssh_secret", deserialize_json=True))
with DAG(
    "variable_setting",
    start_date=datetime(2021, 10, 6),
    schedule_interval=None,
    catchup=False,
) as dag:
    variable_set() >> variable_get()