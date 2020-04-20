WELCOME! 

Here we will explore from start to finish the basics of Python. We will use Python3, so let's download and install it!

We will use python 3.6.8 because it has a lot of support across libraries and has all of the installers available across all systems.
https://www.python.org/downloads/release/python-368/


Step 1:
    Choose your installer: Scroll down until you see a section called "Files".
    Locate what type of system you have.
    NOTE: 
    Mac(OSX) - look at description for your version. You can compare this version by clicking the apple button on the top left corner of your screen and click "About This Mac" The version should be near the bottom.
    Windows - use "Windows x86-64 executable installer" and follow the instructions.

Step 2:
    Make sure you can access your python. Open a terminal.
    Mac - /Applications/Utilities/Terminal.app
    Windows - C:\Windows\System32\cmd.exe

Step 3:
    type "python" (no quotes). If this does not work, try "python3" or "python36"

    Still not working? The installer must have not assigned your Environment variables.
    https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html

    Mac - 

    Open Terminal.app;
    Open the file ~/.bash_profile in your text editor – e.g. atom ~/.bash_profile;
    Add the following line to the end:
    export PYTHONPATH="/Users/my_user/code"
    Save the file.
    Close Terminal.app;
    Start Terminal.app again, to read in the new settings, and type this:
    echo $PYTHONPATH
    It should show something like /Users/my_user/code.

    Windows - 

    Got to the Windows menu, right-click on “Computer” and select “Properties”:
    From the computer properties dialog, select “Advanced system settings” on the left:
    From the advanced system settings dialog, choose the “Environment variables” button:
    In the Environment variables dialog, click the “New” button in the top half of the dialog, to make a new user variable:
    Give the variable name as PYTHONPATH and the value is the path to the code directory. Choose OK and OK again to save this variable.
    Now open a cmd Window (Windows key, then type cmd and press Return). Type:
    echo %PYTHONPATH% to confirm the environment variable is correctly set.
    If you want your IPython sessions to see this new PYTHONPATH variable, you’ll have to restart your terminal and restart IPython so that it picks up PYTHONPATH from the environment settings.

    Now quit and start the terminal app again. The python commands mentioned at the beginning of Step 3: should be working now.

Let's get started! Follow the tutorials in each folder listed.