# handles window setup and navigation
from tkinter import *
import tkinter as tk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.inventory import Inventory
from datetime import datetime


inv = Inventory()
root = tk.Tk()
menu = Menu(root)
root.geometry("600x400")
root.title('Inventory Management System')
root.config(menu=menu)
filemenu = Menu(menu)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)


# ** NAVBAR ***
menu.add_cascade(label='Home')
menu.add_cascade(label='Inventory')
menu.add_cascade(label='Products')
menu.add_cascade(label='Users')


# *** TESTING DATA ***
inv.add_product("Test Product", 10.0, "Category A", 5)
inv.add_user("dyana", "admin")
inv.add_user("aya", "cashier")

inv.add_product("Apple", 0.50, "Fruit", 100)     # product_id = 1
inv.add_product("Notebook", 2.00, "Stationery", 50)  # product_id = 2

inv.record_transaction(1, 1, 15, "purchase")  # Apple: restock 15
inv.record_transaction(1, 2, 15, "purchase")  # Notebook: restock 15
inv.record_transaction(1, 1, 10, "sale")  # Apple: sell 10
inv.record_transaction(2, 2, 5, "sale")   # Notebook: sell 5
inv.record_transaction(2, 2, 5, "return")     # Notebook: return 5

# *** DASHBOARD/HOME ***

# grab info from function to display
def display_totals():
    result_total_products = inv.total_inventory_count()
    total_products.config(text=result_total_products)
    
    result_total_value= inv.total_inventory_value()
    total_value.config(text=result_total_value)
    
    result_total_users = inv.total_user_count()
    total_users.config(text=result_total_users)

# dyanmic labels
total_products = tk.Label(root, text="")
total_products.grid(row=0, column=0)
total_value = tk.Label(root, text="")
total_value.grid(row=0, column=1)
total_users = tk.Label(root, text="")
total_users.grid(row=0, column=2)

# total labels
total_products_label = tk.Label(root, text='Total Products')
total_products_label.grid(row=1, column=0)
total_value_label = tk.Label(root, text='Total Value')
total_value_label.grid(row=1, column=1)
total_users_label = tk.Label(root, text='Total Users')
total_users_label.grid(row=1, column=2)

# schedules funtion to run after a delay to display results automatically
root.after(1000, display_totals)


# display recent transactions
recent_transactions_frame = tk.Frame(root)
recent_transactions_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

scrollbar = Scrollbar(recent_transactions_frame, orient=VERTICAL)
scrollbar.grid(row=3, column=1, sticky='ns')

recent_transactions_list = Listbox(recent_transactions_frame, yscrollcommand=scrollbar.set, width=80,
    height=8)
recent_transactions_list.grid(row=3, column=0) 

scrollbar.config(command=recent_transactions_list.yview)
    
recent_transactions_label = tk.Label(root, text="Recent Transactions:")
recent_transactions_label.grid(row=2, column=0, pady=(10, 0), sticky="w")

def display_recent_transactions():
    result = inv.recent_transactions()
    for transaction in result:
         recent_transactions_list.insert(0, f"Type: {transaction.transaction_type } | Time: {transaction.timestamp} | User: {transaction.user_id}")

root.after(1000, display_recent_transactions)

# display recent added products
recent_products_frame = tk.Frame(root)
recent_products_frame.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

product_scrollbar = Scrollbar(recent_products_frame, orient=VERTICAL)
product_scrollbar.grid(row=0, column=1, sticky='ns')

recent_products_list = Listbox(
    recent_products_frame,
    yscrollcommand=product_scrollbar.set,
    width=80,
    height=8
)
recent_products_list.grid(row=0, column=0)
product_scrollbar.config(command=recent_products_list.yview)

recent_products_label = tk.Label(root, text="Recently Added Products:")
recent_products_label.grid(row=2, column=1, pady=(10, 0), sticky="w")

def display_recent_products():
    result = inv.recent_products()
    for product in result:
         recent_products_list.insert(0, f"{product.name } | Qty: {product.quantity} | Price: ${product.price}")

root.after(1000, display_recent_products)


root.mainloop()