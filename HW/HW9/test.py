import requests

# where to send request to test our image and return results: 
url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

# the data we want to send via post request. SInce it is json data, has a key and a field. 
# Our lambda function should expect a url key and some value in it
data = {'url': 'https://upload.wikimedia.org/wikipedia/en/e/e9/GodzillaEncounterModel.jpg'}

# return results as json, lambda function should pass results that are json serializable 
result = requests.post(url, json=data).json()
print(result)
