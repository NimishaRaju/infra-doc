# infra-doc project
For a given server the app collects the health information of the server and displays it to the user
# Prerequisites 
Before setting up the project, ensure you have the following installed on your local machine:
* Python (version 3.11 or higher)
* Git

Create and activate virtual environment and then run pip install -r requirements.txt to install the pkgs --these are required for running pytest

# Project Structure
```
infra-doc/
    ├── app
        ├──__init__.py 
        ├──config.toml               # general app configuration
        ├──healthcheck.py            # checks the health of various server components
        ├──logging_config.py          #logging configuration initial setup
        ├──main.py                   #application entrypoint
    └── tests/
        ├── __init__.py
        ├── test_health.py #pytest to test healthcheck module
    ├── .gitignore
    ├── Dockerfile                        
    ├── README.md             # Project documentation
    ├── requirements.txt             # Packages to be installed
```