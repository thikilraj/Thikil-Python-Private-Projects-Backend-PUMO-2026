import tkinter as tk
from tkinter import messagebox


# ============================================================
# 1. PYTHON IDENTIFIERS AND VARIABLES
# ============================================================

company_name = "ABC IT Solutions"
application_name = "IT Company Food Menu System"
currency = "₹"


# ============================================================
# 2. TUPLE
# ============================================================

FOOD_TYPES = (
    "Veg",
    "Non-Veg"
)

MEAL_TYPES = (
    "Breakfast",
    "Lunch",
    "Dinner",
    "Snacks"
)


# ============================================================
# 3. LIST
# ============================================================

food_menu = []

orders = []


# ============================================================
# 4. SET
# ============================================================

food_categories = set()


# ============================================================
# 5. DICTIONARY
# ============================================================

food_statistics = {
    "total_items": 0,
    "veg_items": 0,
    "non_veg_items": 0,
    "total_orders": 0,
    "total_revenue": 0.0
}


# ============================================================
# 6. OOP - FOOD ITEM CLASS
# ============================================================

class FoodItem:
    """
    FoodItem class manages company food menu details.
    """

    company_name = "ABC IT Solutions"

    def __init__(
        self,
        food_id,
        food_name,
        food_type,
        meal_type,
        price,
        category
    ):

        self.food_id = food_id
        self.food_name = food_name
        self.food_type = food_type
        self.meal_type = meal_type
        self.price = price
        self.category = category

    def display_food(self):

        return (
            f"Food ID: {self.food_id}\n"
            f"Food Name: {self.food_name}\n"
            f"Food Type: {self.food_type}\n"
            f"Meal Type: {self.meal_type}\n"
            f"Category: {self.category}\n"
            f"Price: ₹{self.price:.2f}\n"
        )

    def __str__(self):

        return (
            f"{self.food_id} - "
            f"{self.food_name}"
        )


# ============================================================
# 7. OOP - ORDER CLASS
# ============================================================

class FoodOrder:
    """
    FoodOrder class manages employee food orders.
    """

    def __init__(
        self,
        order_id,
        employee_name,
        food_item,
        quantity
    ):

        self.order_id = order_id
        self.employee_name = employee_name
        self.food_item = food_item
        self.quantity = quantity

    def calculate_total(self):

        return (
            self.food_item.price
            * self.quantity
        )

    def display_order(self):

        return (
            f"Order ID: {self.order_id}\n"
            f"Employee: {self.employee_name}\n"
            f"Food: {self.food_item.food_name}\n"
            f"Food Type: {self.food_item.food_type}\n"
            f"Quantity: {self.quantity}\n"
            f"Total: ₹"
            f"{self.calculate_total():.2f}\n"
        )


# ============================================================
# 8. BUILT-IN CLASS ATTRIBUTES
# ============================================================

print(
    "Class Name:",
    FoodItem.__name__
)

print(
    "Class Module:",
    FoodItem.__module__
)

print(
    "Class Documentation:",
    FoodItem.__doc__
)


# ============================================================
# 9. ADD FOOD ITEM FUNCTION
# ============================================================

def add_food_item(
    food_id,
    food_name,
    food_type,
    meal_type,
    price,
    category
):

    try:

        if food_id == "":

            raise ValueError(
                "Food ID cannot be empty."
            )

        if food_name == "":

            raise ValueError(
                "Food name cannot be empty."
            )

        if food_type not in FOOD_TYPES:

            raise ValueError(
                "Food type must be Veg or Non-Veg."
            )

        if meal_type not in MEAL_TYPES:

            raise ValueError(
                "Invalid meal type."
            )

        if category == "":

            raise ValueError(
                "Category cannot be empty."
            )

        price = float(price)

        if price <= 0:

            raise ValueError(
                "Price must be greater than zero."
            )

        # Check duplicate Food ID

        for food in food_menu:

            if (
                food.food_id
                == food_id
            ):

                raise ValueError(
                    "Food ID already exists."
                )

        # Create FoodItem object

        food = FoodItem(
            food_id,
            food_name,
            food_type,
            meal_type,
            price,
            category
        )

        # Add to LIST

        food_menu.append(food)

        # Add category to SET

        food_categories.add(category)

        # Update DICTIONARY

        food_statistics[
            "total_items"
        ] += 1

        if food_type == "Veg":

            food_statistics[
                "veg_items"
            ] += 1

        else:

            food_statistics[
                "non_veg_items"
            ] += 1

        return True, (
            "Food item added successfully."
        )

    except ValueError as error:

        return False, str(error)


