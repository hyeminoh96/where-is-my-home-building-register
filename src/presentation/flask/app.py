from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/address/sido')
def get_sido():
    sido_list = address_service.get_sido()
    return


if __name__ == '__main__':
    app.run()
