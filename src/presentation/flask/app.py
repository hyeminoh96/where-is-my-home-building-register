from flask import Flask
from sqlalchemy import text

from src.application.address_service import AddressService
from src.config import app_config, config_name
from src.domain.address import Address, db


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    db.init_app(app=app)
    return app


app = create_app(config_name)

# Comment out this after table creation
with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
    result = db.session.execute(text('SELECT 1'))
    one = result.first()
    return one


@app.route('/address/sido')
def get_sido():
    address_service = AddressService()
    sido_list = address_service.get_sido()
    return sido_list


if __name__ == '__main__':
    app.run()