# ============================================================
# 10. VIEW FOOD MENU
# ============================================================

def view_menu():

    if len(food_menu) == 0:

        return "Food menu is empty."

    output = ""

    for index in range(
        len(food_menu)
    ):

        output += (
            f"\nFood Item "
            f"{index + 1}\n"
        )

        output += "=" * 45

        output += "\n"

        output += (
            food_menu[index]
            .display_food()
        )

    return output


# ============================================================
# 11. SEARCH FOOD ITEM
# ============================================================

def search_food(
    food_id
):

    for food in food_menu:

        if (
            food.food_id
            == food_id
        ):

            return (
                food
                .display_food()
            )

    return "Food item not found."


# ============================================================
# 12. SEARCH BY FOOD TYPE
# ============================================================

def search_by_food_type(
    food_type
):

    output = ""

    found = False

    for food in food_menu:

        if (
            food.food_type.lower()
            == food_type.lower()
        ):

            output += (
                food
                .display_food()
            )

            output += "\n"

            found = True

    if found:

        return output

    return (
        "No food items found."
    )


# ============================================================
# 13. DELETE FOOD ITEM
# ============================================================

def delete_food(
    food_id
):

    for food in food_menu:

        if (
            food.food_id
            == food_id
        ):

            food_menu.remove(food)

            food_statistics[
                "total_items"
            ] -= 1

            if food.food_type == "Veg":

                food_statistics[
                    "veg_items"
                ] -= 1

            else:

                food_statistics[
                    "non_veg_items"
                ] -= 1

            return (
                "Food item deleted successfully."
            )

    return "Food item not found."


# ============================================================
# 14. PLACE FOOD ORDER
# ============================================================

def place_order(
    order_id,
    employee_name,
    food_id,
    quantity
):

    try:

        if order_id == "":

            raise ValueError(
                "Order ID cannot be empty."
            )

        if employee_name == "":

            raise ValueError(
                "Employee name cannot be empty."
            )

        quantity = int(quantity)

        if quantity <= 0:

            raise ValueError(
                "Quantity must be greater than zero."
            )

        selected_food = None

        for food in food_menu:

            if (
                food.food_id
                == food_id
            ):

                selected_food = food

                break

        if selected_food is None:

            raise ValueError(
                "Food item not found."
            )

        order = FoodOrder(
            order_id,
            employee_name,
            selected_food,
            quantity
        )

        orders.append(order)

        food_statistics[
            "total_orders"
        ] += 1

        food_statistics[
            "total_revenue"
        ] += (
            order.calculate_total()
        )

        return True, (
            "Order placed successfully."
        )

    except ValueError as error:

        return False, str(error)


# ============================================================
# 15. VIEW ORDERS
# ============================================================

def view_orders():

    if len(orders) == 0:

        return "No orders found."

    output = ""

    for index in range(
        len(orders)
    ):

        output += (
            f"\nOrder "
            f"{index + 1}\n"
        )

        output += "=" * 45

        output += "\n"

        output += (
            orders[index]
            .display_order()
        )

    return output


# ============================================================
# 16. FOOD STATISTICS
# ============================================================

