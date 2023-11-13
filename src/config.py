import os

from dotenv import load_dotenv

env_path = '.env'
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("API_KEY")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_SCHEMA_NAME = os.getenv("MYSQL_SCHEMA_NAME")

