from flask import Flask, make_response, request, jsonify
from detect import *
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hnxkebxspmxljf:9046e46116eaa8d473c5f3f167399a45272a15f43b3e580502a7d4711bc823a9@ec2-54-156-151-232.compute-1.amazonaws.com:5432/d6v79c9c0m0r21
'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Phishing

@app.route('/')
def main():
    return "Phishing-Fishing"

@app.route('/api/phishing', methods=['POST'])
def detect():
    if request.method == 'POST':
        if request.is_json:
            data=request.get_json()
            url = data['url']
            res = str(classify(url))
            response = jsonify({
                'phishing' : res
            })
            response.status_code = 200
    return response


@app.route('/api/phishing/register', methods=['POST'])
def register():
    if request.method == 'POST' :
        if request.is_json:
            data=request.get_json()
            new_phishing = Phishing(url=data['url'])
            new_phishing.save()
            response = jsonify({
                'success' : 1
            })
        else : 
            response = jsonify({
                'success' : 0
            })
        response.status_code = 201
    return response



@app.route('/api/phishing/database', methods=['GET'])
def get_databases():
    phishings = Phishing.get_all()
    results = []

    for phishing in phishings:
        obj = {
            'url' : phishing.url
        }
        results.append(obj)
    response = jsonify(results)
    response.status_code = 200
    return response


@app.route('/api/phishing/count', methods=['GET'])
def get_counts():
    phishings = Phishing.get_all()
    count = len(phishings)
    response = jsonify({
        'count' : count
    })
    response.status_code = 200
    return response



if __name__ == '__main__':
    app.run(debug=True)