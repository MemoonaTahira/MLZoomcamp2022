The aim of this guide is to replicate the exact working environment as shown in the [week 5](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/05-deployment) of MLZoomcamp coursework, as well for [homework5](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/cohorts/2022/05-deployment). 

<img src ="https://github.com/MemoonaTahira/MLZoomcamp2022/blob/main/Notes/imgs/MLZoomcamp_workflow_x1.png" width=80% height=60%>


### Pre-requsites:
1. Windows 10 
2. If you have an Nvidia GPU:
   - Upgrade to Windows 11 if you haven't automatically been upgraded from Windows 10 to 11. Check if you meet requirements for Windows 11, and download it directly from [here](https://www.microsoft.com/software-download/windows11). 
   - Next download WSL ready drivers from [here](https://developer.nvidia.com/cuda/wsl)


### Step wise tasks for enabling WSL:

1. Type powershell in windows start menu and click enter
2. Enable WSL from Powershell
3. Download "Ubuntu 20.04" distro. We are selecting Ubuntu 20.04 as it is the latest Ubuntu distro available in WSL.
4. Upgrade from WSL1 to WSL2 if not on WSL2 already, and set WSL2 as default version for any new distro

Step 2-4 can be done by running all these commands in powershell one by one:

```
wsl --install  
wsl --list --online  
wsl --install -d Ubuntu-20.04 
wsl -l -v  
wsl --set-version Ubuntu 2  
wsl --set-default-version 2
```
      
   - ![image](https://user-images.githubusercontent.com/41547742/194409098-2b6fd63d-ae20-443e-a216-f8cd3e6439a3.png)

   - This tutorial [here](https://learn.microsoft.com/en-us/windows/wsl/install) will explain step 1-3.
   - You can now use bash commands in the ubuntu bash shell* to interact with your new Ubuntu system!
   - *\*You can find it by going to start menu> typing "ubuntu 20.04 on windows".*
   - ![ubuntu](https://user-images.githubusercontent.com/41547742/194554316-b296450b-8104-4396-b4c3-ddcaf1d07d1e.png)
 


5. Use Ubuntu bash shell with Windows Terminal as it has a cleaner layout and better customization options.
To download Windows Terminal: [Click here](https://learn.microsoft.com/en-us/windows/terminal/install)
   - Use the small arrow next to the + tab to select ubuntu terminal (with a penguin :penguin: on it) to get started.
   - Find it by typing 'terminal' in start menu
   - ![term](https://user-images.githubusercontent.com/41547742/194554655-ae74eb43-bc06-42c6-a2ab-591d6d29509d.png)
 
   - open the terminal
   
6. Next, upgrade Ubuntu 20.04 to 22.04 distro using this guide [here](https://linuxconfig.org/how-to-upgrade-ubuntu-to-22-04-lts-jammy-jellyfish) from the terminal:

   - ![image](https://user-images.githubusercontent.com/41547742/194409522-eda361a7-78db-4dbc-aaf1-46619e2b0433.png)

Run all these commands one by one:

```
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
 

### Understanding how WSL and Windows interact:
<img src ="https://github.com/MemoonaTahira/MLZoomcamp2022/blob/main/Notes/imgs/MLZoomcamp_WSL_x1.png" width=80% height=80%>

### Setting up env (for jupyter + flask) and docker inside WSL:
From now on, everything you need to do is inside the Ubuntu terminal (and not cmd etc).

1. Install pipenv inside Ubuntu using terminal. 

![any2](https://user-images.githubusercontent.com/41547742/194410760-685cd894-7b0e-4216-a627-d27c8e9f64ef.png)

Run these commands one by one:

```
sudo apt install python3-pip
pip install pipenv
```

Close this terminal tab and open a new tab using the + sign. This will refresh the path and make pipenv command visible in the terminal. (Kind of like restarting a computer if we were using a real Ubuntu OS) 


2. Confirm system python version:

![image](https://user-images.githubusercontent.com/41547742/194552774-fc83f0cd-d7e3-4aa1-8ca1-2949ed7c7d6c.png)

Run this:

```
python3 --version
```

<!--On Ubuntu 22.04, the version is python 3.10. We need 3.9 for homework. Since pipenv will use system python, we need to install python 3.9 ourselves. We'll do so using miniconda.-->

3. (Optional) Installing miniconda for better python version management:

![image](https://user-images.githubusercontent.com/41547742/194419378-ccb8c757-2926-4827-8356-64c11a9760c9.png)

Run the following commands one by one:

```
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh --output miniconda_installer.sh
bash miniconda_installer.sh
```

Hit enter till you reach end of agreement, type *yes*, hit *enter* to keep default installation location, type *yes* to `init conda`

Once done, open another ubuntu tab, and close the path to refresh and for conda to become visible in the termianl. (Kind of like restarting a computer if we were using a real Ubuntu OS) 

Create a new environment without specifiying python version (it will create an environment with the latest python version available with conda) and activate it:

![image](https://user-images.githubusercontent.com/41547742/194419793-6605e12c-944f-4867-a511-499eedc650a5.png)

Run the following commands one by one:

```
conda create -n mlzoomcamp-ubuntu
conda activate mlzoomcamp-ubuntu
````

In case you want a specific python version, you can change the first command to: `conda create -n mlzoomcamp-ubuntu python=3.9
`

3. Create a new directory for our code and cd to it:
   
![image](https://user-images.githubusercontent.com/41547742/194423330-391493ae-6858-45a1-ab8d-d930f7ce0490.png)

Run all of the following commands one by one:

```
mkdir churn-pred-app
cd churn-pred-app

#if you installed miniconda then run the next 2 commands:
pipenv --python=$(conda run which python) --site-packages
pipenv install numpy pandas scikit-learn==1.0.2 requests flask jupyter ipython

# if you didn't, only run this:
pipenv install numpy pandas scikit-learn==1.0.2 requests flask jupyter ipython
```
The last command will automatically use system python (3.10) in the pyenv virtual environment.

In case you forget anything, just run:

```pipenv <package name>```

![image](https://user-images.githubusercontent.com/41547742/194424643-f0c38ac5-ab84-4f34-b075-9a66e31e1f19.png)


4. Activate the new environment:

```pipenv shell```

(In case of miniconda, note how it went from the mlzoomcamp-ubuntu environment to base environment, but it will still use python from mlzoomcamp-ubuntu.) 

Whenever you want to activate the pipenv you just created, you need to cd into the folder from where you ran the pipenv install command, and type `pipenv shell`. This is the way to identify environments in pipenv without using any environment name. See FAQ for more info. 

To check if it is working, type:

```ipython```

![image](https://user-images.githubusercontent.com/41547742/194424720-d2e4189d-460f-47a6-9596-0fb5b4d2442e.png)


4. Connect jupyter notebook / VScode to WSL. 
   - For jupyter notebook, simply type `jupyter notebook` in the Ubuntu terminal, 
   and copy the token it generates and paste it in Chrome in Windows. (P.S. In my case, it automatically opened a chrome browser window, yaay!)
   
![image](https://user-images.githubusercontent.com/41547742/194425039-04fc8935-434b-4058-aca7-d5b5733c1496.png)

![image](https://user-images.githubusercontent.com/41547742/194425469-a07d7d95-84af-47e0-b6f4-9a3831bd1b5b.png)

   - For using VScode: Install the remote developer extension. 

![image](https://user-images.githubusercontent.com/41547742/194425639-c2a11115-a99d-4211-a463-19c07afbc19b.png)

Once done: 

![5](https://user-images.githubusercontent.com/41547742/194429048-e8674daa-1966-490f-a5cf-55ccc31bace9.png)

Select your project folder and open it. 

![image](https://user-images.githubusercontent.com/41547742/194426920-a9963fec-e20a-4840-ad61-fa522c0b33c1.png)

And it will look something like this. In the terminal menu, click add new terminal and then type `pipenv shell`, and voila, you can use all WSL commands here if you need. 

![image](https://user-images.githubusercontent.com/41547742/194427931-20497a75-4144-41cd-b664-04aee2ebddd3.png)

Manually add the code files from [week 5](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/05-deployment/code) to home/*your username*/churn-prediction-app using file explorer, and keep the existing pipfile and pipfile.lock already present, don't overwrite them. 

![image](https://user-images.githubusercontent.com/41547742/194473451-7896e150-cca7-4249-a548-090f4c31dee3.png)

Type this in any terminal (Ubuntu or the just created VScode terminal) with path set to churn-predict-app folder to get data.week-3.csv:

![image](https://user-images.githubusercontent.com/41547742/194473209-0a99243b-54e6-4218-8652-2b89ab6c0b52.png)

`  curl https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv --output data-week-3.csv
`

Add correct python interpreter:

![7](https://user-images.githubusercontent.com/41547742/194431431-1094414f-53d4-4585-9225-27b90d68c946.png)
   
Run code without debugging. (Iff vscode asks you to install the Python for WSL extension, do so). The output of train.py: 

![image](https://user-images.githubusercontent.com/41547742/194432513-9f881fde-01fb-4516-afdf-8d6f70d08a09.png)

Once you are done coding, and want to restore vscode to work with windows, click on the bottom left, and select terminate connection.

![4](https://user-images.githubusercontent.com/41547742/194428461-c743f0b7-3ccb-4de2-9c07-180aa90c5617.png)   

5. Play with your code. You can also run the code entirely within Ubuntu terminal:

![8](https://user-images.githubusercontent.com/41547742/194467722-0971d925-a5ba-45d3-9bdc-72b4cb3acb95.png)

Run the following command to run train.py:

```
pipenv shell
python train.py
```

7. Create a flask app and deploy it locally, and test it 
8. Install Docker. 
   - Either directly inside WSL using the Ubuntu terminal. [This](https://www.youtube.com/watch?v=IXSiYkP23zo&ab_channel=DataTalksClub%E2%AC%9B) [1] video covers it from timestamp 6:39 to 10:05.

   - Or alternatively, install Docker Desktop for Windows, which is a more easier installation and you can access the docker command inside WSL. You can find help [here](https://docs.docker.com/desktop/windows/wsl/).
8. Dockerize the flask app 
9. Again deploy the docker container locally 
10. Now deploy on cloud, e.g. Heroku or AWS. 

Step 5 onwards are covered here: 
[Churn prediction app deployment with flask and docker to AWS](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/05-deployment)



### Extra notes:

[1] This video is linked in Week 1, 06-environment.md of MLZoomcamp 
[here](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/01-intro/06-environment.md). Follow this video for primarily setting up docker, even though watching the full video will be very helpful. We are using
different tools (WSL instead of AWS Ubuntu instance, pipenv instead of anaconda), but the workflow is same.

You can of course follow the whole video if you want to skip using
WSL altogether, and you'd rather connect with an AWS Ubuntu backend. 

Some notes on the video:
- The important thing to understand here is that the instructor is using a mingw64 terminal (which allows a user to interact with 
Windows using linux commands, but is not a full fledged OS like WSL with Ubuntu), to connect AWS to add a Ubuntu backend.
- After he has provisioned a Ubuntu instance from AWS, it is as if he is using Ubuntu from within his mingw64 terminal. Instead we are using WSL's Ubuntu terminal. 
- Consider that you already have done the above 2 steps and using Ubuntu via WSL instead of AWS, and are at the 5:18 min timestamp, and can now proceed from here. Only instead of anaconda,
you will install pipenv for the MLZoomcamp videos. The rest of the video will be the same for you, and it covers setting up
Docker nicely. Connecting to VScode and jupyter is a bit different as you'll see in the tutorials, and easier in the case of jupyter because pasting the token 
in the browser will directly open it, no port forwarding needed.



### FAQ:

1. Should I use pipenv alone to create environments? 
   - No. Without any environment, pipenv will be bound to system python, so any upgrade to python can potentially break a pipenv environment. 
   - We should either use it with pyenv (to manage different python versions)
   - Or use it with anaconda/miniconda, and use a pipenv environment inside of a anaconda environment with the required python version. 
   - There are multiple other options. [This](https://towardsdatascience.com/python-environment-101-1d68bda3094d) article here explains some of them.
   - Only pipenv is a MUST becuase it creates the pipfile.lock we need for our Docker container. Another advantage is that we can install ALL python packages using this pipenv (pipenv replaces pip). (In anaconda, packages are first installed using conda. If they are not available via conda, then they can be installed via pip, but this can sometimes cause conflicts. Pipenv skips all these troubles.)

2. Where does pipenv create environments and how does it name them?
   - It created them in pipenv installs packages in ~/.local/share/virtualenvs/ and names them after the folder directory where from where we used the pipenv install command. E.g. If my folder path is ~/home/mona/Churn-Flask-app, and I `cd` to it, and use `pipenv install <package>`, it will create an environment named Churn-Flask-app-some_random_characters, and I can see a path like this: /home/mona/.local/share/virtualenvs/churn-flask-app-i_mzGMjX. All libraries will be installed inside this folder. To activate this environment, I will need to cd into the project folder again, and type `pipenv shell`. The location of the project folder acts as an idetifier for the environment we are working in, in place of any name.


3. Do I need to install both Docker Desktop for Windows and install Docker manually on WSL? 
   - No, not needed. Installing Docker Desktop for windows will make the docker command accessible inside WSL. It is also easier to install. However, if you want to install docker directly from bash in WSL, uninstall Docker Desktop completely first. 

4. Do we need to create Docker image inside an environment? 
   - No, not necessary. It can be created directly outside of any environment.

5. What are 0.0.0.0 and 127.0.0.1? 
   - 0.0.0.0 is a placeholder IP which can mean: Use any IP available. 127.0.0.1 is localhost IP (a reserved IP) which refers to the host OS iteself. On Windows, this IP will refer to localhost which is Windows. On WSL, this IP will refer to Ubuntu.

6. Can I map multiple IPs to the same port inside a single OS? 
   - No, this will not work. Map the new IP to any of the available, unused ports. 

7. If your main concern isn't following along the videos, how much of these steps can be done in Windows alone, without using WSL? 
   - Everything from step 1-6 can be done in Windows. Install pipenv inside an anaconda environment. For step 7, WSL is needed but the Docker container can be completely created with Docker Desktop. Step 8 onwards can again be done in Windows. (Summary: Docker containers can be only be created in a Linux system e.g. Ubuntu, MacOS) but they can be deployed in any OS.

