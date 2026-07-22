# ============================================================
# ONLINE FOOD ORDER MANAGEMENT SYSTEM
# ============================================================

import tkinter as tk
from tkinter import messagebox


# ============================================================
# BASIC DATA TYPES
# ============================================================

restaurant_name = "ABC Food Restaurant"  # String
restaurant_code = 101                    # Integer
tax_rate = 5.0                           # Float
restaurant_open = True                   # Boolean


# ============================================================
# TUPLE
# ============================================================

FOOD_CATEGORIES = (
    "Pizza",
    "Burger",
    "Biryani",
    "Drinks",
    "Dessert"
)


# ============================================================
# LIST
# ============================================================

orders = []


# ============================================================
# SET
# ============================================================

unique_customers = set()


# ============================================================
# DICTIONARY
# ============================================================

restaurant_statistics = {
    "total_orders": 0,
    "total_sales": 0.0
}


# ============================================================
# OOP - FOOD ORDER CLASS
# ============================================================

class FoodOrder:
    """
    FoodOrder class for managing customer food orders.
    """

    restaurant = "ABC Food Restaurant"

    def __init__(
        self,
        order_id,
        customer_name,
        food_name,
        quantity,
        price
    ):

        self.order_id = order_id
        self.customer_name = customer_name
        self.food_name = food_name
        self.quantity = quantity
        self.price = price

    def calculate_total(self):

        return self.quantity * self.price

    def display_order(self):

        total = self.calculate_total()

        return (
            f"Order ID: {self.order_id}\n"
            f"Customer: {self.customer_name}\n"
            f"Food: {self.food_name}\n"
            f"Quantity: {self.quantity}\n"
            f"Price: ₹{self.price:.2f}\n"
            f"Total: ₹{total:.2f}\n"
        )

    def __str__(self):

        return (
            f"{self.order_id} - "
            f"{self.customer_name}"
        )


# ============================================================
# BUILT-IN CLASS ATTRIBUTES
# ============================================================

print(
    "Class Name:",
    FoodOrder.__name__
)

print(
    "Class Module:",
    FoodOrder.__module__
)

print(
    "Class Documentation:",
    FoodOrder.__doc__
)


# ============================================================
# FUNCTION: ADD ORDER
# ============================================================

def add_order(
    order_id,
    customer_name,
    food_name,
    quantity,
    price
):

    try:

        if order_id == "":

            raise ValueError(
                "Order ID cannot be empty."
            )

        if customer_name == "":

            raise ValueError(
                "Customer name cannot be empty."
            )

        # Convert quantity to integer
        quantity = int(quantity)

        if quantity <= 0:

            raise ValueError(
                "Quantity must be greater than zero."
            )

        # Convert price to float
        price = float(price)

        if price <= 0:

            raise ValueError(
                "Price must be greater than zero."
            )

        # Check duplicate order ID
        for order in orders:

            if (
                order.order_id
                == order_id
            ):

                raise ValueError(
                    "Order ID already exists."
                )

        # Create object
        order = FoodOrder(
            order_id,
            customer_name,
            food_name,
            quantity,
            price
        )

        # Add to list
        orders.append(order)

        # Add customer to set
        unique_customers.add(
            customer_name
        )

        # Update dictionary
        restaurant_statistics[
            "total_orders"
        ] += 1

        restaurant_statistics[
            "total_sales"
        ] += order.calculate_total()

        return True, "Order added successfully."

    except ValueError as error:

        return False, str(error)


# ============================================================
# FUNCTION: VIEW ALL ORDERS
# ============================================================

def view_all_orders():

    if len(orders) == 0:

        return "No orders found."

    output = ""

    # RANGE
    for index in range(len(orders)):

        output += (
            f"\nOrder {index + 1}\n"
        )

        output += "=" * 40

        output += "\n"

        output += (
            orders[index]
            .display_order()
        )

    return output


# ============================================================
# FUNCTION: SEARCH ORDER
# ============================================================

def search_order(order_id):

    for order in orders:

        if (
            order.order_id
            == order_id
        ):

            return (
                order.display_order()
            )

    return "Order not found."


# ============================================================
# FUNCTION: DELETE ORDER
# ============================================================

def delete_order(order_id):

    for order in orders:

        if (
            order.order_id
            == order_id
        ):

            restaurant_statistics[
                "total_sales"
            ] -= order.calculate_total()

            restaurant_statistics[
                "total_orders"
            ] -= 1

            orders.remove(order)

            return (
                "Order deleted successfully."
            )

    return "Order not found."


# ============================================================
# FUNCTION: SHOW STATISTICS
# ============================================================

