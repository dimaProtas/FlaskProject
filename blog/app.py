from time import time
from flask import Flask, request, g
from werkzeug.exceptions import BadRequest


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Главная страничка</h1>"


