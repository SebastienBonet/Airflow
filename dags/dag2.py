from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.timetables.events import EventsTimetable
import time, pendulum

def hello_world():
    print("#############################################")
    print("  Hello, MYSELF!")
    print((datetime.now()+timedelta(hours=2)).strftime("%y-%m-%d %H:%M:%S"))
    print("#############################################")
    time.sleep(5)

# Define the DAG
dag = DAG(
    'hello_world_schedule_dag_pendulum',
    description='A simple DAG that prints Hello, World! according to a pendulum schedule',
    start_date = datetime(2021,5,28),
    schedule=EventsTimetable(
        event_dates=[
            pendulum.datetime(2023, 6, 1, 12, 50, 5, tz="Europe/Paris"),
            pendulum.datetime(2023, 6, 1, 12, 50, 30, tz="Europe/Paris"),
            pendulum.datetime(2023, 6, 1, 12, 50, 59, tz="Europe/Paris")
        ],
        description="my pendulum schedule",
        restrict_to_events=False,
    ),
    catchup=False
)

# Define the task
hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=hello_world,
    dag=dag
)

# Set the task dependencies
hello_task