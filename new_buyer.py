import twilio wilio CLI and Twilio Serverless plugin 




def create_agreement(time, location, price):
    agreement = {
        "time": time,
        "location": location,
        "price": price   
    }
    return agreement

def agreement_display(agreement):
    agreement_details = f"Agreement Details:\n"
    agreement_details += f"Time: {agreement['time']}\n"
    agreement_details += f"Location: {agreement['location']}\n"
    agreement_details += f"Price: {agreement['price']}"
    return agreement_details

# Send confirmation through website to either side's phone and then confirm through text
from twilio.rest import Client
import random
import string

def generate_confirmation_code(length=6):
    """Generate a random confirmation code."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def agreement_sms(location, time, price, buyer_phone_number):
    # Generate confirmation code
    confirmation_code = generate_confirmation_code()

    # Construct the agreement message
    agreement_message = f"Agreement Details:\n\n"
    agreement_message += f"Location: {location}\n"
    agreement_message += f"Time: {time}\n"
    agreement_message += f"Price: {price}\n\n"
    agreement_message += f"Please confirm your agreement by clicking the following link: https://yourwebsite.com/confirm?code={confirmation_code}"

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
