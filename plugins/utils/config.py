import os

MYSQL_HOST = os.getenv("MYSQL_HOST", "host.docker.internal")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "root")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "airflow_logs")

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

SNS_TOPIC_ARN = os.getenv(
    "SNS_TOPIC_ARN",
    "arn:aws:sns:us-east-1:339713066136:BatchFebSNS"
)