import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


# =====================================================
# FILE NAME
# =====================================================

DATA_FILE = "it_company_data.json"


# =====================================================
# IT COMPANY BUDGET CLASS
# =====================================================

class ITCompanyBudget:

    # Class attribute
    company_name = "CodeTech IT Solutions Pvt Ltd"

    def __init__(self):

        # List
        self.departments = []

        # List of dictionaries
        self.transactions = []

        # Dictionary
        self.budget = {

            "total_income": 0.0,

            "total_expense": 0.0

        }

    # =================================================
    # ADD DEPARTMENT
    # =================================================

    def add_department(self, department):

        if department == "":

            raise ValueError(

                "Department name cannot be empty."

            )

        if department in self.departments:

            raise ValueError(

                "Department already exists."

            )

        self.departments.append(

            department

        )

    # =================================================
    # ADD INCOME
    # =================================================

    def add_income(

        self,

        amount,

        description

    ):

        if amount <= 0:

            raise ValueError(

                "Income must be greater than zero."

            )

        if description == "":

            raise ValueError(

                "Income description is required."

            )

        self.budget[

            "total_income"

        ] += amount

        transaction = {

            "type": "INCOME",

            "department": "Company",

            "category": "Revenue",

            "amount": amount,

            "description": description,

            "status": "SUCCESS"

        }

        self.transactions.append(

            transaction

        )

    # =================================================
    # ADD EXPENSE
    # =================================================

    def add_expense(

        self,

        department,

        category,

        amount,

        description

    ):

        if department == "":

            raise ValueError(

                "Department is required."

            )

        if category == "":

            raise ValueError(

                "Expense category is required."

            )

        if amount <= 0:

            raise ValueError(

                "Expense must be greater than zero."

            )

        self.budget[

            "total_expense"

        ] += amount

        transaction = {

            "type": "EXPENSE",

            "department": department,

            "category": category,

            "amount": amount,

            "description": description,

            "status": "SUCCESS"

        }

        self.transactions.append(

            transaction

        )

    # =================================================
    # CALCULATE REMAINING BUDGET
    # =================================================

    def calculate_balance(self):

        return (

            self.budget[

                "total_income"

            ]

            -

            self.budget[

                "total_expense"

            ]

        )

    # =================================================
    # DEPARTMENT-WISE EXPENSE REPORT
    # =================================================

    def department_report(self):

        report = {}

        for transaction in (

            self.transactions

        ):

            if transaction["type"] == "EXPENSE":

                department = (

                    transaction["department"]

                )

                amount = (

                    transaction["amount"]

                )

                if department not in report:

                    report[department] = 0

                report[department] += amount

        return report

    # =================================================
    # CATEGORY-WISE EXPENSE REPORT
    # =================================================

    def category_report(self):

        report = {}

        for transaction in (

            self.transactions

        ):

            if transaction["type"] == "EXPENSE":

                category = (

                    transaction["category"]

                )

                amount = (

                    transaction["amount"]

                )

                if category not in report:

                    report[category] = 0

                report[category] += amount

        return report

    # =================================================
    # UNIQUE EXPENSE CATEGORIES
    # =================================================

    def get_categories(self):

        categories = set()

        for transaction in (

            self.transactions

        ):

            if transaction["type"] == "EXPENSE":

                categories.add(

                    transaction["category"]

                )

        return categories

    # =================================================
    # SAVE DATA TO FILE
    # =================================================

    def save_data(self):

        data = {

            "company_name":

            self.company_name,

            "departments":

            self.departments,

            "budget":

            self.budget,

            "transactions":

            self.transactions

        }

        with open(

            DATA_FILE,

            "w"

        ) as file:

            json.dump(

                data,

                file,

                indent=4

            )

    # =================================================
    # LOAD DATA FROM FILE
    # =================================================

    def load_data(self):

        if not os.path.exists(

            DATA_FILE

        ):

            return

        try:

            with open(

                DATA_FILE,

                "r"

            ) as file:

                data = json.load(file)

                self.departments = (

                    data.get(

                        "departments",

                        []

                    )

                )

                self.budget = (

                    data.get(

                        "budget",

                        {

                            "total_income": 0,

                            "total_expense": 0

                        }

                    )

                )

                self.transactions = (

                    data.get(

                        "transactions",

                        []

                    )

                )

        except json.JSONDecodeError:

            messagebox.showerror(

                "File Error",

                "Invalid JSON file."

            )


