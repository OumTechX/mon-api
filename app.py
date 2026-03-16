from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_url = os.environ.get('MONGO_URL', 'mongo-service')
mongo_user = os.environ.get('MONGO_USERNAME', 'mongouser')
mongo_password = os.environ.get('MONGO_PASSWORD', 'mongopass')

client = MongoClient(
    host=mongo_url,
    port=27017,
    username=mongo_user,
    password=mongo_password
)

db = client['mydb']
users_collection = db['users']

@app.route('/')
def home():
    return jsonify({"message": "Mon API fonctionne", "status": "OK"})

@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}, {'_id': 0}))
    return jsonify({"users": users})

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    users_collection.insert_one(data)
    return jsonify({"message": "Utilisateur ajoute"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)