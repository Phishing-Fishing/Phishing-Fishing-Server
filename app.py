from flask import Flask, make_response, request
from detect import *
import requests

app = Flask(__name__)

@app.route('/')
def detect():

    res = classify()
    return res


if __name__ == '__main__':
    app.run(debug=True)