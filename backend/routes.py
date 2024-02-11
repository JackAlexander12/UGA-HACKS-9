# routes.py

from flask import Flask, jsonify, request
from flask_cors import CORS
from database import DynamoDBManager
from models import User, Request

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

dynamo_manager = DynamoDBManager()

@app.route('/api/users', methods=['GET'])
def get_all_users():
    users = dynamo_manager.get_all_users()
    return jsonify(users)

@app.route('/api/users/<username>', methods=['GET'])
def get_user(username):
    user = dynamo_manager.get_user_item({'username': username})
    return jsonify(user)

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    
    new_user = User(username, password)
    dynamo_manager.put_user_item(vars(new_user))
    
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/api/requests', methods=['GET'])
def get_all_requests():
    requests = dynamo_manager.get_all_requests()
    return jsonify(requests)

@app.route('/api/requests/<request_id>', methods=['GET'])
def get_request(request_id):
    request_data = dynamo_manager.get_request_item({'request_id': int(request_id)})
    return jsonify(request_data)

@app.route('/api/requests', methods=['POST'])
def create_request():
    data = request.get_json()
    buyer_username = data.get('buyer_username')
    seller_username = data.get('seller_username')
    request_type = data.get('request_type')
    time = data.get('time')
    location = data.get('location')
    amount = data.get('amount')
    
    if not buyer_username or not seller_username or not request_type or not time or not location or not amount:
        return jsonify({'error': 'Missing required fields'}), 400
    
    new_request = Request(buyer_username, seller_username, request_type, time, location, amount)
    dynamo_manager.put_request_item(vars(new_request))
    
    return jsonify({'message': 'Request created successfully'}), 201

# Additional routes for updating and deleting data can be added as needed

if __name__ == '__main__':
    app.run(debug=True)
