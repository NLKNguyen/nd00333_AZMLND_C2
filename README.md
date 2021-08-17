Operationalizing Machine Learning with Azure
======

# Overview

This project demonstrates the use of Azure ML to operationalize an end-to-end machine learning pipeline from model training to API consuming in production with sufficient monitoring. 

The dataset we use is a marketing campaign that records people who contacted/answered the calls, and we seek to predict a yes/no answer to whether a person is a potential lead in this campaign.

Dataset URL: https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv

First, we use Azure ML Studio interface to register the dataset then create an Automated ML experiment for traing classification models. 

Second, we deploy the best performance model as a prediction web service as a REST API endpoint. We have Application Insights enabled for collecting logs and Swagger specification available for viewing the API documentation. The web service API can be consumed by any standard HTTP client, and we will be using a Python script as an example.

Third, we set up a Pipeline using Azure ML Python SDK in Jupyter Notebook to facilitate a similar worklfow like we have just done previously using web interface, but now it's done programmatically. Therefore, more automation capabilities are available, for example, automaticallly rerun the Pipeline for model retrain whenever there is dataset update or code change. This Pipeline can be integrated nicely to an existing CI/CD (e.g. Azure DevOps) that allows automatic model training and deployment. We can also pick and choose any model that looks better than the previous to deploy a new prediction service endpoint.

Finally, we publish the Pipeline endpoint that is also a REST API but for Pipeline execution. We use Jupyter Notebook to demonstrate a Pipeline trigger to make a new experiment.


## Architectural Diagram

This is an architecture overview of the workflow and the scope of this project.

