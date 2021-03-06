from datetime import timedelta
from textwrap import dedent

import pendulum
from datetime import datetime, timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization

"""
-시군구 사이트 중 광역시 데이터 수집 크롤러 작동 및 시트 데이터 전송 명령
-서버컴퓨터에 있는 크롤러 실행


참고(추가셋팅목록)
-에러나면 메일전송(프로덕션)
-TASK 실패시 재실행 ('retries')
-TASK 실패시 재실행 시간간격('retry_delay')
-cron ('schedule_interval')
-시작시간('start_date')
"""

kst = pendulum.timezone("Asia/Seoul")


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['wltnwkd241@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success',
}

with DAG(
    'test',
    default_args=default_args,
    schedule_interval="0 18 * * *",
    start_date=datetime(2021, 8, 22, tzinfo=kst),
) as dag:

    test = BashOperator(
        task_id='test1',
        bash_command='{{ var.json.ssh_secret.desktop}} "d: && cd D:\Desktop\airflow_test\python test.py',
    )

    test