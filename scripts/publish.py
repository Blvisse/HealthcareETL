'''
This script publishes data into our pub/sub topic


'''

#import necessary libraries
try:
    import os
    import time
    import json
    import pandas as pd
    from google.cloud import pubsub_v1
    from google.oauth2 import service_account
    
    print("Loaded libraries")
    
    
except ImportError as ie:
    
    print(ie)
    print("Error importing {} ".format(ie.name))
    print("/n")
    print("To fix this we recommend running --pip install {} ".format(ie.name))
    exit(1)
    
#create a function to push the data

def pushData(data: pd.DataFrame, projectId: str,pubsub_topic: str):
    '''
    This function takes in a DataFrame and pushes data to the pub/sub topic
    
    Args:
        data ,pd.DataFrame: Pandas DataFrame to publish to 
        projectId, Str: The name of the projectId
        
    Returns:
        Null
    
    '''
    
    pubsub_topic="projects/" + projectId + "/topics/" + pubsub_topic 
    
    print("Establishing script to publish data to  {} ".format(pubsub_topic))
    
    
    #define our credentials
    print("Reading service account details")
    #direct the path to where the service account details have been stored 
    credentials_path="../keys/account.json"
    
    print(credentials_path)
    
    #Set environmental variable for our authentication 
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
    
    #initialize cloud client connection
    
    publisher=pubsub_v1.PublisherClient.from_service_account_file(credentials_path)
    
    print(pubsub_topic)
    print("projects/dtc-dataeng2/topics/healthdata")
    
    #publish data to into the topic
    publisher.publish(pubsub_topic,data)
    
    
    
if __name__ == "__main__":
    print("Accessing publishing script")
    print("Establishing data path ")
    try:
        print("Accessing data ... ")
        data=pd.read_csv("../data/healthcare/train_data.csv")
        
        print(data.head())
        
        print("Loaded data into memory ... ")
    except FileNotFoundError as fnfe:
        print("The file you are looking for can not be found in the specified path")
        exit(1)
        
    project_id="dtc-dataeng2"
    pubsup_topic="healthdata"
    
    print("Converting data to json")
    data_json=data[:1000].to_json()
    
    print("Parsing JSON data")
    parsed=json.loads(data_json)
    dumped_data=json.dumps(parsed).encode("utf-8")
    testdata = """{'order_id': '84c538fa-ef6f-11ea-a9c3-3db3abcedca9', 'timestamp': 1599307283.61477, 'ordered_item': [{'item_name': 'Sample Product Trolly', 'item_id': '1001', 'category_name': 'sample category 1', 'item_price': 189.99, 'item_qty': 1}, {'item_name': 'Sample Product Mystery Box', 'item_id': '1002', 'category_name': 'sample category 2', 'item_price': 47.0, 'item_qty': 3}, {'item_name': 'Sample Product Gift Bag', 'item_id': '1003', 'category_name': 'sample category 3', 'item_price': 23.19, 'item_qty': 5}, {'item_name': 'Sample Product Small Block', 'item_id': '1004', 'category_name': 'sample category 4', 'item_price': 44.99, 'item_qty': 1}, {'item_name': 'Sample Product Cardboard Box', 'item_id': '1005', 'category_name': 'sample category 5', 'item_price': 64.59, 'item_qty': 5}]}"""
    testdata = str.encode(testdata)
    pushData(testdata,project_id,pubsup_topic)
    
    