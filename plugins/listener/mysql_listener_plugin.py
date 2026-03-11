from airflow.plugins_manager import AirflowPlugin

from listener.mysql_log_listener import TaskExecutionListener



class MySQLLogPlugin(AirflowPlugin):

    name = "mysql_log_plugin"

    listeners = [
        TaskExecutionListener
    ]