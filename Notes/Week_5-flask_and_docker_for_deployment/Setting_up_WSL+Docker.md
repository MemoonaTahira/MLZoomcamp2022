The aim of this guide is to replicate the exact working environment as shown in the [week 5](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/05-deployment) of MLZoomcamp coursework, as well for [homework5](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/cohorts/2022/05-deployment). 

<img src = MLZoomcamp_docker_workflow_x1.png width=80% height=60%>


## Pre-requisites:
1. Windows 10 
2. If you have an Nvidia GPU:
   - Upgrade to Windows 11 if you haven't automatically been upgraded from Windows 10 to 11. Check if you meet requirements for Windows 11, and download it directly from [here](https://www.microsoft.com/software-download/windows11). 
   - Next download WSL ready drivers from [here](https://developer.nvidia.com/cuda/wsl)


## Setting up WSL:

1. Type powershell in windows start menu and click enter
2. Enable WSL from powershell
3. Download "Ubuntu 20.04" distro. We are selecting Ubuntu 20.04 as it is the latest Ubuntu distro available in WSL
4. Upgrade from WSL1 to WSL2 if not on WSL2 already, and set WSL2 as default version for any new distro. Let's have a look at how to do all this:

   - ![image](https://user-images.githubusercontent.com/41547742/194409098-2b6fd63d-ae20-443e-a216-f8cd3e6439a3.png)
   - Run the following commands one by one"
      - ```
         # To install the latest default distro, only works for first time WSL install:
         wsl --install  
         
         # OR if you want to manually choose which Ubuntu distro to install:
         wsl --list --online  
         
         # Choose whichever distro you want, at the time of writing, latest available is Ubuntu 20.04
         wsl --install -d Ubuntu-20.04 
         wsl -l -v  
         wsl --set-version Ubuntu 2  
         wsl --set-default-version 2
         ```
        
   - You can now use bash commands in the ubuntu bash shell* to interact with your new Ubuntu system!
   
   - *\*You can find it by going to start menu> typing "ubuntu 20.04 on windows".*
   
   - ![194554316-b296450b-8104-4396-b4c3-ddcaf1d07d1e](https://user-images.githubusercontent.com/41547742/194722893-a9adc0d2-8048-4411-8574-9b25f4da06c8.png)


5. Use Ubuntu bash shell with Windows Terminal as it has a cleaner layout and better customization options.
To download Windows Terminal: [Click here](https://learn.microsoft.com/en-us/windows/terminal/install)
   - Find it by typing 'terminal' in start menu
   -  ![194554655-ae74eb43-bc06-42c6-a2ab-591d6d29509d](https://user-images.githubusercontent.com/41547742/194722914-f2b27b15-8e0b-4c1b-ac9c-2e2ae75e57d5.png)

   - open the terminal
   - Use the small arrow next to the + tab to select ubuntu terminal (with a penguin :penguin: on it) to get started.

   
6. Next, upgrade Ubuntu 20.04 to 22.04 distro (since it isn't available yet from wsl --list --online) using this guide [here](https://linuxconfig.org/how-to-upgrade-ubuntu-to-22-04-lts-jammy-jellyfish) from the terminal:

   - ![image](https://user-images.githubusercontent.com/41547742/194409522-eda361a7-78db-4dbc-aaf1-46619e2b0433.png)

   - Run all these commands one by one:

      - ```
         sudo apt update  
         sudo apt upgrade
         sudo apt dist-upgrade
         sudo apt autoremove
         sudo apt install update-manager-core
         sudo do-release-upgrade 
         ```
   - Once you've run all commands, you'll see this message:

   - ![any](https://user-images.githubusercontent.com/41547742/194403608-01c4591c-3e02-4b08-b850-3cad9f872059.png)

   - (P.S. The name of the of the Ubuntu app and on the tab in the terminal isn't changed with an upgrade from 20.04 to 22.04, it will still be Ubuntu-20.4, so don't worry about it.) 


## Setting up pipenv, optionally with miniconda
From now on, everything you need to do is inside the Ubuntu terminal (and not cmd etc).

1. **Install pipenv inside Ubuntu using terminal.** 

   - ![any2](https://user-images.githubusercontent.com/41547742/194410760-685cd894-7b0e-4216-a627-d27c8e9f64ef.png)

   - Run these commands one by one:

      -  ```
         sudo apt install python3-pip
         pip install pipenv
         ```

   - Close this terminal tab and open a new tab using the + sign. This will refresh the path and make pipenv command visible in the terminal. (Kind of like restarting a computer if we were using a real Ubuntu OS) 


2. **Confirm system python version:**

   - ![image](https://user-images.githubusercontent.com/41547742/194552774-fc83f0cd-d7e3-4aa1-8ca1-2949ed7c7d6c.png)

   - Run this:

      - ```
         python3 --version
         ```

<!--On Ubuntu 22.04, the version is python 3.10. We need 3.9 for homework. Since pipenv will use system python, we need to install python 3.9 ourselves. We'll do so using miniconda.-->

3. **(Optional/Recommended) Installing miniconda for better python version management:**

   - ![image](https://user-images.githubusercontent.com/41547742/194419378-ccb8c757-2926-4827-8356-64c11a9760c9.png)

   - Run the following commands one by one:

      -  ```
         curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh --output
         miniconda_installer.sh
         bash miniconda_installer.sh
         ```

   - Hit enter till you reach end of agreement, type *yes*, hit *enter* to keep default installation location, type *yes* to `init conda`

   - Once done, open another ubuntu tab, and close the first tab for conda to become visible in the terminal. (Kind of like restarting a computer if we were using a real Ubuntu OS) 

   - Create a new conda environment:
   - ![image](https://user-images.githubusercontent.com/41547742/194419793-6605e12c-944f-4867-a511-499eedc650a5.png)

   - Run the following commands one by one:

      - ```
         conda update conda 
         conda create -n mlzoomcamp-ubuntu python=3.9
         conda activate mlzoomcamp-ubuntu
         conda run which python
         conda deactivate
         ```

   - In case you want python 3.10, or any older version like 3.8, you can change the first command to: `conda create -n mlzoomcamp-ubuntu python=3.10` or `conda create -n mlzoomcamp-ubuntu python=3.8`

   - Also, note the python path of this conda environment.

4. **Create a new directory for our code and cd to it:**

   - ![image](https://user-images.githubusercontent.com/41547742/194729741-c2849c2a-e68d-4854-8e15-284f89ea5583.png)

   - Run all of the following commands one by one:

      - ```
         mkdir churn-flask-app
         cd churn-flask-app

         #if you installed miniconda then run the next 2 commands:
         pipenv --python=/home/$USER/miniconda3/envs/mlzoomcamp-ubuntu/bin/python
         pipenv install numpy pandas scikit-learn==1.0.2 requests flask jupyter ipython gunicorn
         
         # in case you get an error about python_version and python_full version, do this:
         nano Pipfile
         # In the opened file, remove the line with python_full_version, type CTRL+X to exit, type Y to save 
         # and click Enter. Now complete the lock creation:
         pipenv lock
         #You should be good to go.  

         # if you didn't, only run this:
         pipenv install numpy pandas scikit-learn requests flask jupyter ipython gunicorn
         ```
   - The last command should automatically use system python (3.10) in the pyenv virtual environment.
   - A word of caution - I have tried this with all 3 options; pipenv without miniconda and 2 separate miniconda environments with python 3.9 and python 3.10:
      - In the first case, with pipenv with just system python 3.10, I tried installing scikit-learn==1.0.2 and it failed for me. If I install just scikit-learn without specifying version, it runs fine and installs latest scikit-learn 1.1.2. 
      - When I tested with 2 separate miniconda environments with python 3.9 and python 3.10, and then used pipenv with python from these environments, I could install scikit-learn==1.0.2 without any trouble in both cases. 
      - To use scikit-learn 1.0.2 as required in the homework, I'd strongly suggest using miniconda.
      - If you prefer to skip miniconda, please search more on how to install specifically scikit-learn==1.0.2.  

   - In case you forget anything, just run ```pipenv install <package name>```


5. **Activate the new environment:**

   - Whenever you want to activate the pipenv you just created, you need to cd into the folder from where you ran the pipenv install command, and type `pipenv shell`. This is the way to identify environments in pipenv without using any environment name. See FAQ 3 for more info. 

   - To check if it is working, type ```ipython```

   - ![image](https://user-images.githubusercontent.com/41547742/194424720-d2e4189d-460f-47a6-9596-0fb5b4d2442e.png)

## Setting up Jupyter Notebook and VSCode with WSL:
6. **Connect jupyter notebook / VScode to WSL.** 
   - For jupyter notebook, simply type `jupyter notebook` in the Ubuntu terminal, 
   and copy the token it generates and paste it in Chrome in Windows. (P.S. In my case, it automatically opened a chrome browser window, yaay!)
   
   - ![image](https://user-images.githubusercontent.com/41547742/194425039-04fc8935-434b-4058-aca7-d5b5733c1496.png)

   - ![image](https://user-images.githubusercontent.com/41547742/194425469-a07d7d95-84af-47e0-b6f4-9a3831bd1b5b.png)

   - For using VScode: Install the remote developer extension. 

   - ![image](https://user-images.githubusercontent.com/41547742/194425639-c2a11115-a99d-4211-a463-19c07afbc19b.png)

   - Once done: 

   - ![5](https://user-images.githubusercontent.com/41547742/194429048-e8674daa-1966-490f-a5cf-55ccc31bace9.png)

   - Select your project folder and open it. 

   - ![image](https://user-images.githubusercontent.com/41547742/194426920-a9963fec-e20a-4840-ad61-fa522c0b33c1.png)

   - Next, clone the mlbookcamp repo, and code week 5 code to churn-flask-app without overwriting the Pipfile and Pipfile.lock:
   - ![image](https://user-images.githubusercontent.com/41547742/194729052-46b41a70-d3f8-4377-9b4f-3fb07d0ccaa2.png)
   - ![image](https://user-images.githubusercontent.com/41547742/194729186-1453712e-3b68-4476-ba6e-592b8fd40339.png)

   - Run these commands one by one:
      - ```
         git clone https://github.com/alexeygrigorev/mlbookcamp-code.git
         # -n flag will prevent overwriting, --verbose will show what was copied. You can omit --verbose
         cp -r -n --verbose mlbookcamp-code/course-zoomcamp/05-deployment/code/* churn-flask-app/
         ```
   - Next get data-week-3.csv as it is not the week 3 folder, copy it to churn-flask-app and rename it:
   - ![image](https://user-images.githubusercontent.com/41547742/194729373-4dce1f6f-e014-4856-a87c-ebe7d95a4500.png)

   - Run the following one by one:
      - ```
         cp mlbookcamp-code/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv churn-flask-app/
         cd churn-flask-app/
         mv WA_Fn-UseC_-Telco-Customer-Churn.csv data-week-3.csv
         ```


   - Add correct python interpreter. Also, in the terminal menu, click add new terminal and then type `pipenv shell`, and voila, you can use all WSL commands here if you need:

   - ![7](https://user-images.githubusercontent.com/41547742/194431431-1094414f-53d4-4585-9225-27b90d68c946.png)
   
   - Run code without debugging. (Iff vscode asks you to install the Python for WSL extension, do so). The output of train.py: 

   - ![image](https://user-images.githubusercontent.com/41547742/194432513-9f881fde-01fb-4516-afdf-8d6f70d08a09.png)

   - Once you are done coding, and want to restore vscode to work with windows, click on the bottom left, and select terminate connection.

   - ![4](https://user-images.githubusercontent.com/41547742/194428461-c743f0b7-3ccb-4de2-9c07-180aa90c5617.png)   

7. **Play with your code. You can also run the code entirely within Ubuntu terminal:**

   - ![8](https://user-images.githubusercontent.com/41547742/194467722-0971d925-a5ba-45d3-9bdc-72b4cb3acb95.png)

   - Run the following command to run train.py:

      - ```
         pipenv shell
         python train.py
         ```

8. **Create a flask app and deploy it locally, and test it** 

## Installing Docker with WSL: 

9. **Install Docker:** 
   - Either directly inside WSL using the Ubuntu terminal. [This](https://www.youtube.com/watch?v=IXSiYkP23zo&ab_channel=DataTalksClub%E2%AC%9B) [1] video covers it from timestamp 6:39 to 10:05.

   - run the following commands one by one in your home directory:

      - ```
         sudo apt update
         sudo apt install docker.io
         mkdir soft
         cd soft/
         # Go to https://github.com/docker/compose/releases to get link of the release of docker-compose you want by right clicking > copy link. Download it with wget command as shown below:
         wget https://github.com/docker/compose/releases/download/v2.11.2/docker-compose-linux-x86_64 -O docker-compose
         # make the newly downloaded docker file an executable:
         chmod +x docker-compose
         # open bashrc in nano editor
         nano .bashrc
         # add path of soft folder with docker-compose inside to the end of the file like this:
         export PATH="${HOME}/soft:${PATH}"
         # type ^X to exit, then type 'Y' to accept changes, and then click Enter. 
         # Reload bashrc:
         source .bashrc
         # check if docker-compose has been correctly added to the path, the commnand below will return path of docker-compose
         which docker-compose
         # check if docker command is working:
         sudo docker run hello-world
         # add our user to docker group, to avoid using sudo everytime before docker
         sudo usermod -aG docker $USER
         logout
         # run hello-world command again to see if it worked:
         docker run hello-world
         # In case the above command does not execute properly and says docker daemon isn't running, run this:
         sudo update-alternatives --set iptables /usr/sbin/iptables-legacy
         sudo update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy
         sudo dockerd &
         # try again, and it should run:
         docker run hello-world
         ```

   - For additional docker compose plugins installation, please see [here](https://github.com/MemoonaTahira/MLZoomcamp2022/blob/main/Notes/Week_7-production_ready_deployment_bentoML/setting_up_bentoML_WSL.sh). (Code lines 221 - 242). This part is not needed until week 7 of BentoML. BentoML requires some of these plugins.
   - Or alternatively, install Docker Desktop for Windows, which is an easier installation and you can access the docker command inside WSL. You can find help [here](https://docs.docker.com/desktop/windows/wsl/).
10. **Dockerize the flask app** 
11. **Again deploy the docker container locally** 
12. **Now deploy on cloud, e.g. Heroku or AWS.** 

Step 8 onwards are covered here: 
[Churn prediction app deployment with flask and docker to AWS](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/05-deployment)



## Extra notes:

[1] This video is linked in Week 1, 06-environment.md of MLZoomcamp 
[here](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/01-intro/06-environment.md).

Some points to understand from the video:
- The instructor is using a mingw64 terminal (which allows a user to interact with 
Windows using linux commands, but is not a full-fledged OS like WSL with Ubuntu), to connect AWS to add a Ubuntu backend.
- After he has provisioned a Ubuntu instance from AWS, it is as if he is using Ubuntu from within his mingw64 terminal. Instead we are using WSL's Ubuntu terminal. 
- Consider that you already have done the above 2 steps and are using Ubuntu via WSL instead of AWS, and are at the 5:18 min timestamp, and can now proceed from here. Only instead of just anaconda/miniconda,
you will also need to install pipenv for week 5 (which is covered in [lesson 5.5](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/05-deployment/05-pipenv.md)). The rest of the video will be the same for you, and it covers setting up
Docker nicely. Connecting to VScode and jupyter is a bit different as you'll see in the tutorials, and easier in the case of jupyter because pasting the token 
in the browser will directly open it, no port forwarding needed.



## FAQ:

1. **Should I use pipenv alone to create environments without using something like miniconda?** 
   - Ideally, no. This way, pipenv will be bound to system python, so any upgrade to the system python can potentially break a pipenv environment. 
   - Instead, we use it with anaconda/miniconda environment with the required python version.
   - There are multiple other options. [This](https://towardsdatascience.com/python-environment-101-1d68bda3094d) article here explains some of them.
   - Only using *pipenv* is a **MUST** becuase it creates the pipfile.lock we need for our Docker container.
2. **Where do I run this command: `pip run pipenv`:**
   - Globally, outside of any environment. Deactivate all environments, including conda base environment, before running this command.  

3. **Does using a miniconda environment means we are creating our pipenv environment inside of it?**
   - No, as long we don't run `pip install pipenv` inside a conda environment. We only want our pipenv environment to use python of the conda environment and that's it. A word of caution: *Do not use the conda environment supplying the python to pipenv environment for anything else as this can cause the python version to change. Leave it alone and deactivated.*

   - You may ask why we create a new conda environment, `mlzoomcamp-ubuntu` is this case, and why not just use the base environment? It is good practice to use one separate environment for each project instead of base.

   - Now, the last question that may arise is: Why is the `(base)` environment still active when I activate my pipenv environment? This is not related to pipenv specifically. Once you install miniconda, it modifies the terminal settings to always start it with the base environment activated. You can deactivate it, and the pipenv environment would still work fine. See this image below:

   - ![image](https://user-images.githubusercontent.com/41547742/194654806-0e180a65-757f-4af9-bde9-919056ea3ecf.png)


4. **Where does pipenv create environments and how does it name them?**
   - It creates them in *~/.local/share/virtualenvs/environment_name.* 

   - The environment name is the name of the last folder in the folder directory where we used the pipenv install command (or any other pipenv command). E.g. If you run any pipenv command in folder path *~/home/user/Churn-Flask-app*, it will create an environment named Churn-Flask-app-some_random_characters, and it's path will be like this: */home/user/.local/share/virtualenvs/churn-flask-app-i_mzGMjX.* 

   - All libraries of this environment will be installed inside this folder. To activate this environment, I will need to cd into the project folder again, and type pipenv shell. In short, the location of the project folder acts as an identifier for an environment, in place of any name.


5. **Do I need to install both Docker Desktop for Windows and install Docker manually on WSL?** 
   - No, not needed. Installing Docker Desktop for windows will make the docker command accessible inside WSL. It is also easier to install. However, if you want to install docker directly from bash in WSL, uninstall Docker Desktop completely first. 

6. **Do we need to use docker inside any environment?** 
   - Doesn't matter as docker is not affected by environments. 

<!--7. **What are 0.0.0.0 and 127.0.0.1?** 
   - 0.0.0.0 is a placeholder IP which can mean: Use any IP available. 127.0.0.1 is localhost IP (a reserved IP) which refers to the host OS itself. On Windows, this IP will refer to localhost which is Windows. On WSL, this IP will refer to Ubuntu.

8. **Can I map multiple IPs to the same port inside a single OS?** 
   - No, this will not work. Map the new IP to any of the available, unused ports. -->

7. **If your main concern isn't following along the videos, how much of these steps can be done in Windows alone, without using WSL?** 
   - Everything from step 1-6 can be done in Windows. Install pipenv inside an anaconda environmen in Windows, as pip is only available via a coda environment without any WSL. For step 7, WSL is needed but the Docker container can be completely created within Docker Desktop GUI. Step 8 onwards can again be done in Windows. (Summary: Docker containers can be only be created in a Linux system e.g. Ubuntu, MacOS) but they can be deployed in any OS.

## Troubleshooting common error:

1. **Python_version and Python_full_version error after running pipenv install:**
 
   - If you install packages via pipenv install, and get an error that ends like this: 

      - ```
         pipenv.vendor.plette.models.base.ValidationError: {'python_version': '3.9', 'python_full_version': '3.9.13'}
         python_full_version: 'python_version' must not be present with 'python_full_version'   
         python_version: 'python_full_version' must not be present with 'python_version'
         ```
   - Do this:
      - open Pipfile in nano editor, and remove either the python_version or python_full_version line, press CTRL+X, type Y and click Enter to save changed
      - type `pipenv nano` to open file in nano
      - Type `pipenv lock` to create the Pipfile.lock.
      - Done. Continue what you were doing
 
2. **Docker build error: Pipfile.lock out-of-date:**
 
   - If during running the  docker build command, you get an error like this:
 
      - ```
         Your Pipfile.lock (221d14) is out of date. Expected: (939fe0).
         Usage: pipenv install [OPTIONS] [PACKAGES]...   
         ERROR:: Aborting deploy
         ```
   
   - Option 1: Delete the pipfile.lock via `rm Pipfile`, and then rebuild the lock via `pipenv lock` from the terminal before retrying the docker build command. 
   - Option 2:  If it still doesn’t work, remove the pipenv environment, Pipfile and Pipfile.lock, and create a new one before building docker again. Commands to remove pipenv environment and removing pipfiles:

      -  ```
         Pipenv --rm
         rm Pipfile*
         ```
3. **Error message whil trying to use docker commands: "Is Docker Daemon running?"**
   - If you get an eeror that says:
      - ```
         Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
         ```
   - Type `dockerd` in the terminal to start the docker daemon, and then open a new tab to continue. This command will start the docker daemon.

