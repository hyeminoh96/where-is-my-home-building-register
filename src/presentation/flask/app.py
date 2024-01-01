from flask import Flask

from src.config import app_config, config_name
from src.infrastructure.db import db
from src.presentation.flask.address_router import address
from src.presentation.flask.building_register_router import register


def create_app(config_name):
    app = Flask(__name__)
    # Register blueprints
    app.register_blueprint(address)
    app.register_blueprint(register)

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


if __name__ == '__main__':
    app.run()
