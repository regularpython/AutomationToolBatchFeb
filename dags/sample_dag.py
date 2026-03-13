from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time

# function to execute
def say_hello():
    time.sleep(15)
    print("Hello World from Apache Airflow!")



# define DAG
with DAG(
    dag_id="sample_dag",
    schedule="@daily",
    start_date=datetime(2024,1,1),
    catchup=False
) as dag:

    A = PythonOperator(
        task_id="a",
        python_callable=say_hello
    )

    B = PythonOperator(
        task_id="b",
        python_callable=say_hello
    )

    C = PythonOperator(
        task_id="c",
        python_callable=say_hello
    )

    D = PythonOperator(
        task_id="d",
        python_callable=say_hello
    )

    E = PythonOperator(
        task_id="e",
        python_callable=say_hello
    )

    A >> B
    B >> C
    B >> D
    A >> E