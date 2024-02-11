# controller.py

from models import User, Request
from database import DynamoDBManager

dynamo_manager = DynamoDBManager()

def create_request(username, target_username, request_type, time, location, amount):
    if request_type not in ["buy", "sell"]:
        print("Invalid request type. Please use 'buy' or 'sell'.")
        return

    # Check if the target user exists
    target_user = dynamo_manager.get_user_item({'username': target_username})
    if not target_user:
        print(f"User {target_username} not found.")
        return

    # Create the request
    request = Request(username, target_username, request_type, time, location, amount)
    dynamo_manager.put_request_item(vars(request))

    print(f"Request created successfully: {request}")

def get_requests_by_user(username):
    user_requests = dynamo_manager.get_requests_by_user(username)
    if user_requests:
        print(f"Requests for {username}:")
        for request in user_requests:
            print(request)
    else:
        print(f"No requests for {username}")

