## Enviroment

The project use python-dotenv library, so you need the .env file on root directory of the project:

 - Develop Enviroment 

```
FLASK_APP=application
FLASK_ENV=development
FLASK_CONFIG_FILE=config.DevelopmentConfig
```

 - Production Enviroment

```
FLASK_APP=application
FLASK_ENV=production
FLASK_CONFIG_FILE=config.ProductionConfig
```

 - Testing Enviroment

```
FLASK_APP=application
FLASK_ENV=development
FLASK_CONFIG_FILE=config.TestingConfig
```
