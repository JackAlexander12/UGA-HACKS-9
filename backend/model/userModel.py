import pymongo
from twilio.rest import Client

# Establish MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["marketplace"]

# Define collections
buyers_collection = db["buyers"]
sellers_collection = db["sellers"]

# Twilio credentials
account_sid = "your_account_sid"
auth_token = "your_auth_token"
twilio_phone_number = "your_twilio_phone_number"

# Twilio client
twilio_client = Client(account_sid, auth_token)

def send_confirmation_code(phone_number, confirmation_code):
    message_body = f"Your confirmation code: {confirmation_code}"
    twilio_client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=phone_number
    )

if __name__ == "__main__":
    # Create a new buyer
    new_buyer_data = {
        "username": "buyer_username",
        "email": "buyer@example.com",
        "password": "buyer_password",
        "phone_number": "+1234567890"  # Add buyer's phone number here
    }
    buyers_collection.insert_one(new_buyer_data)
    print("New buyer added successfully.")
    send_confirmation_code(new_buyer_data['phone_number'], "123456")  # Send confirmation code to buyer

if __name__ == "__main__":
    # Create a new seller
    new_seller_data = {
        "username": "seller_username",
        "email": "seller@example.com",
        "password": "seller_password",
        "phone_number": "+9876543210"  # Add seller's phone number here
    }
    sellers_collection.insert_one(new_seller_data)
    print("New seller added successfully.")
    send_confirmation_code(new_seller_data['phone_number'], "654321")
