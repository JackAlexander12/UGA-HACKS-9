import random
import string
import requests

def generate_confirmation_code(length=6):
    """Generate a random confirmation code."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def agreement_display(agreement):
    agreement_details = f"Agreement Details:\n"
    agreement_details += f"Time: {agreement['time']}\n"
    agreement_details += f"Location: {agreement['location']}\n"
    agreement_details += f"Price: {agreement['price']}"
    return agreement_details

def agreement_sms(location, time, price, buyer_phone_number):
    # Generate confirmation code
    confirmation_code = generate_confirmation_code()

    # Construct the agreement message
    agreement_message = f"Agreement Details:\n\n"
    agreement_message += f"Location: {location}\n"
    agreement_message += f"Time: {time}\n"
    agreement_message += f"Price: {price}\n\n"
    agreement_message += f"Please confirm your agreement by clicking the following link: https://yourwebsite.com/confirm?code={confirmation_code}"

    # Trigger the function deployed using Twilio Serverless
    twilio_function_url = "YOUR_DEPLOYED_FUNCTION_URL"  # Replace with your deployed function URL
    payload = {
        "body": agreement_message,
        "to": buyer_phone_number
    }
    response = requests.post(twilio_function_url, json=payload)

    if response.status_code == 200:
        return "Agreement sent successfully."
    else:
        return "Failed to send agreement."


agreement = create_agreement(time, location, price)
print(agreement_display(agreement))
print(agreement_sms(location, time, price, buyer_phone_number))
