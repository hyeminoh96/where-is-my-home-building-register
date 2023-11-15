from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.config import app_config, config_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    db = SQLAlchemy(app=app)
    db.create_all()
    return app


app = create_app(config_name)


@app.route('/')
def hello_world():
    return 'Hello World!'


# @app.route('/address/sido')
# def get_sido():
#     sido_list = address_service.get_sido()
#     return


if __name__ == '__main__':
    app.run()
