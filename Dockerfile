FROM apache/airflow:2.1.3
RUN apt update && apt install sshpass