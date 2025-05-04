 # Entry point: handles program flow

from models.inventory import Inventory

inv = Inventory()
inv.add_product("Milk", 2.49, "Dairy", 20)
inv.add_product("Eggs", 3.99, "Dairy", 12)

for pid, product in inv.products.items():
    print(f"ID: {pid}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

inv.total_inventory_value()

inv.total_inventory_count()

inv.adjust_product_price(2, 3.49)

for pid, product in inv.products.items():
    print(f"ID: {pid}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
