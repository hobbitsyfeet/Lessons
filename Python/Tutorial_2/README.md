Pip is a very useful collection of python packages for free use. Many of these packages are created and posted on github, so there should be some documentation to follow. 

Here, I will show you how to create a python environment (a place to store and download your packages independently of each project) and use some very common and useful packages. 

How do we get Pip?
        Linux - sudo apt install python3-pip

        #Run this command in this folder. Use the python command you've been using from the beginning.
        Mac & Windows - python3 get-pip.py

How do we set up an environment to work in for this project?

Since we are most likely going to use the same python in all of our projects here, we will create an environement in Lessons/Python/

To do this, go to that directory. (From here type in cd ../) NOTE: cd stands for 'change directory'

When we are in Python/ (you can check by typing 'pwd' on linux/mac or just typing 'cd' on windows)

We will type 'python3 -m pip install virtualenv'
we will create an environment named 'env' by typing 'python3 venv ./env' This will take a bit as it's setting up the environment.

We will enter the environment and activate it.

Mac & linux - '. ./env/bin/activate'
Windows - './env/Source/activate'


You should see (env) before your input in your terminal, this is how you know you've done this properly.

To install the packages used for these tutorials, type 'python3 -m pip install -r requirments.txt'

This is just a simple list of packages, exactly how you would install them individually with pip, but it recursively goes through and installs them one by one. This is a handy way to install dependencies.