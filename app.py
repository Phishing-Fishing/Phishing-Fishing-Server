from flask import Flask, make_response, request
import requests

app = Flask(__name__)

@app.route('/')
def detect():
    return 'detect result'


if __name__ == '__main__':
    app.run(debug=True)