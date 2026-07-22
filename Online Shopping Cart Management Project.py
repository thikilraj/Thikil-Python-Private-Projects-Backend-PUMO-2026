import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


# =====================================================
# CONSTANTS
# =====================================================

DATA_FILE = "products.json"


# =====================================================
# PRODUCT CLASS
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
            f"{self.category} - "
            f"₹{self.price} - "
            f"Stock: {self.quantity}"
        )

    def to_dictionary(self):

        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity
        }


# =====================================================
# SHOPPING CART CLASS
# =====================================================

class ShoppingCart:

    def __init__(self):

        # Dictionary
        self.cart = {}

    # Add product to cart
    def add_to_cart(self, product, quantity):

        if quantity <= 0:

            raise ValueError(
                "Quantity must be greater than zero."
            )

        if quantity > product.quantity:

            raise ValueError(
                "Not enough stock available."
            )

        if product.product_id in self.cart:

            self.cart[
                product.product_id
            ]["quantity"] += quantity

        else:

            self.cart[
                product.product_id
            ] = {

                "product": product,

                "quantity": quantity
            }

        product.quantity -= quantity

    # Remove product
    def remove_from_cart(self, product_id):

        if product_id not in self.cart:

            raise ValueError(
                "Product not found in cart."
            )

        item = self.cart[product_id]

        product = item["product"]

        quantity = item["quantity"]

        product.quantity += quantity

        del self.cart[product_id]

    # Calculate total
    def calculate_total(self):

        total = 0

        for item in self.cart.values():

            product = item["product"]

            quantity = item["quantity"]

            total += product.price * quantity

        return total

    # Get cart items
    def get_cart_items(self):

        return self.cart


# =====================================================
# PRODUCT MANAGER CLASS
# =====================================================

class ProductManager:

    def __init__(self):

        # List
        self.products = []

    # Add product
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

    # Get products
    def get_all_products(self):

        return self.products

    # Search products
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

    # Delete product
    def delete_product(self, product_id):

        for product in self.products:

            if product.product_id == product_id:

                self.products.remove(product)

                return True

        return False

    # Get unique categories
    def get_unique_categories(self):

        # Set
        categories = set()

        for product in self.products:

            categories.add(
                product.category
            )

        return categories

    # Save products
    def save_data(self):

        data = []

        for product in self.products:

            data.append(
                product.to_dictionary()
            )

        with open(
            DATA_FILE,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    # Load products
    def load_data(self):

        if not os.path.exists(DATA_FILE):

            return

        try:

            with open(
                DATA_FILE,
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
                "Invalid JSON file."
            )


# =====================================================
# TKINTER APPLICATION
# =====================================================

class ShoppingApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Online Shopping Cart"
        )

        self.root.geometry(
            "1100x700"
        )

        # Objects
        self.product_manager = ProductManager()

        self.cart = ShoppingCart()

        self.product_manager.load_data()

        # =================================================
        # TITLE
        # =================================================

        title = tk.Label(
            root,
            text="Online Shopping Cart System",
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
        # PRODUCT FORM
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
            padx=5
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
            padx=5
        )

        self.quantity_entry = tk.Entry(
            form_frame
        )

        self.quantity_entry.grid(
            row=2,
            column=1
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
            text="Delete Product",
            command=self.delete_product
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Search",
            command=self.search_product
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Show All",
            command=self.show_all_products
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Add To Cart",
            command=self.add_to_cart
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
            text="Clear",
            command=self.clear_fields
        ).grid(
            row=0,
            column=6,
            padx=5
        )

        # =================================================
        # PRODUCT TABLE
        # =================================================

        columns = (
            "ID",
            "Name",
            "Category",
            "Price",
            "Stock"
        )

        self.product_table = ttk.Treeview(
            root,
            columns=columns,
            show="headings"
        )

        for column in columns:

            self.product_table.heading(
                column,
                text=column
            )

            self.product_table.column(
                column,
                width=150
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

        self.show_all_products()

    # =================================================
    # GET USER INPUT
    # =================================================

    def get_product_input(self):

        try:

            product_id = int(
                self.id_entry.get()
            )

            name = self.name_entry.get()

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

            return (
                product_id,
                name,
                category,
                price,
                quantity
            )

        except ValueError as error:

            messagebox.showerror(
                "Input Error",
                str(error)
            )

            return None

    # =================================================
    # ADD PRODUCT
    # =================================================

    def add_product(self):

        data = self.get_product_input()

        if data is None:

            return

        (
            product_id,
            name,
            category,
            price,
            quantity
        ) = data

        try:

            product = Product(
                product_id,
                name,
                category,
                price,
                quantity
            )

            self.product_manager.add_product(
                product
            )

            self.product_manager.save_data()

            self.show_all_products()

            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Product added successfully."
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # =================================================
    # DELETE PRODUCT
    # =================================================

    def delete_product(self):

        try:

            product_id = int(
                self.id_entry.get()
            )

            success = (
                self.product_manager
                .delete_product(
                    product_id
                )
            )

            if success:

                self.product_manager.save_data()

                self.show_all_products()

                messagebox.showinfo(
                    "Success",
                    "Product deleted."
                )

            else:

                messagebox.showerror(
                    "Error",
                    "Product not found."
                )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter a valid Product ID."
            )

    # =================================================
    # SEARCH PRODUCT
    # =================================================

    def search_product(self):

        keyword = (
            self.name_entry.get()
        )

        results = (
            self.product_manager
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

    def show_all_products(self):

        self.clear_table()

        products = (
            self.product_manager
            .get_all_products()
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

            quantity = int(
                self.quantity_entry.get()
            )

            selected_product = None

            for product in (
                self.product_manager
                .get_all_products()
            ):

                if (
                    product.product_id
                    == product_id
                ):

                    selected_product = product

                    break

            if selected_product is None:

                raise ValueError(
                    "Product not found."
                )

            self.cart.add_to_cart(
                selected_product,
                quantity
            )

            self.product_manager.save_data()

            self.show_all_products()

            messagebox.showinfo(
                "Success",
                "Product added to cart."
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # =================================================
    # VIEW CART
    # =================================================

    def view_cart(self):

        cart_window = tk.Toplevel(
            self.root
        )

        cart_window.title(
            "Shopping Cart"
        )

        cart_window.geometry(
            "600x400"
        )

        cart_table = ttk.Treeview(
            cart_window,
            columns=(
                "Product",
                "Quantity",
                "Price",
                "Total"
            ),
            show="headings"
        )

        for column in (
            "Product",
            "Quantity",
            "Price",
            "Total"
        ):

            cart_table.heading(
                column,
                text=column
            )

        cart_table.pack(
            fill=tk.BOTH,
            expand=True
        )

        for item in (
            self.cart
            .get_cart_items()
            .values()
        ):

            product = item["product"]

            quantity = item["quantity"]

            total = (
                product.price
                * quantity
            )

            cart_table.insert(
                "",
                tk.END,
                values=(
                    product.name,
                    quantity,
                    product.price,
                    total
                )
            )

        total_price = (
            self.cart
            .calculate_total()
        )

        tk.Label(
            cart_window,
            text=f"Total Price: ₹{total_price:.2f}",
            font=(
                "Arial",
                16,
                "bold"
            )
        ).pack(
            pady=10
        )

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
    # CLEAR INPUT FIELDS
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