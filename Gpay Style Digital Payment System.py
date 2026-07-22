import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


# =====================================================
# FILE NAMES
# =====================================================

USER_FILE = "users.json"
TRANSACTION_FILE = "transactions.json"


# =====================================================
# USER CLASS
# =====================================================

class User:

    # Class attribute
    app_name = "Python Pay"

    def __init__(
        self,
        user_id,
        name,
        mobile,
        upi_id,
        balance=0.0
    ):

        self.user_id = user_id
        self.name = name
        self.mobile = mobile
        self.upi_id = upi_id
        self.balance = balance

    # Built-in class attribute usage
    def __str__(self):

        return (
            f"{self.user_id} - "
            f"{self.name} - "
            f"{self.upi_id}"
        )

    def to_dictionary(self):

        return {
            "user_id": self.user_id,
            "name": self.name,
            "mobile": self.mobile,
            "upi_id": self.upi_id,
            "balance": self.balance
        }


# =====================================================
# PAYMENT MANAGER CLASS
# =====================================================

class PaymentManager:

    def __init__(self):

        # List
        self.users = []

        # List of dictionaries
        self.transactions = []

    # =================================================
    # CREATE USER
    # =================================================

    def create_user(self, user):

        for existing_user in self.users:

            if (
                existing_user.user_id
                == user.user_id
            ):

                raise ValueError(
                    "User ID already exists."
                )

            if (
                existing_user.upi_id
                == user.upi_id
            ):

                raise ValueError(
                    "UPI ID already exists."
                )

        self.users.append(user)

    # =================================================
    # FIND USER
    # =================================================

    def find_user(self, upi_id):

        for user in self.users:

            if user.upi_id == upi_id:

                return user

        raise ValueError(
            "UPI ID not found."
        )

    # =================================================
    # ADD MONEY
    # =================================================

    def add_money(self, upi_id, amount):

        if amount <= 0:

            raise ValueError(
                "Amount must be greater than zero."
            )

        user = self.find_user(upi_id)

        user.balance += amount

        transaction = {

            "type": "ADD MONEY",

            "receiver": upi_id,

            "amount": amount,

            "status": "SUCCESS",

            "balance_after": user.balance

        }

        self.transactions.append(transaction)

    # =================================================
    # SEND MONEY
    # =================================================

    def send_money(
        self,
        sender_upi,
        receiver_upi,
        amount
    ):

        if amount <= 0:

            raise ValueError(
                "Amount must be greater than zero."
            )

        if sender_upi == receiver_upi:

            raise ValueError(
                "Sender and receiver cannot be the same."
            )

        sender = self.find_user(
            sender_upi
        )

        receiver = self.find_user(
            receiver_upi
        )

        if amount > sender.balance:

            raise ValueError(
                "Insufficient balance."
            )

        sender.balance -= amount

        receiver.balance += amount

        transaction = {

            "type": "SEND MONEY",

            "sender": sender_upi,

            "receiver": receiver_upi,

            "amount": amount,

            "status": "SUCCESS",

            "sender_balance": sender.balance

        }

        self.transactions.append(

            transaction

        )

    # =================================================
    # SEARCH USERS
    # =================================================

    def search_users(self, keyword):

        result = []

        for user in self.users:

            if (

                keyword.lower()
                in user.name.lower()

                or

                keyword.lower()
                in user.upi_id.lower()

            ):

                result.append(user)

        return result

    # =================================================
    # GET UNIQUE UPI DOMAINS
    # =================================================

    def get_upi_domains(self):

        domains = set()

        for user in self.users:

            if "@" in user.upi_id:

                domain = (

                    user.upi_id.split("@")[1]

                )

                domains.add(domain)

        return domains

    # =================================================
    # SAVE DATA
    # =================================================

    def save_data(self):

        users_data = []

        for user in self.users:

            users_data.append(

                user.to_dictionary()

            )

        with open(

            USER_FILE,

            "w"

        ) as file:

            json.dump(

                users_data,

                file,

                indent=4

            )

        with open(

            TRANSACTION_FILE,

            "w"

        ) as file:

            json.dump(

                self.transactions,

                file,

                indent=4

            )

    # =================================================
    # LOAD DATA
    # =================================================

    def load_data(self):

        if os.path.exists(USER_FILE):

            try:

                with open(

                    USER_FILE,

                    "r"

                ) as file:

                    data = json.load(file)

                    for item in data:

                        user = User(

                            item["user_id"],

                            item["name"],

                            item["mobile"],

                            item["upi_id"],

                            item["balance"]

                        )

                        self.users.append(user)

            except json.JSONDecodeError:

                messagebox.showerror(

                    "Error",

                    "Invalid users.json file."

                )

        if os.path.exists(

            TRANSACTION_FILE

        ):

            try:

                with open(

                    TRANSACTION_FILE,

                    "r"

                ) as file:

                    self.transactions = (

                        json.load(file)

                    )

            except json.JSONDecodeError:

                messagebox.showerror(

                    "Error",

                    "Invalid transactions.json file."

                )


