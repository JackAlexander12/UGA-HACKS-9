from pymongo import MongoClient
from twilio.rest import Client

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
orders_collection = db['orders']

# Function to send the agreement to the buyer
def agreement_sms(location, time, price, buyer_phone_number):
    # Construct the agreement message
    agreement_message = f"Agreement Details:\n\n"
    agreement_message += f"Location: {location}\n"
    agreement_message += f"Time: {time}\n"
    agreement_message += f"Price: {price}\n\n"
    agreement_message += "Please confirm your agreement to these terms."

    # Send the agreement message to the buyer using Twilio (replace with your Twilio credentials)
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    twilio_phone_number = "your_twilio_phone_number"

    client_twilio = Client(account_sid, auth_token)

    message = client_twilio.messages.create(
        body=agreement_message,
        from_=twilio_phone_number,
        to=buyer_phone_number
    )

    return "Agreement sent successfully."

# Refund
def authorize_refund(buyer_name, seller_name, order_number, refund_amount):
    # Simulate the refund (In MongoDB, you'd update the order document)
    print(f"Authorizing refund for order {order_number} from {seller_name} to {buyer_name}")
    print(f"Refund amount: ${refund_amount}")
    print("Refund authorized!")

# Partial refund
def partial_return(order_id):
    # Retrieve the order from MongoDB
    order = orders_collection.find_one({'_id': order_id})

    if not order:
        return "Order not found."

    # Calculate the refund amount (20% of total paid amount)
    total_paid_amount = sum(item['price'] * item['quantity'] for item in order['items'])
    refund_amount = total_paid_amount * 0.2  # 20% refund

    # Update the order status and refund amount
    orders_collection.update_one({'_id': order_id}, {'$inc': {'refund_amount': refund_amount}})

    return "Partial refund processed successfully."