def show_statistics():

    return (
        f"Company: "
        f"{company_name}\n"
        f"Total Food Items: "
        f"{food_statistics['total_items']}\n"
        f"Vegetarian Items: "
        f"{food_statistics['veg_items']}\n"
        f"Non-Vegetarian Items: "
        f"{food_statistics['non_veg_items']}\n"
        f"Total Orders: "
        f"{food_statistics['total_orders']}\n"
        f"Total Revenue: ₹"
        f"{food_statistics['total_revenue']:.2f}\n"
        f"Categories: "
        f"{len(food_categories)}"
    )


# ============================================================
# 17. TKINTER FUNCTIONS
# ============================================================

def add_food_gui():

    food_id = food_id_entry.get()

    food_name = food_name_entry.get()

    food_type = food_type_entry.get()

    meal_type = meal_type_entry.get()

    price = price_entry.get()

    category = category_entry.get()

    success, message = add_food_item(
        food_id,
        food_name,
        food_type,
        meal_type,
        price,
        category
    )

    if success:

        messagebox.showinfo(
            "Success",
            message
        )

        clear_food_fields()

    else:

        messagebox.showerror(
            "Error",
            message
        )


def view_menu_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        view_menu()
    )


def search_food_gui():

    food_id = search_food_entry.get()

    result = search_food(
        food_id
    )

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        result
    )


def search_type_gui():

    food_type = search_type_entry.get()

    result = search_by_food_type(
        food_type
    )

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        result
    )


def delete_food_gui():

    food_id = search_food_entry.get()

    result = delete_food(
        food_id
    )

    messagebox.showinfo(
        "Delete Food",
        result
    )

    view_menu_gui()


def place_order_gui():

    order_id = order_id_entry.get()

    employee_name = (
        employee_name_entry.get()
    )

    food_id = order_food_id_entry.get()

    quantity = quantity_entry.get()

    success, message = place_order(
        order_id,
        employee_name,
        food_id,
        quantity
    )

    if success:

        messagebox.showinfo(
            "Success",
            message
        )

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

    output_text.insert(
        tk.END,
        view_orders()
    )


def statistics_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        show_statistics()
    )


def clear_food_fields():

    food_id_entry.delete(
        0,
        tk.END
    )

    food_name_entry.delete(
        0,
        tk.END
    )

    food_type_entry.delete(
        0,
        tk.END
    )

    meal_type_entry.delete(
        0,
        tk.END
    )

    price_entry.delete(
        0,
        tk.END
    )

    category_entry.delete(
        0,
        tk.END
    )


# ============================================================
# 18. TKINTER WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "IT Company Food Menu Management System"
)

root.geometry(
    "1100x1000"
)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="IT COMPANY FOOD MENU SYSTEM",
    font=("Arial", 20, "bold")
)

title_label.pack(
    pady=15
)


# ============================================================
# ADD FOOD FRAME
# ============================================================

food_frame = tk.LabelFrame(
    root,
    text="Add Food Item",
    padx=10,
    pady=10
)

food_frame.pack(
    pady=10
)


# Food ID

tk.Label(
    food_frame,
    text="Food ID"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=5
)


food_id_entry = tk.Entry(
    food_frame,
    width=35
)

food_id_entry.grid(
    row=0,
    column=1
)


# Food Name