# =====================================================
# TKINTER APPLICATION
# =====================================================

class PaymentApp:

    def __init__(self, root):

        self.root = root

        self.root.title(

            "Python Pay - Digital Payment System"

        )

        self.root.geometry(

            "1400x850"

        )

        self.manager = PaymentManager()

        self.manager.load_data()

        # =================================================
        # TITLE
        # =================================================

        title = tk.Label(

            root,

            text=(

                "Python Pay - Digital Payment System"

            ),

            font=(

                "Arial",

                24,

                "bold"

            )

        )

        title.pack(pady=10)

        # =================================================
        # FORM
        # =================================================

        form_frame = tk.Frame(root)

        form_frame.pack(pady=10)

        # User ID

        tk.Label(

            form_frame,

            text="User ID"

        ).grid(

            row=0,

            column=0,

            padx=5,

            pady=5

        )

        self.user_id_entry = tk.Entry(

            form_frame

        )

        self.user_id_entry.grid(

            row=0,

            column=1

        )

        # Name

        tk.Label(

            form_frame,

            text="Name"

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

        # Mobile

        tk.Label(

            form_frame,

            text="Mobile Number"

        ).grid(

            row=1,

            column=0,

            padx=5

        )

        self.mobile_entry = tk.Entry(

            form_frame

        )

        self.mobile_entry.grid(

            row=1,

            column=1

        )

        # UPI ID

        tk.Label(

            form_frame,

            text="UPI ID"

        ).grid(

            row=1,

            column=2,

            padx=5

        )

        self.upi_entry = tk.Entry(

            form_frame

        )

        self.upi_entry.grid(

            row=1,

            column=3

        )

        # Amount

        tk.Label(

            form_frame,

            text="Amount"

        ).grid(

            row=2,

            column=0,

            padx=5

        )

        self.amount_entry = tk.Entry(

            form_frame

        )

        self.amount_entry.grid(

            row=2,

            column=1

        )

        # Receiver UPI

        tk.Label(

            form_frame,

            text="Receiver UPI ID"

        ).grid(

            row=2,

            column=2,

            padx=5

        )

        self.receiver_entry = tk.Entry(

            form_frame

        )

        self.receiver_entry.grid(

            row=2,

            column=3

        )

        # Search

        tk.Label(

            form_frame,

            text="Search"

        ).grid(

            row=3,

            column=0,

            padx=5

        )

        self.search_entry = tk.Entry(

            form_frame

        )

        self.search_entry.grid(

            row=3,

            column=1

        )

        # =================================================
        # BUTTONS
        # =================================================

        button_frame = tk.Frame(root)

        button_frame.pack(pady=10)

        tk.Button(

            button_frame,

            text="Create User",

            command=self.create_user

        ).grid(

            row=0,

            column=0,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Add Money",

            command=self.add_money

        ).grid(

            row=0,

            column=1,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Send Money",

            command=self.send_money

        ).grid(

            row=0,

            column=2,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Search User",

            command=self.search_users

        ).grid(

            row=0,

            column=3,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Show All Users",

            command=self.show_all

        ).grid(

            row=0,

            column=4,

            padx=5

        )

        tk.Button(

            button_frame,

            text="UPI Domains",

            command=self.show_domains

        ).grid(

            row=0,

            column=5,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Transactions",

            command=self.show_transactions

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
        # TABLE
        # =================================================

        columns = (

            "User ID",

            "Name",

            "Mobile",

            "UPI ID",

            "Balance"

        )

        self.table = ttk.Treeview(

            root,

            columns=columns,

            show="headings"

        )

        for column in columns:

            self.table.heading(

                column,

                text=column

            )

            self.table.column(

                column,

                width=250

            )

        self.table.pack(

            fill=tk.BOTH,

            expand=True,

            padx=10,

            pady=10

        )

        self.status_label = tk.Label(

            root,

            text="Ready"

        )

        self.status_label.pack(

            pady=5

        )

        self.show_all()

    # =================================================
    # CREATE USER
    # =================================================

    def create_user(self):

        try:

            user_id = int(

                self.user_id_entry.get()

            )

            name = (

                self.name_entry.get()

            )

            mobile = (

                self.mobile_entry.get()

            )

            upi_id = (

                self.upi_entry.get()

            )

            if name == "":

                raise ValueError(

                    "Name is required."

                )

            if mobile == "":

                raise ValueError(

                    "Mobile number is required."

                )

            if "@" not in upi_id:

                raise ValueError(

                    "Enter a valid UPI ID."

                )

            user = User(

                user_id,

                name,

                mobile,

                upi_id

            )

            self.manager.create_user(

                user

            )

            self.manager.save_data()

            self.show_all()

            self.clear_fields()

            messagebox.showinfo(

                "Success",

                "User created successfully."

            )

        except ValueError as error:

            messagebox.showerror(

                "Input Error",

                str(error)

            )

    # =================================================
    # ADD MONEY
    # =================================================

    def add_money(self):

        try:

            upi_id = (

                self.upi_entry.get()

            )

            amount = float(

                self.amount_entry.get()

            )

            self.manager.add_money(

                upi_id,

                amount

            )

            self.manager.save_data()

            self.show_all()

            messagebox.showinfo(

                "Success",

                (

                    f"₹{amount} added successfully."

                )

            )

        except ValueError as error:

            messagebox.showerror(

                "Add Money Error",

                str(error)

            )

    # =================================================
    # SEND MONEY
    # =================================================

    def send_money(self):

        try:

            sender_upi = (

                self.upi_entry.get()

            )

            receiver_upi = (

                self.receiver_entry.get()

            )

            amount = float(

                self.amount_entry.get()

            )

            self.manager.send_money(

                sender_upi,

                receiver_upi,

                amount

            )

            self.manager.save_data()

            self.show_all()

            messagebox.showinfo(

                "Payment Successful",

                (

                    f"₹{amount} sent successfully."

                )

            )

        except ValueError as error:

            messagebox.showerror(

                "Payment Error",

                str(error)

            )

    # =================================================
    # SEARCH USERS
    # =================================================

    def search_users(self):

        keyword = (

            self.search_entry.get()

        )

        results = (

            self.manager.search_users(

                keyword

            )

        )

        self.clear_table()

        for user in results:

            self.table.insert(

                "",

                tk.END,

                values=(

                    user.user_id,

                    user.name,

                    user.mobile,

                    user.upi_id,

                    user.balance

                )

            )

        self.status_label.config(

            text=(

                f"{len(results)} user(s) found."

            )

        )

    # =================================================
    # SHOW ALL USERS
    # =================================================

    def show_all(self):

        self.clear_table()

        for user in self.manager.users:

            self.table.insert(

                "",

                tk.END,

                values=(

                    user.user_id,

                    user.name,

                    user.mobile,

                    user.upi_id,

                    user.balance

                )

            )

        self.status_label.config(

            text=(

                f"Total Users: "

                f"{len(self.manager.users)}"

            )

        )

    # =================================================
    # SHOW UPI DOMAINS
    # =================================================

    def show_domains(self):

        domains = (

            self.manager.get_upi_domains()

        )

        if domains:

            messagebox.showinfo(

                "UPI Domains",

                "\n".join(domains)

            )

        else:

            messagebox.showinfo(

                "UPI Domains",

                "No UPI domains found."

            )

    # =================================================
    # SHOW TRANSACTIONS
    # =================================================

    def show_transactions(self):

        if not self.manager.transactions:

            messagebox.showinfo(

                "Transactions",

                "No transactions found."

            )

            return

        transaction_text = ""

        for transaction in (

            self.manager.transactions

        ):

            transaction_text += (

                str(transaction)

                + "\n"

            )

        messagebox.showinfo(

            "Transactions",

            transaction_text

        )

    # =================================================
    # CLEAR TABLE
    # =================================================

    def clear_table(self):

        for item in (

            self.table.get_children()

        ):

            self.table.delete(

                item

            )

    # =================================================
    # CLEAR FIELDS
    # =================================================

    def clear_fields(self):

        entries = (

            self.user_id_entry,

            self.name_entry,

            self.mobile_entry,

            self.upi_entry,

            self.amount_entry,

            self.receiver_entry,

            self.search_entry

        )

        for entry in entries:

            entry.delete(

                0,

                tk.END

            )


# =====================================================
# MAIN FUNCTION
# =====================================================

def main():

    root = tk.Tk()

    app = PaymentApp(

        root

    )

    root.mainloop()


# =====================================================
# PROGRAM START
# =====================================================

if __name__ == "__main__":

    main()