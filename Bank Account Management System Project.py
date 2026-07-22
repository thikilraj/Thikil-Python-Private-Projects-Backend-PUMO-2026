# ============================================================
# BANK ACCOUNT MANAGEMENT SYSTEM
# ============================================================

import tkinter as tk
from tkinter import messagebox


# ============================================================
# BASIC DATA TYPES
# ============================================================

bank_name = "ABC National Bank"  # String
bank_code = 101                  # Integer
interest_rate = 6.5              # Float
bank_active = True               # Boolean


# ============================================================
# TUPLE
# ============================================================

ACCOUNT_TYPES = (
    "Savings",
    "Current",
    "Salary"
)


# ============================================================
# LIST
# ============================================================

accounts = []


# ============================================================
# SET
# ============================================================

account_holders = set()


# ============================================================
# DICTIONARY
# ============================================================

bank_statistics = {
    "total_accounts": 0,
    "total_balance": 0.0
}


# ============================================================
# OOP - BANK ACCOUNT CLASS
# ============================================================

class BankAccount:
    """
    BankAccount class for managing bank accounts.
    """

    bank = "ABC National Bank"

    def __init__(
        self,
        account_number,
        holder_name,
        account_type,
        balance
    ):

        self.account_number = account_number
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):

        try:

            amount = float(amount)

            if amount <= 0:

                raise ValueError(
                    "Deposit amount must be greater than zero."
                )

            self.balance += amount

            return "Money deposited successfully."

        except ValueError as error:

            return str(error)

    def withdraw(self, amount):

        try:

            amount = float(amount)

            if amount <= 0:

                raise ValueError(
                    "Withdrawal amount must be greater than zero."
                )

            if amount > self.balance:

                raise ValueError(
                    "Insufficient balance."
                )

            self.balance -= amount

            return "Money withdrawn successfully."

        except ValueError as error:

            return str(error)

    def display_account(self):

        return (
            f"Account Number: {self.account_number}\n"
            f"Holder Name: {self.holder_name}\n"
            f"Account Type: {self.account_type}\n"
            f"Balance: ₹{self.balance:.2f}\n"
        )

    def __str__(self):

        return (
            f"{self.account_number} - "
            f"{self.holder_name}"
        )


# ============================================================
# BUILT-IN CLASS ATTRIBUTES
# ============================================================

print("Class Name:", BankAccount.__name__)
print("Class Module:", BankAccount.__module__)
print("Class Documentation:", BankAccount.__doc__)


# ============================================================
# FUNCTION: CREATE ACCOUNT
# ============================================================

def create_account(
    account_number,
    holder_name,
    account_type,
    initial_balance
):

    try:

        if account_number == "":

            raise ValueError(
                "Account number cannot be empty."
            )

        if holder_name == "":

            raise ValueError(
                "Account holder name cannot be empty."
            )

        initial_balance = float(
            initial_balance
        )

        if initial_balance < 0:

            raise ValueError(
                "Initial balance cannot be negative."
            )

        # Check duplicate account number
        for account in accounts:

            if (
                account.account_number
                == account_number
            ):

                raise ValueError(
                    "Account number already exists."
                )

        # Create object
        account = BankAccount(
            account_number,
            holder_name,
            account_type,
            initial_balance
        )

        # Add object to list
        accounts.append(account)

        # Add name to set
        account_holders.add(holder_name)

        # Update dictionary
        bank_statistics[
            "total_accounts"
        ] += 1

        bank_statistics[
            "total_balance"
        ] += initial_balance

        return True, "Account created successfully."

    except ValueError as error:

        return False, str(error)


# ============================================================
# FUNCTION: VIEW ALL ACCOUNTS
# ============================================================

def view_all_accounts():

    if len(accounts) == 0:

        return "No accounts found."

    output = ""

    # RANGE
    for index in range(len(accounts)):

        output += (
            f"\nAccount {index + 1}\n"
        )

        output += "=" * 40

        output += "\n"

        output += (
            accounts[index]
            .display_account()
        )

    return output


# ============================================================
# FUNCTION: SEARCH ACCOUNT
# ============================================================

def search_account(account_number):

    for account in accounts:

        if (
            account.account_number
            == account_number
        ):

            return (
                account.display_account()
            )

    return "Account not found."


# ============================================================
# FUNCTION: DEPOSIT MONEY
# ============================================================

def deposit_money(
    account_number,
    amount
):

    try:

        amount = float(amount)

        if amount <= 0:

            raise ValueError(
                "Amount must be greater than zero."
            )

        for account in accounts:

            if (
                account.account_number
                == account_number
            ):

                result = account.deposit(
                    amount
                )

                bank_statistics[
                    "total_balance"
                ] += amount

                return result

        return "Account not found."

    except ValueError as error:

        return str(error)


# ============================================================
# FUNCTION: WITHDRAW MONEY
# ============================================================

def withdraw_money(
    account_number,
    amount
):

    try:

        amount = float(amount)

        if amount <= 0:

            raise ValueError(
                "Amount must be greater than zero."
            )

        for account in accounts:

            if (
                account.account_number
                == account_number
            ):

                if amount > account.balance:

                    raise ValueError(
                        "Insufficient balance."
                    )

                result = account.withdraw(
                    amount
                )

                bank_statistics[
                    "total_balance"
                ] -= amount

                return result

        return "Account not found."

    except ValueError as error:

        return str(error)


