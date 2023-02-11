'''
This python script creates a data schema in BigQuery
'''

try:
    import pandas as pd
    import os
    from google.cloud import bigquery
    from pathlib import Path
    import time
    from google.cloud.bigquery import SchemaField
    print("Successfully imported libraries")

except ImportError as ie:
    print ("Couldn't import {}'".format(ie.name))
    print("Run pip install {} ".format(ie.name))


#variables
credentials_path="../keys/bigquery.json"
    
print(credentials_path)
    
#Set environmental variable for our authentication 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

project_id = 'dtc-dataeng2'
dataset_id=   'pub_sub_staging' 

#initialize python BigQuery Client
client = bigquery.Client()

def table_reference(project_id: str, dataset_id: str,table_id):
    dataset_ref=bigquery.DatasetReference(project_id, dataset_id)
    table_reference=bigquery.TableReference(dataset_ref,table_id)
    
    return table_reference

def create_schema():
    schema=[SchemaField("case_id","INTEGER",mode="NULLABLE"),
            SchemaField("Hospital_code","INTEGER",mode="NULLABLE"),
            SchemaField("city_Code_Hospital","INTEGER",mode="NULLABLE"),
            SchemaField("Hospital_region_code","STRING",mode="NULLABLE"),
            SchemaField("Available_Extra_Rooms","INTEGER",mode="NULLABLE"),
            SchemaField("Department","STRING"),
            SchemaField("Ward_Type","STRING"),
            SchemaField("Ward_Facility_Code","STRING"),
            SchemaField("Bed_Grade","STRING"),
            SchemaField("patientid","INTEGER"),
            SchemaField("City_Code_Patient","STRING"),
            SchemaField("Type_of_Admission","STRING"),
            SchemaField("Severity_of_Illness","STRING"),
            SchemaField("Visitors_with_Patient","INTEGER"),
            SchemaField("Age","STRING"),
            SchemaField("Admission_Deposit","STRING"),
            SchemaField("Stay","STRING")]
    return schema

#job configuration
table=bigquery.Table(table_reference(project_id, dataset_id,"cleaned_data"),schema=create_schema())
table=client.create_table(table)
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)
# job_config =bigquery.LoadJobConfig()
# job_config.schema = create_schema()
# job_config.write_disposition='WRITE_TRUNCATE'
# job_config.autodetect=False
# job=client.create_job(table_reference(project_id, dataset_id,"cleaned_data"),job_config)
# print(job.result)



    
    