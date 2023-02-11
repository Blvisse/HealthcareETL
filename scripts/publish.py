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
    from concurrent import futures
    
    print("Loaded libraries")
    
    
except ImportError as ie:
    
    print(ie)
    print("Error importing {} ".format(ie.name))
    print("/n")
    print("To fix this we recommend running --pip install {} ".format(ie.name))
    exit(1)
    
#create a function to push the data

credentials_path="../keys/account.json"
    
print(credentials_path)
    
#Set environmental variable for our authentication 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

# project_id="dtc-dataeng2"
# topic_id="healthdata"
    
# publisher = pubsub_v1.PublisherClient()
# topic_path = publisher.topic_path(project_id, topic_id)
# publish_futures = []

def get_callback(
    publish_future: pubsub_v1.publisher.futures.Future, data: str
): 
    def callback(publish_future: pubsub_v1.publisher.futures.Future) -> None:
        try:
            # Wait 60 seconds for the publish call to succeed.
            print(publish_future.result(timeout=60))
        except futures.TimeoutError:
            print(f"Publishing {data} timed out.")

    return callback

# for i in range(10):
#     data = str(i)
    # When you publish a message, the client returns a future.
# testdata = """{'orders_id': '84c538fa-ef6f-11ea-a9c3-3db3abcedca9', 'timestamp': 1599307283.61477, 'ordered_item': [{'item_name': 'Sample Product Trolly', 'item_id': '1001', 'category_name': 'sample category 1', 'item_price': 189.99, 'item_qty': 1}, {'item_name': 'Sample Product Mystery Box', 'item_id': '1002', 'category_name': 'sample category 2', 'item_price': 47.0, 'item_qty': 3}, {'item_name': 'Sample Product Gift Bag', 'item_id': '1003', 'category_name': 'sample category 3', 'item_price': 23.19, 'item_qty': 5}, {'item_name': 'Sample Product Small Block', 'item_id': '1004', 'category_name': 'sample category 4', 'item_price': 44.99, 'item_qty': 1}, {'item_name': 'Sample Product Cardboard Box', 'item_id': '1005', 'category_name': 'sample category 5', 'item_price': 64.59, 'item_qty': 5}]}"""
# testdata = str.encode(testdata)
# publish_future = publisher.publish(topic_path, testdata)
#     # Non-blocking. Publish failures are handled in the callback function.
# publish_future.add_done_callback(get_callback(publish_future, testdata))
# publish_futures.append(publish_future)

# # Wait for all the publish futures to resolve before exiting.
# futures.wait(publish_futures, return_when=futures.ALL_COMPLETED)

# print(f"Published messages with error handler to {topic_path}.")

def pushData(publish_future: pubsub_v1.publisher.futures.Future, data: pd.DataFrame, projectId: str,pubsub_topic: str):
    '''
    This function takes in a DataFrame and pushes data to the pub/sub topic
    
    Args:
        data ,pd.DataFrame: Pandas DataFrame to publish to 
        projectId, Str: The name of the projectId
        
    Returns:
        Null
    
    '''
    #define our credentials
    print("Reading service account details")
    #direct the path to where the service account details have been stored 

        
    credentials_path="../keys/account.json"
    
    print(credentials_path)
    
    #Set environmental variable for our authentication 
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path    
    publisher=pubsub_v1.PublisherClient()
   
    # pubsub_topic="projects/" + projectId + "/topics/" + pubsub_topic 
    topic_path=publisher.topic_path(projectId,pubsub_topic)
    print("Establishing script to publish data to  {} ".format(topic_path))
    
    
    

    #initialize cloud client connection
    
    # publisher=pubsub_v1.PublisherClient.from_service_account_file(credentials_path)
    
    print(pubsub_topic)
    
    # def callback(publish_future: pubsub_v1.publisher.futures.Future) -> None:
    
    #publish data to into the topic
    publisher.publish(topic_path,data)
    

    
    
    
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
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
    
    project_id="dtc-dataeng2"
    topic_id="healthdata"
    
    print("Converting data to json")
    data_json=data[:1000].to_json()
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    publish_futures = []
    
    print("Parsing JSON data")
    parsed=json.loads(data_json)
    dumped_data=json.dumps(parsed).encode("utf-8")
    publish_future=publisher.publish(topic_path,dumped_data)
    publish_future.add_done_callback(get_callback(publish_future,dumped_data))
    publish_futures.append(publish_future)
    
    futures.wait(publish_futures,return_when=futures.ALL_COMPLETED)
    print(f"Published messages with error handler to {topic_path}.")
#     testdata = """{'order_id': '84c538fa-ef6f-11ea-a9c3-3db3abcedca9', 'timestamp': 1599307283.61477, 'ordered_item': [{'item_name': 'Sample Product Trolly', 'item_id': '1001', 'category_name': 'sample category 1', 'item_price': 189.99, 'item_qty': 1}, {'item_name': 'Sample Product Mystery Box', 'item_id': '1002', 'category_name': 'sample category 2', 'item_price': 47.0, 'item_qty': 3}, {'item_name': 'Sample Product Gift Bag', 'item_id': '1003', 'category_name': 'sample category 3', 'item_price': 23.19, 'item_qty': 5}, {'item_name': 'Sample Product Small Block', 'item_id': '1004', 'category_name': 'sample category 4', 'item_price': 44.99, 'item_qty': 1}, {'item_name': 'Sample Product Cardboard Box', 'item_id': '1005', 'category_name': 'sample category 5', 'item_price': 64.59, 'item_qty': 5}]}"""
#     testdata = str.encode(testdata)
#     pushData(testdata,project_id,pubsup_topic)
    
    