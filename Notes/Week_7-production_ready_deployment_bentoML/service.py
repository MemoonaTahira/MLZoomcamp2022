import numpy as np
import bentoml
from bentoml.io import JSON
# helper library to cast ndarray into numpy array, to receive e.g. a CSV file that's sent line by line
from bentoml.io import NumpyNdarray
from pydantic import BaseModel

# pydantic class for data validation
class CreditApplication(BaseModel):
    seniority: int
    home: str
    time: int
    marital: str
    records: str
    job: str
    expenses: int
    income: float
    assets: float
    debt: float
    amount: int


# To get model by tag:
# model_ref = bentoml.xgboost.get("credit_risk_model:g6c6ytcqm22agaav")
# To get model by latest:
model_ref = bentoml.xgboost.get("credit_risk_model:latest")
dv = model_ref.custom_objects['dictVectorizer']

# model runner is bentoml's abstraction of the model itself, helps us access the model
model_runner = model_ref.to_runner()
svc = bentoml.Service("credit_risk_classifier", runners = [model_runner])


# the decorater allows us to use rest and curl APIs
@svc.api (input =JSON(pydantic_model= CreditApplication), output=JSON())

# def classify(application_data):
# adding async parallelizes at the endpoint level
async def classify(credit_application):
    # credit_application is an object of class CreditApplication

    # application data is a dict object, and incase we used @svc.api (input =JSON(), output=JSON()),
    # we could pass it to classify and use it without converting
    application_data = credit_application.dict()    
    vector = dv.transform(application_data)

    # prediction = model_runner.predict.run(vector)
    # also async at inference level, the runner abstraction here is doing microbatching, i.e. like a test set
    # instead of performing inference for each single user/test sample
    # corresponding change in train.ipynb by adding customizations besides the custom objects
    prediction = await model_runner.predict.async_run(vector)
    print(prediction)

    result = prediction[0]
    if result > 0.5:
        return {"status": "DECLINED"}
    elif result > 0.25:
        return{"status":"MAYBE"}
    else: 
        return{"status":"APPROVED"}

'''
# for numpy ndarray data: 

# the decorater allows us to use rest and curl APIs
# for numpy arrays, I think no separate pydantic class if defined
@svc.api (input =NumpyNdarray(shape = (-1,29), enforce_shape = True, dtype= np.float32, enforce_dtype= True), output=JSON())
# @svc.api (input =NumpyNdarray(shape = (-1,29), enforce_shape = True, dtype= np.float32, enforce_dtype= True), output=NumpyNdarray)


def classify(vector):

    prediction = model_runner.predict.run(vector)
    print(prediction)

    result = prediction[0]
    if result > 0.5:
        return {"status": "DECLINED"}
    elif result > 0.25:
        return{"status":"MAYBE"}
    else: 
        return{"status":"APPROVED"}
'''

# P.S. Always return the type defined in svc.api output