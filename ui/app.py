# handles window setup and navigation
from tkinter import *
import tkinter as tk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.inventory import Inventory

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



root.mainloop()