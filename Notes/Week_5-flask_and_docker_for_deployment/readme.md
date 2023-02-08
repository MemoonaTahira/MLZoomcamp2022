# Week 5: Learning to package and deploy a ML Model with WSL, Flask and Docker

### 1. Understanding how WSL and Windows interact:

<img src = ./MLZoomcamp_WSL_x1.png width=80% height=80%>

### 2. For a complete, step-by-step visual installation guide on setting up flask and docker with WSL Ubuntu, please click [here](./Setting_up_WSL%2BDocker.md)

### 3. Building and running docker:

```
# . will look for a docker file in the current directory, we can also tag the image as: image_name:tag
docker build -t image_name . 
# rm is important, it removes intermediate containers created, and it will give us an interactive terminal used as entrypoint, e.g. bash. This will provide us with a # bash terminal in case we pulled a python image instead of a python terminal
docker run -it --rm --entrypoint=bash --name=container_name image_name -p docker_port:external_port
```

For more details, see:
- Notes by [Ayoub BERDEDDOUCH](https://github.com/ayoub-berdeddouch/mlbookcamp-homeworks/blob/main/Deployment/README.md)
- Notes by [Hareesh Tummala](https://github.com/tummala-hareesh/ml_zoomcamp_ht/blob/main/notes/week-5-notes.md) 
<!-- ### 3. For a step-by-step command line script for building and runnig a flask app and docker container, please click [here](./Create_flask_app_docker.sh) -->

