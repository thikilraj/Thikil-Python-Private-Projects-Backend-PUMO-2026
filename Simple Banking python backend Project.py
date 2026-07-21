import tkinter as tk
from tkinter import messagebox


# -------------------------------
# OOP: Bank Account Class
# -------------------------------

class BankAccount:

    # Class attribute
    bank_name = "Python Bank"

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

        # List
        self.transactions = []

        # Set
        self.transaction_types = set()

    # Function: Deposit money
    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        self.balance += amount

        self.transactions.append(("Deposit", amount))
        self.transaction_types.add("Deposit")

    # Function: Withdraw money
    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount

        self.transactions.append(("Withdrawal", amount))
        self.transaction_types.add("Withdrawal")

    # Function: Get account details
    def get_details(self):

        return {
            "name": self.name,
            "account_number": self.account_number,
            "balance": self.balance,
            "transactions": self.transactions
        }


# -------------------------------
# Dictionary: Store Accounts
# -------------------------------

accounts = {}


# -------------------------------
# Create Account Function
# -------------------------------

def create_account():

    try:

        name = name_entry.get()
        account_number = account_entry.get()

        if name == "" or account_number == "":
            raise ValueError("Please enter all details")

        if account_number in accounts:
            raise ValueError("Account already exists")

        accounts[account_number] = BankAccount(
            name,
            account_number
        )

        messagebox.showinfo(
            "Success",
            "Account created successfully!"
        )

        name_entry.delete(0, tk.END)
        account_entry.delete(0, tk.END)

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# -------------------------------
# Deposit Function
# -------------------------------

def deposit_money():

    try:

        account_number = account_entry.get()
        amount = float(amount_entry.get())

        if account_number not in accounts:
            raise ValueError("Account not found")

        accounts[account_number].deposit(amount)

        messagebox.showinfo(
            "Success",
            f"₹{amount} deposited successfully!"
        )

        amount_entry.delete(0, tk.END)

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# -------------------------------
# Withdraw Function
# -------------------------------

def withdraw_money():

    try:

        account_number = account_entry.get()
        amount = float(amount_entry.get())

        if account_number not in accounts:
            raise ValueError("Account not found")

        accounts[account_number].withdraw(amount)

        messagebox.showinfo(
            "Success",
            f"₹{amount} withdrawn successfully!"
        )

        amount_entry.delete(0, tk.END)

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# -------------------------------
# Check Balance Function
# -------------------------------

def check_balance():

    try:

        account_number = account_entry.get()

        if account_number not in accounts:
            raise ValueError("Account not found")

        account = accounts[account_number]

        details = account.get_details()

        output = f"""
Bank: {BankAccount.bank_name}

Customer Name: {details["name"]}

Account Number: {details["account_number"]}

Balance: ₹{details["balance"]}

Transactions:
{details["transactions"]}
"""

        messagebox.showinfo(
            "Account Details",
            output
        )

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# -------------------------------
# Tkinter GUI
# -------------------------------

root = tk.Tk()

root.title("Python Banking Management System")

root.geometry("450x500")


title_label = tk.Label(
    root,
    text="PYTHON BANK",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=20)


# Name
tk.Label(
    root,
    text="Customer Name"
).pack()

name_entry = tk.Entry(root)

name_entry.pack(pady=5)


# Account Number
tk.Label(
    root,
    text="Account Number"
).pack()

account_entry = tk.Entry(root)

account_entry.pack(pady=5)


# Amount
tk.Label(
    root,
    text="Amount"
).pack()

amount_entry = tk.Entry(root)

amount_entry.pack(pady=5)


# Buttons
tk.Button(
    root,
    text="Create Account",
    command=create_account
).pack(pady=10)


tk.Button(
    root,
    text="Deposit Money",
    command=deposit_money
).pack(pady=5)


tk.Button(
    root,
    text="Withdraw Money",
    command=withdraw_money
).pack(pady=5)


tk.Button(
    root,
    text="Check Balance",
    command=check_balance
).pack(pady=5)


root.mainloop()