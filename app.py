from flask import Flask, make_response, request, jsonify
from detect import *
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/phishing-fishing'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Phishing


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