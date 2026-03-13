from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import time


def test_task():
    time.sleep(10)
    print("Hello Airflow")



with DAG(
    dag_id="sample_dag2",
    schedule="@daily",
    start_date=datetime(2024,1,1),
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="task1",
        python_callable=test_task
    )

    # wait_for_file >> run_glue_job
    task1