# ============================================================
# FUNCTION: DELETE ACCOUNT
# ============================================================

def delete_account(
    account_number
):

    for account in accounts:

        if (
            account.account_number
            == account_number
        ):

            bank_statistics[
                "total_balance"
            ] -= account.balance

            bank_statistics[
                "total_accounts"
            ] -= 1

            accounts.remove(account)

            return (
                "Account deleted successfully."
            )

    return "Account not found."


# ============================================================
# FUNCTION: BANK STATISTICS
# ============================================================

def show_statistics():

    return (
        f"Bank: {bank_name}\n"
        f"Total Accounts: "
        f"{bank_statistics['total_accounts']}\n"
        f"Total Bank Balance: ₹"
        f"{bank_statistics['total_balance']:.2f}\n"
        f"Unique Account Holders: "
        f"{len(account_holders)}"
    )


# ============================================================
# TKINTER FUNCTIONS
# ============================================================

def create_account_gui():

    account_number = account_number_entry.get()

    holder_name = holder_name_entry.get()

    account_type = account_type_entry.get()

    initial_balance = balance_entry.get()

    success, message = create_account(
        account_number,
        holder_name,
        account_type,
        initial_balance
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


def view_accounts_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    result = view_all_accounts()

    output_text.insert(
        tk.END,
        result
    )


def search_account_gui():

    account_number = search_entry.get()

    result = search_account(
        account_number
    )

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        result
    )


def deposit_gui():

    account_number = search_entry.get()

    amount = amount_entry.get()

    result = deposit_money(
        account_number,
        amount
    )

    messagebox.showinfo(
        "Deposit",
        result
    )

    view_accounts_gui()


def withdraw_gui():

    account_number = search_entry.get()

    amount = amount_entry.get()

    result = withdraw_money(
        account_number,
        amount
    )

    messagebox.showinfo(
        "Withdrawal",
        result
    )

    view_accounts_gui()


def delete_account_gui():

    account_number = search_entry.get()

    result = delete_account(
        account_number
    )

    messagebox.showinfo(
        "Delete Account",
        result
    )

    view_accounts_gui()


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

    account_number_entry.delete(
        0,
        tk.END
    )

    holder_name_entry.delete(
        0,
        tk.END
    )

    account_type_entry.delete(
        0,
        tk.END
    )

    balance_entry.delete(
        0,
        tk.END
    )


# ============================================================
# TKINTER WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "Bank Account Management System"
)

root.geometry(
    "900x800"
)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="BANK ACCOUNT MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold")
)

title_label.pack(
    pady=15
)


# ============================================================
# ACCOUNT FORM
# ============================================================

form_frame = tk.Frame(root)

form_frame.pack(
    pady=10
)


# Account Number

tk.Label(
    form_frame,
    text="Account Number"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=5
)


account_number_entry = tk.Entry(
    form_frame,
    width=35
)

account_number_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)


# Holder Name

tk.Label(
    form_frame,
    text="Holder Name"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


holder_name_entry = tk.Entry(
    form_frame,
    width=35
)

holder_name_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


# Account Type

tk.Label(
    form_frame,
    text="Account Type"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=5
)


account_type_entry = tk.Entry(
    form_frame,
    width=35
)

account_type_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)


# Initial Balance

tk.Label(
    form_frame,
    text="Initial Balance"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=5
)


balance_entry = tk.Entry(
    form_frame,
    width=35
)

balance_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=5
)


# ============================================================
# CREATE ACCOUNT BUTTON
# ============================================================

create_button = tk.Button(
    root,
    text="Create Account",
    width=25,
    command=create_account_gui
)

create_button.pack(
    pady=5
)


# ============================================================
# VIEW ACCOUNTS
# ============================================================

view_button = tk.Button(
    root,
    text="View All Accounts",
    width=25,
    command=view_accounts_gui
)

view_button.pack(
    pady=5
)


# ============================================================
# STATISTICS
# ============================================================

statistics_button = tk.Button(
    root,
    text="Bank Statistics",
    width=25,
    command=statistics_gui
)

statistics_button.pack(
    pady=5
)


# ============================================================
# SEARCH AND OPERATIONS
# ============================================================

operation_frame = tk.Frame(root)

operation_frame.pack(
    pady=15
)


tk.Label(
    operation_frame,
    text="Account Number"
).grid(
    row=0,
    column=0,
    padx=5
)


search_entry = tk.Entry(
    operation_frame,
    width=20
)

search_entry.grid(
    row=0,
    column=1,
    padx=5
)


search_button = tk.Button(
    operation_frame,
    text="Search",
    command=search_account_gui
)

search_button.grid(
    row=0,
    column=2,
    padx=5
)


tk.Label(
    operation_frame,
    text="Amount"
).grid(
    row=0,
    column=3,
    padx=5
)


amount_entry = tk.Entry(
    operation_frame,
    width=15
)

amount_entry.grid(
    row=0,
    column=4,
    padx=5
)


deposit_button = tk.Button(
    operation_frame,
    text="Deposit",
    command=deposit_gui
)

deposit_button.grid(
    row=0,
    column=5,
    padx=5
)


withdraw_button = tk.Button(
    operation_frame,
    text="Withdraw",
    command=withdraw_gui
)

withdraw_button.grid(
    row=0,
    column=6,
    padx=5
)


delete_button = tk.Button(
    operation_frame,
    text="Delete",
    command=delete_account_gui
)

delete_button.grid(
    row=0,
    column=7,
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