![image](https://user-images.githubusercontent.com/4667129/129495120-9cd5f844-91c9-419d-b6ef-cc59846ec515.png)

The project includes registering dataset to use with Automated ML to determine the best model for production deployment as a REST API endpoint which will then be consumed by a REST client and also be managed by Python SDK for monitoring. Finally, a pipeline will be set up so that it can be triggered to execute whenever needed in the future.

# Key Steps
 
## Step 0: Resource Provision
### Create Azure Service Principle

![image](https://user-images.githubusercontent.com/4667129/129117771-8e9fdf44-a2f8-434c-bff8-a5d10ef8bb25.png)

Get object Id

![image](https://user-images.githubusercontent.com/4667129/129118657-992a03e9-6a9b-4bdf-8d13-6c9fb2573741.png)


### Share workspace to the newly created account
![image](https://user-images.githubusercontent.com/4667129/129118415-ba4bc243-2efe-4beb-bcb9-a14adca4bd9f.png)


## Step 1: Model Training
### Upload dataset and register

![image](https://user-images.githubusercontent.com/4667129/129119881-c0cf253e-b0a5-42e2-92a8-20a5c7879e5a.png)

![image](https://user-images.githubusercontent.com/4667129/129119850-02de4623-3402-43b2-bc7e-eb477e4b537d.png)

### Use AutoML for finding the best classification model

![image](https://user-images.githubusercontent.com/4667129/129120027-875f0be6-c487-4262-9ffc-370495223e64.png)

![image](https://user-images.githubusercontent.com/4667129/129120128-a730e484-4332-4e30-9db9-e6a9d189de74.png)

![image](https://user-images.githubusercontent.com/4667129/129120152-becff75c-6cd2-45d1-9092-403d3acb2c79.png)


## Step 2: Model Deployment

### Deploy the best model

![image](https://user-images.githubusercontent.com/4667129/129460832-621b4167-aa5c-4bf1-ba47-3a6eeed382eb.png)


## Step 3: Enabled Application Insights

Once the model is deployed, enable Application Insights to collect the service logs and useful metrics for monitoring purposes.

### Set up Python SDK for Azure in local environment

Make virtual environment in the project directory

```powershell
mkdir venv
python -m venv ./venv
```

Activate the virtual environment in current shell session

```powershell
.\venv\Scripts\activate
```

Install Azure Python ML SDK

```powershell
pip install azureml-core
```

Due to an SDK bug that caused `"Could not retrieve user token. Please run 'az login'"`, downgrading PyJWT to get around the issue:

```powershell
python -m pip install --upgrade PyJWT==1.7.1
```

@ref: https://stackoverflow.com/questions/67488064/get-workspace-failed-azuremlsdk-authenticationexception

Check current versions:

```powershell
pip show azure-core
```

```
Name: azure-core
Version: 1.17.0
```


```powershell
pip show PyJWT
```

```
Name: PyJWT
Version: 1.7.1
```

### Enabled Application Insights using Python script

![image](https://user-images.githubusercontent.com/4667129/129120622-c2e842be-4559-48c3-895e-421e0e03e62b.png)

![image](https://user-images.githubusercontent.com/4667129/129120539-27853550-8331-43ea-848a-cc313fc5f425.png)

Preview logs from the local script

![image](https://user-images.githubusercontent.com/4667129/129120654-d88f6ea1-b411-46a6-89ac-722691b53162.png)

## Step 4: View Swagger Documentation

Swagger.json URL for the endpoint is available to download

![image](https://user-images.githubusercontent.com/4667129/129433043-2e63be75-cb0e-493b-8706-4c9ff099183f.png)


Run localhost serving the edownloaded swagger.json that allows CORS for Swagger UI to access

![image](https://user-images.githubusercontent.com/4667129/129433035-1727ea70-70ca-4dd8-b765-20f84d3f8fec.png)

Run Swagger UI

![image](https://user-images.githubusercontent.com/4667129/129433076-f5ab8dbf-f4cd-4c19-9671-653e46a7d63a.png)

Access API documentation from the local swagger.json

![image](https://user-images.githubusercontent.com/4667129/129433082-52e36b54-b028-4dc3-a038-76a78ffdcbc4.png)

## Step 5: Consume Endpoint

Set up endpoint test script with URI with authentication key and sample test data

![image](https://user-images.githubusercontent.com/4667129/129434783-82c120b4-c872-4da2-869b-6542fb408c2f.png)

Test the endpoint

![image](https://user-images.githubusercontent.com/4667129/129434801-843586c9-f5fe-463e-b03a-83db5a26c16e.png)


## Step 6: Pipeline Automation

Using Python SDK in Jupyter Notebook to create a ML pipeline

![image](https://user-images.githubusercontent.com/4667129/129459282-65b3cbd4-d83c-49b1-9b96-bbe30c83d63e.png)

A pipeline endpoint is also created programatically.

![image](https://user-images.githubusercontent.com/4667129/129459356-c4481166-4e05-473a-af95-38c4311c1186.png)

The pipeline steps show the input bank marketing data set and the AutoML model where the model trainings happen. Also, the pipeline REST endpdoint is active for triggers to execute.

![image](https://user-images.githubusercontent.com/4667129/129459490-801dd325-8679-4932-aa55-b71edbe9b0d0.png)

Trigger the endpoint with proper authentication within Jupyter Notebook for a new pipeline execution and use RunDetails widget to show the step runs.

![image](https://user-images.githubusercontent.com/4667129/129459607-d795183f-fa39-4734-9f4b-9ca40abd0029.png)

The scheduled run also shows in ML Studio.

![image](https://user-images.githubusercontent.com/4667129/129460183-f73fd810-80e7-4440-872b-c8c3ad302115.png)


# Screen Recording

Video: https://youtu.be/M8rDx_4pgHk

# Future Work

Some improvements for future consideration

+ **Feature engineering**: as explained in the video, since the labels in the provided dataset are highly imbalanced (89% "No" vs 11% "Yes"), this can lead to a falsely perceived positive effect of a model's accuracy because the input data has bias towards one class. Improving this will surely be beneficial. One way is to find more data of the smaller class, or using synthetic data generation technique is also useful. 

+ **Training optimization**: increasing experiment timeout and number of cross validation for AutoML can help find better performance model.

+ **Service monitoring**: using benchmark tools such as Apache Benchmark to examine the service throughput in current compute target to see if it meets the performance target or needs to have more computation resource. Also, having the benchmark information we can estimate the acceptable time per request then set up alerts in Application Insights to detect early sign of performance degrading to proactively plan for higher compute resource. 

