from flask import Flask, make_response, request
from detect import *
import requests

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def detect():
    url = request.args.get('url')

    res = classify()
    return res


@app.route('/api/phishing/register', methods=['GET'])
def register():
    url = request.args.get('url')


# @app.route('/api/phishing/database', methods=['GET'])
# url 불러오기


# @app.route('/api/phishing/count', methods=['GET'])
#url 개수 반환



if __name__ == '__main__':
    app.run(debug=True)