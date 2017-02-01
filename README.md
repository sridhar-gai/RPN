# RPN
This is a demo project created to learn about development practices in SCRUM

Required software/packages:
Python==2.7.11
Django==1.10.5
behave==1.2.5
pytest==3.0.6
selenium==3.0.2
Firefox > 50
Gecko driver 1.3+ for Mozilla/Windows (versioned under resources directory)

For non-windows OS, please download the latest gecko driver here:
https://github.com/mozilla/geckodriver/releases

Installation & Configuration:
1. Install python 2.7.11
2. After installing python, the easiest way to install other python packages is to use pip.
   To do this, you need to have install pip (python package manager) first.
   Refer to this page to install pip: https://pip.pypa.io/en/stable/installing/
3. Once pip is installed, you can just install the required python packages by executing the following commands.
    pip install Django==1.10.5
    pip install behave==1.2.5
    pip install pytest==3.0.6
    pip install selenium==3.0.2
4. Install firefox (>50)
5. Copy/download the gecko driver 
6. Add the location of the geckodriver to PATH environment variable.
    In windows, set PATH=%PATH%;"path\to\gecko\driver"
    In linux, export PATH=$PATH:/path/to/gecko/driver

Running the project:
Note: <project_dir> = /path/to/RPN
In shell/command prompt, go to <project_dir>/web/rpnui & execute
    python manage.py runserver
    This will bring up the django server on port 8000.
    You should be able to access the RPN calculator page via http://127.0.0.1:8000/calculate

Running the unit tests:
To run the unit tests, go to <project_dir>/ & execute
    pytest tests/business/test.py
    You can see the test results
    
Running the acceptance/feature based tests:
To run the acceptance tests, go to <project_dir>/tests & execute
    behave
    You can see the selenium tests getting executed in firefox.
    From the terminal, you can check the result of the acceptance tests.
