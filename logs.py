# import azureml.core
from azureml.core import Workspace
from azureml.core.webservice import Webservice

# print("Ready to use Azure ML", azureml.core.VERSION)

# Requires the config to be downloaded first to the current working directory
# ws = Workspace.from_config()
ws = Workspace.from_config('config.json')
# print(ws.name, "loaded")

# Set with the deployment name
name = "bankmarketing-classifier"

# load existing web service
service = Webservice(name=name, workspace=ws)

# Enable Application Insights; only need to do once
# service.update(enable_app_insights=True)

# Recent logs
logs = service.get_logs()

for line in logs.split('\n'):
    print(line)

