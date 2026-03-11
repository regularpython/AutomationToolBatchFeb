from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from datetime import datetime
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.operators.python import PythonOperator
import time
def test_task():
    1/0
    time.sleep(10)
    print("Hello Airflow")



with DAG(
    dag_id="run_glue_job_dag",
    start_date=datetime(2024,1,1),
    schedule_interval=None,
    catchup=False
) as dag:
    # Step 1: Wait for file in S3
    # wait_for_file = S3KeySensor(
    #     task_id="wait_for_file_upload",
    #     bucket_name="real-estate-dsr-2",
    #     bucket_key="test/movies.csv",
    #     aws_conn_id="aws_default",
    #     poke_interval=30,
    #     timeout=60 * 60,
    # )

    # run_glue_job = GlueJobOperator(
    #     task_id="run_glue_job",
    #     job_name="gittest",   # AWS Glue Job Name
    #     region_name="us-east-1",
    #     aws_conn_id="aws_default"
    # )

    task1 = PythonOperator(
        task_id="task1",
        python_callable=test_task
    )

    # wait_for_file >> run_glue_job
    task1