import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


# =====================================================
# CONSTANTS
# =====================================================

PRODUCT_FILE = "products.json"
ORDER_FILE = "orders.json"


# =====================================================
# PRODUCT CLASS
# Demonstrates OOP
# =====================================================

class Product:

    # Class attribute
    store_name = "Python Online Store"

    def __init__(
        self,
        product_id,
        name,
        category,
        price,
        quantity
    ):

        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    # Built-in class attribute method
    def __str__(self):

        return (
            f"{self.product_id} - "
            f"{self.name} - "
            f"₹{self.price}"
        )

    # Convert object to dictionary
    def to_dictionary(self):

        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity
        }


# =====================================================
# CART CLASS
# =====================================================

class ShoppingCart:

    def __init__(self):

        # Dictionary
        self.cart = {}

    # Add product to cart
    def add_to_cart(self, product):

        if product.product_id in self.cart:

            self.cart[
                product.product_id
            ]["quantity"] += 1

        else:

            self.cart[
                product.product_id
            ] = {
                "product": product,
                "quantity": 1
            }

    # Remove product from cart
    def remove_from_cart(self, product_id):

        if product_id in self.cart:

            del self.cart[
                product_id
            ]

            return True

        return False

    # Calculate total
    def calculate_total(self):

        total = 0

        for item in self.cart.values():

            product = item["product"]

            quantity = item["quantity"]

            total += (
                product.price
                * quantity
            )

        return total

    # Get cart items
    def get_items(self):

        return self.cart.values()

    # Clear cart
    def clear_cart(self):

        self.cart.clear()


# =====================================================
# STORE MANAGER CLASS
# =====================================================

