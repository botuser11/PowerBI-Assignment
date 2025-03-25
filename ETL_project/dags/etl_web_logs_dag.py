from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '/home/craig/w3c')  # Adjust path to where log_processing.py is

from scripts.log_processing import load_data_to_postgres

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'ETL_WebLogs_To_Postgres',
    default_args=default_args,
    description='ETL Web Logs Pipeline to PostgreSQL',
    schedule_interval='@daily',
    start_date=datetime(2023, 3, 1),
    catchup=False,
)

task_process_logs = PythonOperator(
    task_id='process_logs_and_load_postgres',
    python_callable=load_data_to_postgres,
    dag=dag,
)

task_process_logs
