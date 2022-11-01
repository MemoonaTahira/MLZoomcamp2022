# Week 5: Learning to package and deploy a ML Model with WSL, Flask and Docker

### 1. Understanding how WSL and Windows interact:

<img src = ./MLZoomcamp_WSL_x1.png width=80% height=80%>

### 2. For a complete, step-by-step visual installation guide on setting up flask and docker with WSL Ubuntu, please click [here](./Setting_up_WSL%2BDocker.md)

<!-- ### 3. For a step-by-step command line script for building and runnig a flask app and docker container, please click [here](./Create_flask_app_docker.sh) -->

### 3. For building and runnig a flask app, follow these steps:


### for buidling and running a docker container (optionally with gpu), follow these steps:

#### OPTIONAL - Speed up docker build: Only if you have an NVIDIA GPU + Windows 11 + WSL ready NVIDIA drivers
# set up nvidia container runtime for building docker containers with GPU:
# https://github.com/NVIDIA/nvidia-docker

distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list


sudo apt-get update
sudo apt-get install -y nvidia-docker2
# sudo systemctl restart docker
# systemctl doesn't work with WSL, just start the docker srevice:
sudo dockerd & 
# hit enter once to exit the INFO message, the docker service will keep running in the background
sudo docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
# once done, run docker images to get image ID and then run:
docker rmi <image ID>


### jumble

Do docker run and docker pull download an image? If so, where is it? in temp?

To start the docker dameon, what's the difference between these two commands: sudo dockerd vs sudo dockerd &? I think it numbers

Why do we not need sudo inside docker image?


 docker image prune -a
 docker image prune


‘’‘docker build --rm ‘’’



when we exit, what happens to the changes we did inside the image?

image remains, containers get deleted

Does accidentally running dockerd 3 times spawn 3 different daemons? no, it says pid found

sometime sudo command doesnt run > wont ask for passwork
after running, INFO should exit, can do. daemon already started

ctrl d to exit shell

mkdir app didnt overwrite but can leave it?
WORKDIR /app

uses cache. But if something in previous iamge, not overwritten wese only setting workdir, not creating new


leave python version only unless exact python version


 docker build --no-cache -t zoomcamp-test .

(base) mona@Memoona-PC:~/HW5$ docker run -it --rm --entrypoint=bash zoomcamp-test                                       

(base) mona@Memoona-PC:~/HW5$ docker run -it --rm --entrypoint=bash svizor/zoomcamp-model:3.9.12-slim


/usr/local/bin/python -m pip install --upgrade pip


add correct filename in app, without py
variables should be correct
also, add main guard and command line args

after change to docker file, always rebuild

no cache is so quick


 docker run -it -p 9000:9000 --rm zoomcamp

docker rmi <your-image-id>


docker shell with ctrl d
bash command ctrl c


map port
expose port
forward port
