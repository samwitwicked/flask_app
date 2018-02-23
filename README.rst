==========
flask_app
==========

Configuring the flask_app

Template used - pyscaffold

Description
===========

The purpose of the flask_app as part of the assignment 2 in Software Engineering is to import
the systeminfo package from GitHub and displaying the operating system of my machine on the
localhost 0.0.0.0/5000. The following are the instructions on how to use this flask_app.

INSTRUCTIONS:

Setting up the flask_app:

1) Downloaded the pyscaffold python project template to the working location. Chose this tool because it was easy to
install had a understandable template.

2) Opened into the src folder of the pyscaffold tool and created a new folder called flask_app. Inside that another
folder named a second 'flask_app' and the python file run.py.

3) The file 'run.py' was used to import the flask_app to connect to the localhost port 5000. And inside the 2nd
flask_app created a folder named 'templates' and two python files named views.py and '__init__.py'.

4) The templates folder had the index.html, which was used to print the output of platform details on the browser.

5) The file 'views.py' was used to display the platform details from importing systeminfo and connecting to the
index.html which shall display the platform details on the browser.

6) The '__init__.py' was used to import flask package which was installed in the computer and import the views.py.

In Terminal:

1) Import the systeminfo package from GitHub(using the git+http://github.com/samwitwicked/systeminfo.git).
in the working virtual environment inside the flask_app folder in src.

2) Open the systeminfo folder and then install all packages (using pip install -e .).

3) Get back to the home directory of the Virtual environment and now open the location where the folder flask_app
and the file run.py is present.

4) Run the file run.py (python run.py)

5) When the command is executed, copy the host url'http://0.0.0.0:5000/' and paste this url in the browser.

6) The browser will show the result of visiting http://localhost:5000. Displays the platform details. (Refer:'localhost screenshot'). 


Note
====

This project has been set up using PyScaffold 3.0.1. For details and usage
information on PyScaffold see http://pyscaffold.org/.
