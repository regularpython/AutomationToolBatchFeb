import boto3
from datetime import datetime
from plugins.utils.config import (
    AWS_REGION,
    SNS_TOPIC_ARN
)


class SNSHook:

    @staticmethod
    def send_notification(dag_id, task_id, run_id, state, execution_date):

        sns_client = boto3.client("sns", region_name=AWS_REGION)

        message = f"""
Airflow Task Alert

DAG ID: {dag_id}
Task ID: {task_id}
Run ID: {run_id}
State: {state}
Execution Date: {execution_date}
Time: {datetime.now()}
"""

        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=f"Airflow Task {state}",
            Message=message
        )