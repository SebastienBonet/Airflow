from airflow import DAG
from airflow.decorators import task
from datetime import datetime
import pprint

with DAG('single_map-download-ctx', start_date=datetime(2023, 4, 8), schedule_interval='@daily', catchup=False) as dag:

    @task
    def download_url(url: str):
        import requests
        response = requests.get(url)
        content = response.content.decode('utf-8')
        lines = content.splitlines()
        return (lines)

    @task
    def print_content(content):
        for file in content:
            print('---------------FILE-------------------')
            print(file)
            print('---------------------------------------')

    files = download_url.expand(url=[
        "https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv",
        "https://people.sc.fsu.edu/~jburkardt/data/csv/grades.csv",
        "https://people.sc.fsu.edu/~jburkardt/data/csv/taxables.csv"
    ])
    print_content(files)