from MySQLdb import create_engine
from MySQLdb import session maker
from models import Order
from twilio.rest import Client  


# Change the Username,Password, host , and database
engine = create_engine('mysql+pymysql://username:password@host/database')


#Function in order to send the agreement to the buyer



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

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=agreement_message,
        from_=twilio_phone_number,
        to=buyer_phone_number
    )

    return "Agreement sent successfully."




#Refund
def authorize_refund(buyer_name, seller_name, order_number, refund_amount):
    #simulate the refund
    print(f"Authorizing refund for order {order_number} from {seller_name} to {buyer_name}")
    print(f"Refund amount: ${refund_amount}")
    print("Refund authorized!")



 def partial_return(order_id):
    # Connect to the MySQL database
    # Change the Username,Password, host , and database
    engine = create_engine('mysql+pymysql://username:password@localhost/database_name')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the order from the database
    order = session.query(Order).filter(Order.id == order_id).first()

    if not order:
        return "Order not found."

    # Calculate the refund amount (20% of total paid amount)
    total_paid_amount = sum(item.price * item.quantity for item in order.items)
    refund_amount = total_paid_amount * 0.2  # 20% refund

    # Update the order status and refund amount
    order.refund_amount += refund_amount
    session.commit()
