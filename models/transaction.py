# For stock updates, logging
from .product import Product

class Transaction:
    def __init__(self, transaction_id, product_id, user_id, quantity, transaction_type, timestamp):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.timestamp = timestamp
        self.product_id = product_id
        self.user_id = user_id
        self.quantity = quantity
        