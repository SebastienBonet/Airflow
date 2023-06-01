from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import time


def hello_world(task_id):
    print("#############################################")
    print(f"  Hello from TASK : {task_id}")
    print((datetime.now()+timedelta(hours=2)).strftime("%y-%m-%d %H:%M:%S"))
    print("#############################################")
    time.sleep(5)

# Define the DAG
dag = DAG(
    'hello_world_AB',
    description='Lilou Dallas Moulti Task',
    start_date = datetime(2023,5,31),
    schedule_interval = timedelta(seconds=10),
    end_date=datetime(2023, 6, 1, hour=10, minute=5),
    catchup=False
)

# Define the task
_task_id='hello_task_A'
hello_task_A = PythonOperator(
    task_id=_task_id,
    python_callable=hello_world,
    op_args=[_task_id],
    dag=dag
)

# Define the task
_task_id='hello_task_B'
hello_task_B = PythonOperator(
    task_id=_task_id,
    python_callable=hello_world,
    op_args=[_task_id],
    dag=dag
)

# Set the task dependencies
hello_task_A >> hello_task_B