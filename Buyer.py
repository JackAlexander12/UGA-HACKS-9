def create_agreement(time,location,price)::
     agreement = {
        "time": time,
        "location": location,
        "price":price   
        }
    return agreement

def agreement_display(agreement):
    agreement_details = f"Agreement Details:\n"
    agreement_details += f"Time: {agreement['time']}\n"
    agreement_details += f"Location: {agreement['location']}\n"
    agreement_details += f"Price: {agreement['price']}"
    return agreement_details




// Send confirmation through website to either sides phone and then confirm through text
