# Product class
class Product:
    def __init__(self, product_id, name, category, quantity, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
    
    def update_stock(self, new_quantity):
        self.quantity = new_quantity
        return self.quantity
    
    def adjust_price(self, new_price):
        self.price = new_price
        return self.price