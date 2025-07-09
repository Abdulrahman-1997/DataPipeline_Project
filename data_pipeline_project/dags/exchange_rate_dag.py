# dags/exchange_rate_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

sys.path.append("/opt/airflow/scripts")

from extract import extract_exchange_rates
from transform import transform_exchange_rates
from load import load_to_mongo

default_args = {
    'owner': 'data_engineer',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

def extract_task(**context):
    raw_data = extract_exchange_rates()
    context['ti'].xcom_push(key='raw_data', value=raw_data)

def transform_task(**context):
    raw = context['ti'].xcom_pull(key='raw_data', task_ids='extract')
    transformed = transform_exchange_rates(raw)
    context['ti'].xcom_push(key='transformed_data', value=transformed)

def load_task(**context):
    data = context['ti'].xcom_pull(key='transformed_data', task_ids='transform')
    load_to_mongo(data)

with DAG(
    dag_id='exchange_rate_etl',
    default_args=default_args,
    description='ETL pipeline to extract currency rates and store in MongoDB',
    schedule_interval='@daily',
    start_date=datetime(2025, 7, 7),
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id='extract',
        python_callable=extract_task,
        provide_context=True
    )

    t2 = PythonOperator(
        task_id='transform',
        python_callable=transform_task,
        provide_context=True
    )

    t3 = PythonOperator(
        task_id='load',
        python_callable=load_task,
        provide_context=True
    )

    t1 >> t2 >> t3
