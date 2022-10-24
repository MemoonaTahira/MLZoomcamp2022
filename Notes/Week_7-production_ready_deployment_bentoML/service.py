# credit_risk_model:g6c6ytcqm22agaav

# from numpy import vectorize
import numpy as np
import bentoml
from bentoml.io import JSON

# model_ref = bentoml.xgboost.get("credit_risk_model:g6c6ytcqm22agaav")

model_ref = bentoml.xgboost.get("credit_risk_model:latest")
dv = model_ref.custom_objects['dictVectorizer']

# model runner is bentoml's abstraction of the model itself, helps us access the model
model_runner = model_ref.to_runner()


svc = bentoml.Service("credit_risk_classifier", runners = [model_runner])

# the decorater allows us to use rest ad curl APIs
@svc.api (input =JSON(), output=JSON())
def classify(application_data):
    
    vector = dv.transform(application_data)
    prediction = model_runner.predict.run(vector)
    print(prediction)

    result = prediction[0]
    if result > 0.5:
        return {"status": "DECLINED"}
    elif result > 0.25:
        return{"status":"MAYBE"}
    else: 
        return{"status":"APPROVED"}