def show_statistics():

    return (
        f"Restaurant: {restaurant_name}\n"
        f"Total Orders: "
        f"{restaurant_statistics['total_orders']}\n"
        f"Total Sales: ₹"
        f"{restaurant_statistics['total_sales']:.2f}\n"
        f"Unique Customers: "
        f"{len(unique_customers)}"
    )


# ============================================================
# TKINTER FUNCTIONS
# ============================================================

def add_order_gui():

    order_id = order_id_entry.get()

    customer_name = customer_entry.get()

    food_name = food_entry.get()

    quantity = quantity_entry.get()

    price = price_entry.get()

    success, message = add_order(
        order_id,
        customer_name,
        food_name,
        quantity,
        price
    )

    if success:

        messagebox.showinfo(
            "Success",
            message
        )

        clear_fields()

    else:

        messagebox.showerror(
            "Error",
            message
        )


def view_orders_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    result = view_all_orders()

    output_text.insert(
        tk.END,
        result
    )


def search_order_gui():

    order_id = search_entry.get()

    result = search_order(
        order_id
    )

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        result
    )


def delete_order_gui():

    order_id = search_entry.get()

    result = delete_order(
        order_id
    )

    messagebox.showinfo(
        "Delete Order",
        result
    )

    view_orders_gui()


def statistics_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    result = show_statistics()

    output_text.insert(
        tk.END,
        result
    )


def clear_fields():

    order_id_entry.delete(
        0,
        tk.END
    )

    customer_entry.delete(
        0,
        tk.END
    )

    food_entry.delete(
        0,
        tk.END
    )

    quantity_entry.delete(
        0,
        tk.END
    )

    price_entry.delete(
        0,
        tk.END
    )


# ============================================================
# TKINTER WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "Online Food Order Management System"
)

root.geometry(
    "900x800"
)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="ONLINE FOOD ORDER MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold")
)

title_label.pack(
    pady=15
)


# ============================================================
# FORM FRAME
# ============================================================

form_frame = tk.Frame(root)

form_frame.pack(
    pady=10
)


# Order ID

tk.Label(
    form_frame,
    text="Order ID"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=5
)


order_id_entry = tk.Entry(
    form_frame,
    width=35
)

order_id_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)


# Customer Name

tk.Label(
    form_frame,
    text="Customer Name"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


customer_entry = tk.Entry(
    form_frame,
    width=35
)

customer_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


# Food Name

tk.Label(
    form_frame,
    text="Food Name"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=5
)


food_entry = tk.Entry(
    form_frame,
    width=35
)

food_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)


# Quantity

tk.Label(
    form_frame,
    text="Quantity"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=5
)


quantity_entry = tk.Entry(
    form_frame,
    width=35
)

quantity_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=5
)


# Price

tk.Label(
    form_frame,
    text="Price"
).grid(
    row=4,
    column=0,
    padx=10,
    pady=5
)


price_entry = tk.Entry(
    form_frame,
    width=35
)

price_entry.grid(
    row=4,
    column=1,
    padx=10,
    pady=5
)


# ============================================================
# BUTTONS
# ============================================================

add_button = tk.Button(
    root,
    text="Add Order",
    width=25,
    command=add_order_gui
)

add_button.pack(
    pady=5
)


view_button = tk.Button(
    root,
    text="View All Orders",
    width=25,
    command=view_orders_gui
)

view_button.pack(
    pady=5
)


statistics_button = tk.Button(
    root,
    text="Restaurant Statistics",
    width=25,
    command=statistics_gui
)

statistics_button.pack(
    pady=5
)


# ============================================================
# SEARCH AND DELETE
# ============================================================

search_frame = tk.Frame(root)

search_frame.pack(
    pady=15
)


tk.Label(
    search_frame,
    text="Order ID"
).grid(
    row=0,
    column=0,
    padx=5
)


search_entry = tk.Entry(
    search_frame,
    width=20
)

search_entry.grid(
    row=0,
    column=1,
    padx=5
)


search_button = tk.Button(
    search_frame,
    text="Search",
    command=search_order_gui
)

search_button.grid(
    row=0,
    column=2,
    padx=5
)


delete_button = tk.Button(
    search_frame,
    text="Delete",
    command=delete_order_gui
)

delete_button.grid(
    row=0,
    column=3,
    padx=5
)


# ============================================================
# OUTPUT AREA
# ============================================================

output_text = tk.Text(
    root,
    width=100,
    height=22
)

output_text.pack(
    pady=15
)


# ============================================================
# PROGRAM START
# ============================================================

root.mainloop()