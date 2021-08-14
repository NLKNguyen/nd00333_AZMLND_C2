# nd00333_AZMLND_C2

*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.


# Your Project Title Here

*TODO:* Write an overview to your project.

## Architectural Diagram
*TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model". 

## Key Steps
*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

### Create Azure Service Principle

![image](https://user-images.githubusercontent.com/4667129/129117771-8e9fdf44-a2f8-434c-bff8-a5d10ef8bb25.png)

Get object Id

![image](https://user-images.githubusercontent.com/4667129/129118657-992a03e9-6a9b-4bdf-8d13-6c9fb2573741.png)


### Share workspace to the newly created account
![image](https://user-images.githubusercontent.com/4667129/129118415-ba4bc243-2efe-4beb-bcb9-a14adca4bd9f.png)

### Upload dataset and register

![image](https://user-images.githubusercontent.com/4667129/129119881-c0cf253e-b0a5-42e2-92a8-20a5c7879e5a.png)

![image](https://user-images.githubusercontent.com/4667129/129119850-02de4623-3402-43b2-bc7e-eb477e4b537d.png)

### Use AutoML for finding the best classification model

![image](https://user-images.githubusercontent.com/4667129/129120027-875f0be6-c487-4262-9ffc-370495223e64.png)

![image](https://user-images.githubusercontent.com/4667129/129120128-a730e484-4332-4e30-9db9-e6a9d189de74.png)

![image](https://user-images.githubusercontent.com/4667129/129120152-becff75c-6cd2-45d1-9092-403d3acb2c79.png)


### Deploy the best model

![image](https://user-images.githubusercontent.com/4667129/129460832-621b4167-aa5c-4bf1-ba47-3a6eeed382eb.png)

### Interact with the deployed model using Python

#### Set up Python SDK for Azure in local environment

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

#### Enabled Application Insights using Python script

![image](https://user-images.githubusercontent.com/4667129/129120622-c2e842be-4559-48c3-895e-421e0e03e62b.png)

![image](https://user-images.githubusercontent.com/4667129/129120539-27853550-8331-43ea-848a-cc313fc5f425.png)

Preview logs from the local script

![image](https://user-images.githubusercontent.com/4667129/129120654-d88f6ea1-b411-46a6-89ac-722691b53162.png)

#### Swagger Documentation

Swagger.json URL for the endpoint is available to download

![image](https://user-images.githubusercontent.com/4667129/129433043-2e63be75-cb0e-493b-8706-4c9ff099183f.png)


Run localhost serving the edownloaded swagger.json that allows CORS for Swagger UI to access

![image](https://user-images.githubusercontent.com/4667129/129433035-1727ea70-70ca-4dd8-b765-20f84d3f8fec.png)

Run Swagger UI

![image](https://user-images.githubusercontent.com/4667129/129433076-f5ab8dbf-f4cd-4c19-9671-653e46a7d63a.png)

Access API documentation from the local swagger.json

![image](https://user-images.githubusercontent.com/4667129/129433082-52e36b54-b028-4dc3-a038-76a78ffdcbc4.png)

#### Consume Endpoint

Set up endpoint test script with URI with authentication key and sample test data

![image](https://user-images.githubusercontent.com/4667129/129434783-82c120b4-c872-4da2-869b-6542fb408c2f.png)

Test the endpoint

![image](https://user-images.githubusercontent.com/4667129/129434801-843586c9-f5fe-463e-b03a-83db5a26c16e.png)


### Pipeline

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


## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
