# How usage flask-boilerpate

## Clone Repository

```
git clone git@github.com:jrdiniz/flask-boilerplate.git . 
```

## Create Virtual Environment

I have test this project with 3.10, with you test with another version, please open a pull request to update the documentation.

```
python3.10 -m venv env
```

## Install Dependencies 

```
source env/bin/active
pip install -r requirements.txt
```

## Environment Configuration

The project use python-dotenv library, so you need create an .env file on root directory of the project:

 - Development Environment 

```
FLASK_APP=app
FLASK_DEBUG=True
FLASK_CONFIG_FILE=config.DevelopmentConfig
SECRET_KEY=<your-secret-key>

```

 - Production Environment

```
FLASK_APP=app
FLASK_DEBUG=False
FLASK_CONFIG_FILE=config.ProductionConfig
SECRET_KEY=<your-secret-key>

```

# Library

 - Bootstrap 5.3.3
 - Bootstrap Icons 1.11.3
 - HTMX 1.9.10

## Deploy using Ansible

