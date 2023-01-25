# How usage flask-boilerpate

## Clone Repository

```
git clone git@github.com:jrdiniz/flask-boilerplate.git . 
```

## Create Virtual Environment

I have test this project with 3.8, with you test with another version, please open a pull request to update the documentation.

```
python3.6 -m venv env
```
or
```
python3.8 -m venv env
``` 

## Install Dependencies 

```
source env/bin/active
pip install -r requirements.txt
```

## Environment Configuration

The project use python-dotenv library, so you need the .env file on root directory of the project:

 - Development Environment 

```
FLASK_APP=app
FLASK_DEBUG=True
FLASK_CONFIG_FILE=config.DevelopmentConfig
```

 - Production Enviroment

```
FLASK_APP=app
FLASK_DEBUG=False
FLASK_CONFIG_FILE=config.ProductionConfig
```

 - Testing Enviroment

```
FLASK_APP=app
FLASK_DEBUG=True
FLASK_CONFIG_FILE=config.TestingConfig
```

## Deploy using Ansible

