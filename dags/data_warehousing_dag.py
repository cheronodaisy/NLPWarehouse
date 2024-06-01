from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello, world!")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG(
    'data_warehousing_dag',
    default_args=default_args,
    description='A simple data warehousing DAG',
    schedule_interval='@daily',
)

start_task = DummyOperator(
    task_id='start',
    dag=dag,
)

hello_world_task = PythonOperator(
    task_id='hello_world',
    python_callable=hello_world,
    dag=dag,
)

start_task >> hello_world_task
 