tk.Label(
    food_frame,
    text="Food Name"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


food_name_entry = tk.Entry(
    food_frame,
    width=35
)

food_name_entry.grid(
    row=1,
    column=1
)


# Food Type

tk.Label(
    food_frame,
    text="Food Type Veg/Non-Veg"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=5
)


food_type_entry = tk.Entry(
    food_frame,
    width=35
)

food_type_entry.grid(
    row=2,
    column=1
)


# Meal Type

tk.Label(
    food_frame,
    text="Meal Type"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=5
)


meal_type_entry = tk.Entry(
    food_frame,
    width=35
)

meal_type_entry.grid(
    row=3,
    column=1
)


# Price

tk.Label(
    food_frame,
    text="Price"
).grid(
    row=4,
    column=0,
    padx=10,
    pady=5
)


price_entry = tk.Entry(
    food_frame,
    width=35
)

price_entry.grid(
    row=4,
    column=1
)


# Category

tk.Label(
    food_frame,
    text="Category"
).grid(
    row=5,
    column=0,
    padx=10,
    pady=5
)


category_entry = tk.Entry(
    food_frame,
    width=35
)

category_entry.grid(
    row=5,
    column=1
)


# Add Button

tk.Button(
    food_frame,
    text="Add Food Item",
    command=add_food_gui,
    width=25
).grid(
    row=6,
    column=0,
    columnspan=2,
    pady=10
)


# ============================================================
# SEARCH FOOD FRAME
# ============================================================

search_frame = tk.LabelFrame(
    root,
    text="Search or Delete Food",
    padx=10,
    pady=10
)

search_frame.pack(
    pady=10
)


search_food_entry = tk.Entry(
    search_frame,
    width=20
)

search_food_entry.grid(
    row=0,
    column=0,
    padx=5
)


tk.Button(
    search_frame,
    text="Search",
    command=search_food_gui
).grid(
    row=0,
    column=1,
    padx=5
)


tk.Button(
    search_frame,
    text="Delete",
    command=delete_food_gui
).grid(
    row=0,
    column=2,
    padx=5
)


# ============================================================
# SEARCH BY FOOD TYPE
# ============================================================

type_frame = tk.LabelFrame(
    root,
    text="Search Veg or Non-Veg Food",
    padx=10,
    pady=10
)

type_frame.pack(
    pady=10
)


search_type_entry = tk.Entry(
    type_frame,
    width=20
)

search_type_entry.grid(
    row=0,
    column=0,
    padx=5
)


tk.Button(
    type_frame,
    text="Search Type",
    command=search_type_gui
).grid(
    row=0,
    column=1,
    padx=5
)


# ============================================================
# ORDER FRAME
# ============================================================

order_frame = tk.LabelFrame(
    root,
    text="Place Food Order",
    padx=10,
    pady=10
)

order_frame.pack(
    pady=10
)


tk.Label(
    order_frame,
    text="Order ID"
).grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)


order_id_entry = tk.Entry(
    order_frame,
    width=20
)

order_id_entry.grid(
    row=0,
    column=1
)


tk.Label(
    order_frame,
    text="Employee Name"
).grid(
    row=1,
    column=0,
    padx=5,
    pady=5
)


employee_name_entry = tk.Entry(
    order_frame,
    width=20
)

employee_name_entry.grid(
    row=1,
    column=1
)


tk.Label(
    order_frame,
    text="Food ID"
).grid(
    row=2,
    column=0,
    padx=5,
    pady=5
)


order_food_id_entry = tk.Entry(
    order_frame,
    width=20
)

order_food_id_entry.grid(
    row=2,
    column=1
)


tk.Label(
    order_frame,
    text="Quantity"
).grid(
    row=3,
    column=0,
    padx=5,
    pady=5
)


quantity_entry = tk.Entry(
    order_frame,
    width=20
)

quantity_entry.grid(
    row=3,
    column=1
)


tk.Button(
    order_frame,
    text="Place Order",
    command=place_order_gui,
    width=20
).grid(
    row=4,
    column=0,
    columnspan=2,
    pady=10
)


# ============================================================
# GENERAL BUTTONS
# ============================================================

tk.Button(
    root,
    text="View Complete Menu",
    command=view_menu_gui,
    width=30
).pack(
    pady=5
)


tk.Button(
    root,
    text="View All Orders",
    command=view_orders_gui,
    width=30
).pack(
    pady=5
)


tk.Button(
    root,
    text="Show Food Statistics",
    command=statistics_gui,
    width=30
).pack(
    pady=5
)


# ============================================================
# OUTPUT AREA
# ============================================================

output_text = tk.Text(
    root,
    width=120,
    height=20
)

output_text.pack(
    pady=15
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()