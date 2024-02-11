class Request:
    def __init__(self, buyer_username, seller_username, request_type, time, location, amount):
        self.buyer_username = buyer_username
        self.seller_username = seller_username
        self.type = request_type  # "buy" or "sell"
        self.time = time
        self.location = location
        self.amount = amount
        self.agreement_status = False
        self.location_status = False
