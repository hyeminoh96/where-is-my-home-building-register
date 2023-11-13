from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.config import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_SCHEMA_NAME

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PASSWORD}/{MYSQL_SCHEMA_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/address/sido')
def get_sido():
    sido_list = address_service.get_sido()
    return


if __name__ == '__main__':
    app.run()
