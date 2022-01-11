from http import HTTPStatus
import time
import math

from flask import Flask
from flask import make_response

def n_factorial(count):
    for i in range(count):
        math.factorial(10000)


def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret_key'

    @app.route('/')
    def home():
        return make_response('Hello', HTTPStatus.OK)

    @app.route('/factorial', methods=["GET"])
    def factorial():

        start = time.time()
        n_factorial(count=2000)
        end = time.time()

        return make_response(f'{end-start:.3f}', HTTPStatus.OK)

    return app
