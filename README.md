## Prepare local environment

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

# nd00333_AZMLND_C2

*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.


# Your Project Title Here

*TODO:* Write an overview to your project.

## Architectural Diagram
*TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model". 

## Key Steps
*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
