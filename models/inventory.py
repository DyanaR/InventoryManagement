# Inventory manager class
from .product import Product

class Inventory:
    def __init__(self):
        # only set up the initial state 
        self.products = {}
        self.next_id = 1
        
    def add_product(self, name, price, category, quantity):
        new_product = Product(self.next_id, name, category, quantity, price)
        # new_product is stored in value as an object which is a reference in memory
        self.products[self.next_id] = new_product
        self.next_id += 1
    
    def remove_product(self, product_id):
        try:
            self.products.pop(product_id)
        # using except will catch all errors
        # we dont want that
        # except:
        #     print("Item does not exist")
        # for now we care about the specific case where product_id is missing
        except KeyError:
            print("Item does not exist")
    
    # return object instead of printing later
    def get_product(self, product_id):
        current_product = None
        if product_id in self.products:
            current_product = self.products.get(product_id) 
            print(f"Name: {current_product.name}, Price: {current_product.price}")
        # incase theres not product with that id (current_product being None)
        else:
            print("Item not found.")
    
    def list_all_products(self):
        if not self.products:
            print("No items yet.")
        else:
            for product in self.products.values():
                print(f"Name: {product.name}, Price: {product.price}")
            
    def update_product_stock(self, product_id, new_quantity): 
        # grabs the Product object we need, so dont have to make an instance
        # to use Product class method
        product = self.products.get(product_id)            
        if product:
            product.update_stock(new_quantity)
        else:
            print("Item doesn't exist.")
    
    # encapsulation: Product keeps its price private to itself
    #                instead of changing price directly we use its method
    # abstraction: no need to know how Product updates its price internally 
    #              just that update_price() handles it, hiding interanl logic from Inventory
    def adjust_product_price(self, product_id, new_price):
        product = self.products.get(product_id)
        if product:
            product.update_price(new_price)
        else:
            print("Item doesn't exist.")
    
    def total_inventory_count(self):
        inv_count = len(self.products)
        print(f"Total Inventory: {inv_count}")
    
    def total_inventory_value(self):
        total = 0
        for product in self.products.values():
            total = product.price * product.quantity
        print(f"Inventory Total: ${total}")