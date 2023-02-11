'''
This script, creates a data pipeline using Apache Beam and runs it on DataFlow

'''

from beam_nuggets.io import relational_db
import apache_beam as beam
import json
#set up variables

# subscriber=

#service acoount detials
credentials="../keys/accounts.json"

def run_beam(table_name: str, dataset_name: str, project_name: str, subscriber_name:str):
    
    arg=[project_name,]
    pipe=beam.Pipeline()
    
    #write table to Bigquery
    main_pipeline=(pipe
                   
    | "Read data from pub sub"
    >> beam.io.ReadFromPubSub(subscrIption=subscriber_name)
    |"Writing data to db"
    >>beam.io.WriteToBigQuery(table=table_name,dataset=dataset_name,
    create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED)
    
    )
    
    result=pipe.run()
    result.wait_until_finish()