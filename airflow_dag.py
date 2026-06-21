from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

# Definisci il DAG
default_args = {
    'owner': 'data_engineer',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='Pipeline ETL automatico',
    schedule_interval='0 2 * * *',  # Ogni notte alle 2:00 AM
    start_date=datetime(2024, 1, 1),
    catchup=False,
)

# Task: Esegui lo script ETL
def run_etl():
    subprocess.run(['python', 'etl_script.py'])

task_etl = PythonOperator(
    task_id='esegui_etl',
    python_callable=run_etl,
    dag=dag,
)

task_etl