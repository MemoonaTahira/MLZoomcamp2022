# Week 7: Production-ready ML Models with BentoML

<p align="center">
<img src = "MLZoomcamp_BentoML_x2.png" width=50% height=50%>
</p>

Click [here](MLZoomcamp_BentoML_x3.png) for a high resolution image.

## 1. For a detailed guide for installing and building with bentoml on WSL or Ubuntu, please refer [here](./setting_up_bentoML_WSL.sh). 

1. This guide runs through the code examples used in week 6 to test a basic XGBoost bentoml model locally via curl or Swagger UI. 
2. It then tests the validity of test data
3. And then it does stress testing for production
4. Once the model is found to be satisfactory, it then cantainerizes the bentoml model and again tests it locally via curl or Swagger UI.
5. Finally, the container is deployed to cloud. We now have our production-ready service depoloyed to cloud.
6. Bentoml container has fully functional API to interact with the the ML service.

## 2. All relevant code files can be found in this repo too: [train.ipynb](./train.ipynb), [service.py](./service.py), [bentofile.yaml](./bentofile.yaml), [locustfile.py](./locustfile.py)!
