import os


class Default:
    API_KEY = os.environ.get("API_KEY")
    MYSQL_HOST = os.environ.get("MYSQL_HOST")
    MYSQL_PORT = os.environ.get("MYSQL_PORT")
    MYSQL_USER = os.environ.get("MYSQL_USER")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
    MYSQL_SCHEMA_NAME = os.environ.get("MYSQL_SCHEMA_NAME")

    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_SCHEMA_NAME}'


app_config = {
    'development': Default(),
}

config_name = os.environ.get('FLASK_CONFIG', 'development')


def get_environment_variable(key: str):
    env = app_config[config_name]
    if env[key]:
        return env[key]
    else:
        raise Exception(f"Not Set Environment Variable :: {key}")
