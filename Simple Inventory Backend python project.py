import tkinter as tk
from tkinter import messagebox


# ==========================================
# OOP: Product Class
# ==========================================

class Product:

    # Built-in class attribute
    category = "General Products"

    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_value(self):
        return self.price * self.quantity

    def get_details(self):
        return (
            self.product_id,
            self.name,
            self.price,
            self.quantity
        )


# ==========================================
# Dictionary: Store Products
# ==========================================

products = {}


# ==========================================
# Set: Store Product Categories
# ==========================================

categories = set()


# ==========================================
# Function: Add Product
# ==========================================

def add_product():

    try:

        product_id = id_entry.get()
        name = name_entry.get()
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())

        if product_id == "" or name == "":
            raise ValueError("Please enter all product details")

        if price <= 0:
            raise ValueError("Price must be greater than zero")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if product_id in products:
            raise ValueError("Product ID already exists")

        product = Product(
            product_id,
            name,
            price,
            quantity
        )

        products[product_id] = product

        categories.add(Product.category)

        messagebox.showinfo(
            "Success",
            "Product added successfully!"
        )

        clear_fields()

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# ==========================================
# Function: Display Products
# ==========================================

def view_products():

    try:

        if len(products) == 0:
            raise ValueError("No products available")

        output = ""

        # List
        product_list = list(products.values())

        # Range
        for i in range(len(product_list)):

            product = product_list[i]

            output += (
                f"Product {i + 1}\n"
                f"ID: {product.product_id}\n"
                f"Name: {product.name}\n"
                f"Price: ₹{product.price}\n"
                f"Quantity: {product.quantity}\n"
                f"Total Value: ₹{product.get_total_value()}\n"
                f"-------------------------\n"
            )

        messagebox.showinfo(
            "Product List",
            output
        )

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# ==========================================
# Function: Search Product
# ==========================================

def search_product():

    try:

        product_id = id_entry.get()

        if product_id not in products:
            raise ValueError("Product not found")

        product = products[product_id]

        details = product.get_details()

        output = f"""
Product ID: {details[0]}
Product Name: {details[1]}
Price: ₹{details[2]}
Quantity: {details[3]}
Total Value: ₹{product.get_total_value()}
"""

        messagebox.showinfo(
            "Product Details",
            output
        )

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# ==========================================
# Function: Delete Product
# ==========================================

def delete_product():

    try:

        product_id = id_entry.get()

        if product_id not in products:
            raise ValueError("Product not found")

        del products[product_id]

        messagebox.showinfo(
            "Success",
            "Product deleted successfully!"
        )

        clear_fields()

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# ==========================================
# Function: Clear Input Fields
# ==========================================

def clear_fields():

    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)


# ==========================================
# Tkinter GUI
# ==========================================

root = tk.Tk()

root.title("Inventory Management System")

root.geometry("500x600")


# Title
title_label = tk.Label(
    root,
    text="INVENTORY MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=20)


# Product ID
tk.Label(
    root,
    text="Product ID"
).pack()

id_entry = tk.Entry(root)

id_entry.pack(pady=5)


# Product Name
tk.Label(
    root,
    text="Product Name"
).pack()

name_entry = tk.Entry(root)

name_entry.pack(pady=5)


# Price
tk.Label(
    root,
    text="Price"
).pack()

price_entry = tk.Entry(root)

price_entry.pack(pady=5)


# Quantity
tk.Label(
    root,
    text="Quantity"
).pack()

quantity_entry = tk.Entry(root)

quantity_entry.pack(pady=5)


# Buttons
tk.Button(
    root,
    text="Add Product",
    width=25,
    command=add_product
).pack(pady=10)


tk.Button(
    root,
    text="View Products",
    width=25,
    command=view_products
).pack(pady=5)


tk.Button(
    root,
    text="Search Product",
    width=25,
    command=search_product
).pack(pady=5)


tk.Button(
    root,
    text="Delete Product",
    width=25,
    command=delete_product
).pack(pady=5)


tk.Button(
    root,
    text="Clear Fields",
    width=25,
    command=clear_fields
).pack(pady=5)


# Start application
root.mainloop()