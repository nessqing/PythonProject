import sys

import flask
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return "flask init"
if __name__== "__main__":
    app.run();

