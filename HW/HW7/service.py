import numpy as np
import bentoml
from bentoml.io import JSON
# helper library to cast ndarray into numpy array, to receive e.g. a CSV file that's sent line by line
from bentoml.io import NumpyNdarray
from pydantic import BaseModel
import sklearn

# pydantic class for data validation
class UserProfile(BaseModel):
    name: str
    age: int
    country: str
    rating: float

# To get mode by tag:
model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")
# dv = model_ref.custom_objects['dictVectorizer']

# # To get model by latest:
# model_ref = bentoml.xgboost.get("credit_risk_model:latest")
# # dv = model_ref.custom_objects['dictVectorizer']

# model runner is bentoml's abstraction of the model itself, helps us access the model
model_runner = model_ref.to_runner()
svc = bentoml.Service("mlzoomcamp_model1", runners = [model_runner])


# for numpy ndarray data: 

# the decorater allows us to use rest ad curl APIs
# @svc.api (input =NumpyNdarray(shape = (-1,29), enforce_shape = True, dtype= np.float32, enforce_dtype= True), output=NumpyNdarray)
# @svc.api (input =NumpyNdarray(shape = (-1,4), enforce_shape = True), output=NumpyNdarray)
@svc.api (input= NumpyNdarray(), output= NumpyNdarray())

async def classify(vector):

    # application data is a dict object, and incase we used @svc.api (input =JSON(), output=JSON()),
    # we could pass it to classify and use it without converting
    # user_data = user_profile.dict()
    # vector = dv.transform(user_data)  
    prediction = await model_runner.predict.async_run(vector)
    print(prediction)

    # result = prediction[0]
    # print(result)