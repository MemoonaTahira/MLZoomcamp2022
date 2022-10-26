import numpy as np
import bentoml
# helper library to cast ndarray into numpy array, to receive e.g. a CSV file that's sent line by line
from bentoml.io import NumpyNdarray
# from pydantic import BaseModel
# import sklearn

# pydantic class for data validation
# class UserProfile(BaseModel):
#     name: float
#     age: float
#     country: float
#     rating: float

# To get model by tag:
# model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")
model_ref = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5")


# model runner is bentoml's abstraction of the model itself, helps us access the model
model_runner = model_ref.to_runner()
svc = bentoml.Service("mlzoomcamp_model1", runners = [model_runner])


# for numpy ndarray data: 
# the decorater allows us to use rest and curl APIs
# for numpy arrays, I think no separate pydantic class if defined
@svc.api (input =NumpyNdarray(shape = (-1,4), enforce_shape = True, dtype= np.float32, enforce_dtype= True), output=NumpyNdarray())
async def classify(user_profile):
    print(user_profile)
    prediction = await model_runner.predict.async_run(user_profile)    
    return prediction
