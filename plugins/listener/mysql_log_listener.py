from airflow.listeners import hookimpl
from plugins.hooks.mysql_hook import MySQLHook
from plugins.hooks.sns_hook import SNSHook


class TaskExecutionListener:

    def process_event(self, task_instance, state):

        dag_id = task_instance.dag_id
        task_id = task_instance.task_id
        run_id = task_instance.run_id
        execution_date = task_instance.execution_date

        MySQLHook.insert_log(
            dag_id,
            task_id,
            run_id,
            state,
            execution_date
        )

        SNSHook.send_notification(
            dag_id,
            task_id,
            run_id,
            state,
            execution_date
        )

    @hookimpl
    def on_task_instance_success(self, previous_state, task_instance, session):

        self.process_event(task_instance, "SUCCESS")

    @hookimpl
    def on_task_instance_failed(self, previous_state, task_instance, session):

        self.process_event(task_instance, "FAILED")