# =====================================================
# TKINTER APPLICATION
# =====================================================

class ITBudgetApp:

    def __init__(self, root):

        self.root = root

        self.root.title(

            "IT Company Budget Management System"

        )

        self.root.geometry(

            "1450x850"

        )

        self.company = ITCompanyBudget()

        self.company.load_data()

        # =================================================
        # TITLE
        # =================================================

        title = tk.Label(

            root,

            text=(

                "IT COMPANY BUDGET MANAGEMENT SYSTEM"

            ),

            font=(

                "Arial",

                24,

                "bold"

            )

        )

        title.pack(pady=10)

        # =================================================
        # INPUT FRAME
        # =================================================

        input_frame = tk.Frame(root)

        input_frame.pack(pady=10)

        # Department

        tk.Label(

            input_frame,

            text="Department"

        ).grid(

            row=0,

            column=0,

            padx=5,

            pady=5

        )

        self.department_entry = tk.Entry(

            input_frame,

            width=25

        )

        self.department_entry.grid(

            row=0,

            column=1

        )

        # Category

        tk.Label(

            input_frame,

            text="Category"

        ).grid(

            row=0,

            column=2,

            padx=5

        )

        self.category_entry = tk.Entry(

            input_frame,

            width=25

        )

        self.category_entry.grid(

            row=0,

            column=3

        )

        # Amount

        tk.Label(

            input_frame,

            text="Amount"

        ).grid(

            row=1,

            column=0,

            padx=5

        )

        self.amount_entry = tk.Entry(

            input_frame,

            width=25

        )

        self.amount_entry.grid(

            row=1,

            column=1

        )

        # Description

        tk.Label(

            input_frame,

            text="Description"

        ).grid(

            row=1,

            column=2,

            padx=5

        )

        self.description_entry = tk.Entry(

            input_frame,

            width=25

        )

        self.description_entry.grid(

            row=1,

            column=3

        )

        # New Department

        tk.Label(

            input_frame,

            text="New Department"

        ).grid(

            row=2,

            column=0,

            padx=5

        )

        self.new_department_entry = tk.Entry(

            input_frame,

            width=25

        )

        self.new_department_entry.grid(

            row=2,

            column=1

        )

        # =================================================
        # BUTTON FRAME
        # =================================================

        button_frame = tk.Frame(root)

        button_frame.pack(pady=10)

        tk.Button(

            button_frame,

            text="Add Department",

            command=self.add_department

        ).grid(

            row=0,

            column=0,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Add Income",

            command=self.add_income

        ).grid(

            row=0,

            column=1,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Add Expense",

            command=self.add_expense

        ).grid(

            row=0,

            column=2,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Budget Summary",

            command=self.show_summary

        ).grid(

            row=0,

            column=3,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Department Report",

            command=self.show_department_report

        ).grid(

            row=0,

            column=4,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Category Report",

            command=self.show_category_report

        ).grid(

            row=0,

            column=5,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Show Categories",

            command=self.show_categories

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
        # TRANSACTION TABLE
        # =================================================

        columns = (

            "Type",

            "Department",

            "Category",

            "Amount",

            "Description",

            "Status"

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

                width=210

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

        self.show_transactions()

    # =================================================
    # ADD DEPARTMENT
    # =================================================

    def add_department(self):

        try:

            department = (

                self.new_department_entry.get()

            )

            self.company.add_department(

                department

            )

            self.company.save_data()

            messagebox.showinfo(

                "Success",

                (

                    "Department added successfully."

                )

            )

            self.clear_fields()

        except ValueError as error:

            messagebox.showerror(

                "Error",

                str(error)

            )

    # =================================================
    # ADD INCOME
    # =================================================

    def add_income(self):

        try:

            amount = float(

                self.amount_entry.get()

            )

            description = (

                self.description_entry.get()

            )

            self.company.add_income(

                amount,

                description

            )

            self.company.save_data()

            self.show_transactions()

            messagebox.showinfo(

                "Success",

                (

                    f"Income ₹{amount} "

                    "added successfully."

                )

            )

            self.clear_fields()

        except ValueError as error:

            messagebox.showerror(

                "Income Error",

                str(error)

            )

    # =================================================
    # ADD EXPENSE
    # =================================================

    def add_expense(self):

        try:

            department = (

                self.department_entry.get()

            )

            category = (

                self.category_entry.get()

            )

            amount = float(

                self.amount_entry.get()

            )

            description = (

                self.description_entry.get()

            )

            self.company.add_expense(

                department,

                category,

                amount,

                description

            )

            self.company.save_data()

            self.show_transactions()

            messagebox.showinfo(

                "Success",

                (

                    f"Expense ₹{amount} "

                    "added successfully."

                )

            )

            self.clear_fields()

        except ValueError as error:

            messagebox.showerror(

                "Expense Error",

                str(error)

            )

    # =================================================
    # SHOW BUDGET SUMMARY
    # =================================================

    def show_summary(self):

        income = (

            self.company.budget[

                "total_income"

            ]

        )

        expense = (

            self.company.budget[

                "total_expense"

            ]

        )

        balance = (

            self.company.calculate_balance()

        )

        messagebox.showinfo(

            "Budget Summary",

            (

                f"Company: "

                f"{self.company.company_name}\n\n"

                f"Total Income: ₹{income}\n"

                f"Total Expense: ₹{expense}\n"

                f"Remaining Budget: ₹{balance}"

            )

        )

    # =================================================
    # DEPARTMENT REPORT
    # =================================================

    def show_department_report(self):

        report = (

            self.company.department_report()

        )

        if not report:

            messagebox.showinfo(

                "Department Report",

                "No expense data available."

            )

            return

        output = ""

        for department, amount in report.items():

            output += (

                f"{department}: ₹{amount}\n"

            )

        messagebox.showinfo(

            "Department Report",

            output

        )

    # =================================================
    # CATEGORY REPORT
    # =================================================

    def show_category_report(self):

        report = (

            self.company.category_report()

        )

        if not report:

            messagebox.showinfo(

                "Category Report",

                "No expense data available."

            )

            return

        output = ""

        for category, amount in report.items():

            output += (

                f"{category}: ₹{amount}\n"

            )

        messagebox.showinfo(

            "Category Report",

            output

        )

    # =================================================
    # SHOW UNIQUE CATEGORIES
    # =================================================

    def show_categories(self):

        categories = (

            self.company.get_categories()

        )

        if categories:

            messagebox.showinfo(

                "Expense Categories",

                "\n".join(categories)

            )

        else:

            messagebox.showinfo(

                "Expense Categories",

                "No categories found."

            )

    # =================================================
    # SHOW TRANSACTIONS
    # =================================================

    def show_transactions(self):

        for item in (

            self.table.get_children()

        ):

            self.table.delete(item)

        for transaction in (

            self.company.transactions

        ):

            self.table.insert(

                "",

                tk.END,

                values=(

                    transaction.get(

                        "type",

                        ""

                    ),

                    transaction.get(

                        "department",

                        ""

                    ),

                    transaction.get(

                        "category",

                        ""

                    ),

                    transaction.get(

                        "amount",

                        0

                    ),

                    transaction.get(

                        "description",

                        ""

                    ),

                    transaction.get(

                        "status",

                        ""

                    )

                )

            )

        self.status_label.config(

            text=(

                f"Total Transactions: "

                f"{len(self.company.transactions)}"

            )

        )

    # =================================================
    # CLEAR INPUT FIELDS
    # =================================================

    def clear_fields(self):

        entries = (

            self.department_entry,

            self.category_entry,

            self.amount_entry,

            self.description_entry,

            self.new_department_entry

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

    app = ITBudgetApp(root)

    root.mainloop()


# =====================================================
# PROGRAM START
# =====================================================

if __name__ == "__main__":

    main()