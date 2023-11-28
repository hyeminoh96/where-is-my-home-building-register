from flask import Flask, request

from src.application.address_service import AddressService
from src.config import app_config, config_name
from src.infrastructure.db import db


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_ECHO'] = True

    db.init_app(app=app)
    return app


app = create_app(config_name)


# Comment out this after table creation
# with app.app_context():
#     db.create_all()


@app.route('/')
def hello_world():
    return 'Welcome!'


@app.route('/address/sido')
def get_sido():
    address_service = AddressService()
    sido_list = address_service.get_sido()
    return sido_list


@app.route('/address/sigungu')
def get_sigungu():
    sido = request.args.get('sido')
    address_service = AddressService()
    sigungu_list = address_service.get_sigungu(sido)
    return sigungu_list


@app.route('/address/bjdong')
def get_bjdong():
    sido = request.args.get('sido')
    sigungu = request.args.get('sigungu')
    address_service = AddressService()
    bjdong_list = address_service.get_bjdong(sido, sigungu)
    return bjdong_list


if __name__ == '__main__':
    app.run()
