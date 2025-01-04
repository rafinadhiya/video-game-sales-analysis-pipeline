'''
Name : Rafina Dhiya Pradani
Objective : This pipeline automates the ETL (Extract, Transform, Load) process from a PostgreSQL database to Elasticsearch using Apache Airflow.

The pipeline involves three main steps:
1. Fetch raw data from PostgreSQL.
2. Clean the data by removing duplicates and handling missing values.
3. Upload the cleaned data to Elasticsearch for further analysis.

The pipeline is scheduled to run every Saturday at 09:10, 09:20, and 09:30 WIB.
'''

# import libraries
import pandas as pd
from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch
import pendulum

# default parameter
localtz=pendulum.timezone("Asia/Jakarta")
default_args = {
    'owner' : 'afi',
    'depends_on_past' : False,
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries': 1,
    'start_date':localtz.datetime(2024, 11, 1)
}

def get_data(**context):
    '''
    Function to fetch raw data from PostgreSQL and save it as a temporary CSV file.
    
    - Fetches data from the `table_m3` table.
    - Saves the data as a CSV file in `/tmp/raw_data.csv`.
    - Pushes the file path to XCom for use in the next task.
    '''
    # create connection
    source_hook = PostgresHook(postgres_conn_id='Airflow')
    source_conn = source_hook.get_conn()
    source_cursor = source_conn.cursor()

    # read in pandas
    data_raw = pd.read_sql('SELECT * FROM table_m3', source_conn)
    
    # Save DataFrame to temporary csv
    temp_file = '/tmp/raw_data.csv'
    data_raw.to_csv(temp_file, index=False)

    # Push file path to XCom
    context['ti'].xcom_push(key='raw_data_path', value=temp_file)

def cleaning(**context):
    '''
    Function to clean raw data:
    - Converts column names to lowercase.
    - Removes duplicate rows.
    - Handles missing values: numeric columns are filled with the median, non-numeric columns are filled with 'Unknown'.
    - Converts the `year` column to integer if it exists.
    - Saves the cleaned data as a temporary CSV file.
    '''
    # Get task instance
    ti = context['ti']
    
    # Get raw data path
    temp_file = ti.xcom_pull(task_ids='get_data', key='raw_data_path')

    # Transform to dataframe
    data_raw = pd.read_csv(temp_file)

    # Lowercase all column names
    data_raw.columns = data_raw.columns.str.lower()

    # Rename 'rank' column to 'unique_id'
    data_raw.rename(columns={"rank": "unique_id"}, inplace=True)
    
    # Remove duplicates
    data_clean = data_raw.drop_duplicates()

    # Handle missing values
    for column in data_clean.columns:
        if data_clean[column].dtype in ['float64', 'int64']:
            # Fill missing numeric values with median
            data_clean[column].fillna(data_clean[column].median(), inplace=True)
        else:
            # Fill missing non-numeric values with 'Unknown'
            data_clean[column].fillna('Unknown', inplace=True)

    # Convert year column to integer
    if 'year' in data_clean.columns:
        data_clean['year'] = pd.to_numeric(data_clean['year'], errors='coerce').astype('Int64')

    # Save cleaned data to temporary CSV
    clean_data_path = '/tmp/clean_data.csv'
    data_clean.to_csv(clean_data_path, index=False)

    # Push cleaned file path to XCom
    ti.xcom_push(key='clean_data_path', value=clean_data_path)
    print("Data cleaned and saved to:", clean_data_path)

def upload_elastic(**context):
    '''
    Function to upload cleaned data to Elasticsearch:
    - Reads the cleaned CSV file from the temporary directory.
    - Converts each row into JSON format.
    - Uploads the data to Elasticsearch with the index `m3_afi`.
    '''
    # get task instance
    ti = context['ti']
    
    # get raw data path
    temp_file = ti.xcom_pull(task_ids='cleaning', key='clean_data_path')

    # read clean data path
    data_clean = pd.read_csv(temp_file)

    # Initialize Elasticsearch
    es = Elasticsearch('http://elasticsearch:9200')
    
    # ingest data : Upload data to Elasticsearch
    for i, row in data_clean.iterrows():
        
        doc = row.to_json()

        res = es.index(index='m3_afi', doc_type='doc', body=doc)

# DAG definition
with DAG(
    'm3_afi',
    description = 'Pipeline sederhana',
    schedule_interval = '10,20,30 9 * * 6',
    default_args=default_args,
    catchup=False) as dag:

    # task 1 : Fetch data 
    get = PythonOperator(
        task_id = 'get_data',
        python_callable = get_data,
        provide_context = True
    )

    # task 2 : Clean data
    clean  = PythonOperator(
        task_id = 'cleaning',
        python_callable = cleaning,
        provide_context = True
    )
    
    # task 3 : Upload to Elasticsearch
    upload = PythonOperator(
        task_id = 'upload_elastic',
        python_callable = upload_elastic,
        provide_context=True
    )

# Define task dependencies
get >> clean >> upload