class StoreManager:

    def __init__(self):

        # List
        self.products = []

    # -------------------------------------------------
    # ADD PRODUCT
    # -------------------------------------------------

    def add_product(self, product):

        for existing_product in self.products:

            if (
                existing_product.product_id
                == product.product_id
            ):

                raise ValueError(
                    "Product ID already exists."
                )

        self.products.append(product)

    # -------------------------------------------------
    # GET PRODUCTS
    # -------------------------------------------------

    def get_products(self):

        return self.products

    # -------------------------------------------------
    # SEARCH PRODUCTS
    # -------------------------------------------------

    def search_products(self, keyword):

        result = []

        for product in self.products:

            if (
                keyword.lower()
                in product.name.lower()
                or keyword.lower()
                in product.category.lower()
            ):

                result.append(product)

        return result

    # -------------------------------------------------
    # GET UNIQUE CATEGORIES
    # Demonstrates SET
    # -------------------------------------------------

    def get_unique_categories(self):

        categories = set()

        for product in self.products:

            categories.add(
                product.category
            )

        return categories

    # -------------------------------------------------
    # SAVE PRODUCTS
    # Demonstrates OUTPUT
    # -------------------------------------------------

    def save_products(self):

        data = []

        for product in self.products:

            data.append(
                product.to_dictionary()
            )

        with open(
            PRODUCT_FILE,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    # -------------------------------------------------
    # LOAD PRODUCTS
    # Demonstrates INPUT
    # -------------------------------------------------

    def load_products(self):

        if not os.path.exists(
            PRODUCT_FILE
        ):

            return

        try:

            with open(
                PRODUCT_FILE,
                "r"
            ) as file:

                data = json.load(file)

                for item in data:

                    product = Product(
                        item["product_id"],
                        item["name"],
                        item["category"],
                        item["price"],
                        item["quantity"]
                    )

                    self.products.append(
                        product
                    )

        except json.JSONDecodeError:

            messagebox.showerror(
                "Error",
                "Invalid products file."
            )


# =====================================================
# TKINTER APPLICATION
# =====================================================

class ShoppingApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Python Online Shopping System"
        )

        self.root.geometry(
            "1200x750"
        )

        # Create objects
        self.manager = StoreManager()

        self.cart = ShoppingCart()

        self.manager.load_products()

        # =================================================
        # TITLE
        # =================================================

        title = tk.Label(
            root,
            text="Python Online Shopping System",
            font=(
                "Arial",
                22,
                "bold"
            )
        )

        title.pack(
            pady=10
        )

        # =================================================
        # PRODUCT INPUT FORM
        # =================================================

        form_frame = tk.Frame(
            root
        )

        form_frame.pack(
            pady=10
        )

        # Product ID
        tk.Label(
            form_frame,
            text="Product ID"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.id_entry = tk.Entry(
            form_frame
        )

        self.id_entry.grid(
            row=0,
            column=1
        )

        # Product Name
        tk.Label(
            form_frame,
            text="Product Name"
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        self.name_entry = tk.Entry(
            form_frame
        )

        self.name_entry.grid(
            row=0,
            column=3
        )

        # Category
        tk.Label(
            form_frame,
            text="Category"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.category_entry = tk.Entry(
            form_frame
        )

        self.category_entry.grid(
            row=1,
            column=1
        )

        # Price
        tk.Label(
            form_frame,
            text="Price"
        ).grid(
            row=1,
            column=2,
            padx=5
        )

        self.price_entry = tk.Entry(
            form_frame
        )

        self.price_entry.grid(
            row=1,
            column=3
        )

        # Quantity
        tk.Label(
            form_frame,
            text="Quantity"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5
        )

        self.quantity_entry = tk.Entry(
            form_frame
        )

        self.quantity_entry.grid(
            row=2,
            column=1
        )

        # Search
        tk.Label(
            form_frame,
            text="Search"
        ).grid(
            row=2,
            column=2,
            padx=5
        )

        self.search_entry = tk.Entry(
            form_frame
        )

        self.search_entry.grid(
            row=2,
            column=3
        )

        # =================================================
        # BUTTONS
        # =================================================

        button_frame = tk.Frame(
            root
        )

        button_frame.pack(
            pady=10
        )

        tk.Button(
            button_frame,
            text="Add Product",
            command=self.add_product
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Search",
            command=self.search_products
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Show All",
            command=self.show_all
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Add to Cart",
            command=self.add_to_cart
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Remove from Cart",
            command=self.remove_from_cart
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        tk.Button(
            button_frame,
            text="View Cart",
            command=self.view_cart
        ).grid(
            row=0,
            column=5,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Checkout",
            command=self.checkout
        ).grid(
            row=0,
            column=6,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_fields
        ).grid(
            row=0,
            column=7,
            padx=5
        )

        # =================================================
        # PRODUCT TABLE
        # =================================================

        product_columns = (
            "ID",
            "Name",
            "Category",
            "Price",
            "Stock"
        )

        self.product_table = ttk.Treeview(
            root,
            columns=product_columns,
            show="headings"
        )

        for column in product_columns:

            self.product_table.heading(
                column,
                text=column
            )

            self.product_table.column(
                column,
                width=180
            )

        self.product_table.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10
        )

        # =================================================
        # STATUS
        # =================================================

        self.status_label = tk.Label(
            root,
            text="Ready"
        )

        self.status_label.pack(
            pady=5
        )

        self.show_all()

    # =================================================
    # ADD PRODUCT
    # =================================================

    def add_product(self):

        try:

            product_id = int(
                self.id_entry.get()
            )

            name = (
                self.name_entry.get()
            )

            category = (
                self.category_entry.get()
            )

            price = float(
                self.price_entry.get()
            )

            quantity = int(
                self.quantity_entry.get()
            )

            if name == "":

                raise ValueError(
                    "Product name is required."
                )

            if category == "":

                raise ValueError(
                    "Category is required."
                )

            if price <= 0:

                raise ValueError(
                    "Price must be greater than zero."
                )

            if quantity < 0:

                raise ValueError(
                    "Quantity cannot be negative."
                )

            product = Product(
                product_id,
                name,
                category,
                price,
                quantity
            )

            self.manager.add_product(
                product
            )

            self.manager.save_products()

            self.show_all()

            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Product added successfully."
            )

        except ValueError as error:

            messagebox.showerror(
                "Input Error",
                str(error)
            )

    # =================================================
    # SEARCH PRODUCTS
    # =================================================

    def search_products(self):

        keyword = (
            self.search_entry.get()
        )

        results = (
            self.manager
            .search_products(
                keyword
            )
        )

        self.clear_table()

        for product in results:

            self.product_table.insert(
                "",
                tk.END,
                values=(
                    product.product_id,
                    product.name,
                    product.category,
                    product.price,
                    product.quantity
                )
            )

        self.status_label.config(
            text=f"{len(results)} product(s) found."
        )

    # =================================================
    # SHOW ALL PRODUCTS
    # =================================================

    def show_all(self):

        self.clear_table()

        products = (
            self.manager
            .get_products()
        )

        for product in products:

            self.product_table.insert(
                "",
                tk.END,
                values=(
                    product.product_id,
                    product.name,
                    product.category,
                    product.price,
                    product.quantity
                )
            )

        self.status_label.config(
            text=f"Total Products: {len(products)}"
        )

    # =================================================
    # ADD TO CART
    # =================================================

    def add_to_cart(self):

        try:

            product_id = int(
                self.id_entry.get()
            )

            for product in (
                self.manager
                .get_products()
            ):

                if (
                    product.product_id
                    == product_id
                ):

                    if product.quantity <= 0:

                        raise ValueError(
                            "Product is out of stock."
                        )

                    self.cart.add_to_cart(
                        product
                    )

                    product.quantity -= 1

                    self.manager.save_products()

                    self.show_all()

                    messagebox.showinfo(
                        "Success",
                        "Product added to cart."
                    )

                    return

            raise ValueError(
                "Product not found."
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # =================================================
    # REMOVE FROM CART
    # =================================================

    def remove_from_cart(self):

        try:

            product_id = int(
                self.id_entry.get()
            )

            success = (
                self.cart
                .remove_from_cart(
                    product_id
                )
            )

            if success:

                messagebox.showinfo(
                    "Success",
                    "Product removed from cart."
                )

            else:

                messagebox.showerror(
                    "Error",
                    "Product not found in cart."
                )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter a valid Product ID."
            )

    # =================================================
    # VIEW CART
    # =================================================

    def view_cart(self):

        if not self.cart.cart:

            messagebox.showinfo(
                "Cart",
                "Your cart is empty."
            )

            return

        cart_text = ""

        for item in (
            self.cart
            .get_items()
        ):

            product = item["product"]

            quantity = item["quantity"]

            cart_text += (
                f"{product.name} x {quantity} "
                f"= ₹"
                f"{product.price * quantity}\n"
            )

        cart_text += (
            "\nTotal: ₹"
            f"{self.cart.calculate_total()}"
        )

        messagebox.showinfo(
            "Shopping Cart",
            cart_text
        )

    # =================================================
    # CHECKOUT
    # =================================================

    def checkout(self):

        if not self.cart.cart:

            messagebox.showerror(
                "Error",
                "Cart is empty."
            )

            return

        total = (
            self.cart
            .calculate_total()
        )

        messagebox.showinfo(
            "Order Successful",
            f"Order placed successfully!\n"
            f"Total Amount: ₹{total}"
        )

        self.cart.clear_cart()

    # =================================================
    # CLEAR TABLE
    # =================================================

    def clear_table(self):

        for item in (
            self.product_table
            .get_children()
        ):

            self.product_table.delete(
                item
            )

    # =================================================
    # CLEAR FIELDS
    # =================================================

    def clear_fields(self):

        self.id_entry.delete(
            0,
            tk.END
        )

        self.name_entry.delete(
            0,
            tk.END
        )

        self.category_entry.delete(
            0,
            tk.END
        )

        self.price_entry.delete(
            0,
            tk.END
        )

        self.quantity_entry.delete(
            0,
            tk.END
        )

        self.search_entry.delete(
            0,
            tk.END
        )


# =====================================================
# MAIN FUNCTION
# =====================================================

def main():

    root = tk.Tk()

    app = ShoppingApp(
        root
    )

    root.mainloop()


# =====================================================
# PROGRAM ENTRY POINT
# =====================================================

if __name__ == "__main__":

    main()