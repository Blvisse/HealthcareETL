# HealthcareETL
A healthcare data engineering pipeline for healthcare data-analysis

Data Used can be found here [data]

# GCP

## Create a Service Account for our Pub/Sub service

Create a service account with Pub/Sub Admin privileges add a JSON file key and store it to the keys folder


## Create a Pub/Sub Topic

:warning ensure you have anabled the pub/sub topic before

Head over to the Pub/Sub panel and create a topic, giving it a name and description.

[data]: https://www.kaggle.com/datasets/nehaprabhavalkar/av-healthcare-analytics-ii?resource=download

## Create a front end UI using dash

Some resources can be found below: 

1. [article]
2. [github_code]
3. [table_doc]
4. [input_documentation]

You can find a rough template of the one used in the 

```
sites 
```
folder.

To run it, simply navigate to the site folder and type the following code snippet.

```
python app.py
```
This will launch a local server with the entrypoint being ht web app created in app.py

to access them open your browser and go to 

```
http://localhost:8050/

```


[article]:https://towardsdatascience.com/web-development-with-python-dash-complete-tutorial-6716186e09b3
[github_code]:https://github.com/mdipietro09/App_Wedding/blob/master/dash_app.py
[table_doc]: https://dash.plotly.com/datatable/editable
[input_documentation]: https://dash.plotly.com/dash-core-components/input

## Create a BigQuery Dataset 
You need a bigquery dataset to store the data sent from the website and the pub/sub topic.

Navigate to your GCP console and create a BigQuery Dataset, then run the 

```
schema.py
```

File to first create a schema 