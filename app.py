from flask import Flask, make_response, request
from detect import *
import requests

app = Flask(__name__)

@app.route('/api/<url>')
def detect(url):
    res = classify(url)
    return res


# @app.route('/api/phishing/register/<url>')
# def register(url):


# @app.route('/api/phishing/database', methods=['GET'])
# url 불러오기


# @app.route('/api/phishing/count', methods=['GET'])
#url 개수 반환



if __name__ == '__main__':
    app.run(debug=True)