import mysql.connector
from datetime import datetime
from plugins.utils.config import (
    MYSQL_HOST,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_DATABASE
)


class MySQLHook:

    @staticmethod
    def insert_log(dag_id, task_id, run_id, state, execution_date):

        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )

        cursor = connection.cursor()

        query = """
        INSERT INTO task_execution_logs
        (dag_id, task_id, run_id, state, execution_date, log_time)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                dag_id,
                task_id,
                run_id,
                state,
                execution_date,
                datetime.now()
            )
        )

        connection.commit()

        cursor.close()
        connection.close()