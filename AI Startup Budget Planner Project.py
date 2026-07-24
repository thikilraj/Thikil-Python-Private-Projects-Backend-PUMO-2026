import tkinter as tk
from tkinter import messagebox


# ============================================================
# 1. INTRODUCTION TO PYTHON
# ============================================================

company_name = "SmartAI Startup"
application_name = "AI Startup Budget Planning System"

currency = "₹"


# ============================================================
# 2. PYTHON IDENTIFIERS AND VARIABLES
# ============================================================

monthly_budget = 0.0

expenses = []

expense_categories = set()


# ============================================================
# 3. TUPLE
# ============================================================

EXPENSE_TYPES = (
    "Employee Salary",
    "Cloud Infrastructure",
    "Software Subscription",
    "Marketing",
    "Office",
    "Other"
)


# ============================================================
# 4. DICTIONARY
# ============================================================

budget_statistics = {
    "total_expenses": 0.0,
    "number_of_expenses": 0,
    "remaining_budget": 0.0
}


# ============================================================
# 5. OOP - EXPENSE CLASS
# ============================================================

class Expense:
    """
    Expense class stores startup expense information.
    """

    company_name = "SmartAI Startup"

    def __init__(
        self,
        expense_id,
        expense_name,
        expense_type,
        amount,
        month
    ):

        self.expense_id = expense_id
        self.expense_name = expense_name
        self.expense_type = expense_type
        self.amount = amount
        self.month = month

    def display_expense(self):

        return (
            f"Expense ID: {self.expense_id}\n"
            f"Expense Name: {self.expense_name}\n"
            f"Expense Type: {self.expense_type}\n"
            f"Amount: ₹{self.amount:.2f}\n"
            f"Month: {self.month}\n"
        )

    def __str__(self):

        return (
            f"{self.expense_id} - "
            f"{self.expense_name}"
        )


# ============================================================
# 6. BUILT-IN CLASS ATTRIBUTES
# ============================================================

print(
    "Class Name:",
    Expense.__name__
)

print(
    "Class Module:",
    Expense.__module__
)

print(
    "Class Documentation:",
    Expense.__doc__
)


# ============================================================
# 7. SET MONTHLY BUDGET
# ============================================================

def set_budget(amount):

    global monthly_budget

    try:

        amount = float(amount)

        if amount <= 0:

            raise ValueError(
                "Budget must be greater than zero."
            )

        monthly_budget = amount

        budget_statistics[
            "remaining_budget"
        ] = (
            monthly_budget
            - budget_statistics[
                "total_expenses"
            ]
        )

        return True, (
            "Monthly budget saved successfully."
        )

    except ValueError as error:

        return False, str(error)


# ============================================================
# 8. ADD EXPENSE FUNCTION
# ============================================================

def add_expense(
    expense_id,
    expense_name,
    expense_type,
    amount,
    month
):

    try:

        if expense_id == "":

            raise ValueError(
                "Expense ID cannot be empty."
            )

        if expense_name == "":

            raise ValueError(
                "Expense name cannot be empty."
            )

        if expense_type not in EXPENSE_TYPES:

            raise ValueError(
                "Invalid expense type."
            )

        amount = float(amount)

        if amount <= 0:

            raise ValueError(
                "Amount must be greater than zero."
            )

        if month == "":

            raise ValueError(
                "Month cannot be empty."
            )

        # Check duplicate expense ID

        for expense in expenses:

            if (
                expense.expense_id
                == expense_id
            ):

                raise ValueError(
                    "Expense ID already exists."
                )

        # Create object

        expense = Expense(
            expense_id,
            expense_name,
            expense_type,
            amount,
            month
        )

        # Add to LIST

        expenses.append(expense)

        # Add category to SET

        expense_categories.add(
            expense_type
        )

        # Update DICTIONARY

        budget_statistics[
            "total_expenses"
        ] += amount

        budget_statistics[
            "number_of_expenses"
        ] += 1

        budget_statistics[
            "remaining_budget"
        ] = (
            monthly_budget
            - budget_statistics[
                "total_expenses"
            ]
        )

        return True, (
            "Expense added successfully."
        )

    except ValueError as error:

        return False, str(error)


# ============================================================
# 9. VIEW ALL EXPENSES
# ============================================================

def view_expenses():

    if len(expenses) == 0:

        return "No expenses found."

    output = ""

    for index in range(
        len(expenses)
    ):

        output += (
            f"\nExpense "
            f"{index + 1}\n"
        )

        output += "=" * 50

        output += "\n"

        output += (
            expenses[index]
            .display_expense()
        )

    return output


# ============================================================
# 10. SEARCH EXPENSE
# ============================================================

def search_expense(
    expense_id
):

    for expense in expenses:

        if (
            expense.expense_id
            == expense_id
        ):

            return (
                expense
                .display_expense()
            )

    return "Expense not found."


# ============================================================
# 11. DELETE EXPENSE
# ============================================================

def delete_expense(
    expense_id
):

    for expense in expenses:

        if (
            expense.expense_id
            == expense_id
        ):

            expenses.remove(expense)

            budget_statistics[
                "total_expenses"
            ] -= expense.amount

            budget_statistics[
                "number_of_expenses"
            ] -= 1

            budget_statistics[
                "remaining_budget"
            ] = (
                monthly_budget
                - budget_statistics[
                    "total_expenses"
                ]
            )

            return (
                "Expense deleted successfully."
            )

    return "Expense not found."


# ============================================================
# 12. CALCULATE BUDGET
# ============================================================

def calculate_budget():

    total_expenses = (
        budget_statistics[
            "total_expenses"
        ]
    )

    remaining_budget = (
        monthly_budget
        - total_expenses
    )

    if remaining_budget > 0:

        status = "Within Budget"

    elif remaining_budget == 0:

        status = "Budget Fully Used"

    else:

        status = "Budget Exceeded"

    return (
        f"Monthly Budget: "
        f"₹{monthly_budget:.2f}\n"
        f"Total Expenses: "
        f"₹{total_expenses:.2f}\n"
        f"Remaining Budget: "
        f"₹{remaining_budget:.2f}\n"
        f"Budget Status: "
        f"{status}"
    )


# ============================================================
# 13. CATEGORY-WISE EXPENSE REPORT
# ============================================================

def category_report():

    if len(expenses) == 0:

        return "No expenses available."

    category_totals = {}

    for expense in expenses:

        category = (
            expense.expense_type
        )

        if category not in category_totals:

            category_totals[
                category
            ] = 0

        category_totals[
            category
        ] += expense.amount

    output = ""

    for category in category_totals:

        output += (
            f"{category}: ₹"
            f"{category_totals[category]:.2f}\n"
        )

    return output


# ============================================================
# 14. STATISTICS
# ============================================================

def show_statistics():

    return (
        f"Company: "
        f"{company_name}\n"
        f"Application: "
        f"{application_name}\n"
        f"Monthly Budget: ₹"
        f"{monthly_budget:.2f}\n"
        f"Total Expenses: ₹"
        f"{budget_statistics['total_expenses']:.2f}\n"
        f"Number of Expenses: "
        f"{budget_statistics['number_of_expenses']}\n"
        f"Expense Categories: "
        f"{len(expense_categories)}"
    )


# ============================================================
# 15. TKINTER GUI FUNCTIONS
# ============================================================

def set_budget_gui():

    amount = budget_entry.get()

    success, message = set_budget(
        amount
    )

    if success:

        messagebox.showinfo(
            "Success",
            message
        )

        budget_entry.delete(
            0,
            tk.END
        )

    else:

        messagebox.showerror(
            "Error",
            message
        )


def add_expense_gui():

    expense_id = expense_id_entry.get()

    expense_name = (
        expense_name_entry.get()
    )

    expense_type = (
        expense_type_entry.get()
    )

    amount = amount_entry.get()

    month = month_entry.get()

    success, message = add_expense(
        expense_id,
        expense_name,
        expense_type,
        amount,
        month
    )

    if success:

        messagebox.showinfo(
            "Success",
            message
        )

        clear_expense_fields()

    else:

        messagebox.showerror(
            "Error",
            message
        )


def view_expenses_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        view_expenses()
    )


def search_expense_gui():

    expense_id = (
        search_expense_entry.get()
    )

    result = search_expense(
        expense_id
    )

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        result
    )


def delete_expense_gui():

    expense_id = (
        search_expense_entry.get()
    )

    result = delete_expense(
        expense_id
    )

    messagebox.showinfo(
        "Delete Expense",
        result
    )

    view_expenses_gui()


def budget_calculation_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        calculate_budget()
    )


def category_report_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        category_report()
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


def clear_expense_fields():

    expense_id_entry.delete(
        0,
        tk.END
    )

    expense_name_entry.delete(
        0,
        tk.END
    )

    expense_type_entry.delete(
        0,
        tk.END
    )

    amount_entry.delete(
        0,
        tk.END
    )

    month_entry.delete(
        0,
        tk.END
    )


# ============================================================
# 16. TKINTER WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "AI Startup Budget Planning System"
)

root.geometry(
    "1100x1000"
)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="AI STARTUP BUDGET PLANNING SYSTEM",
    font=("Arial", 20, "bold")
)

title_label.pack(
    pady=15
)


# ============================================================
# BUDGET FRAME
# ============================================================

budget_frame = tk.LabelFrame(
    root,
    text="Set Monthly Startup Budget",
    padx=10,
    pady=10
)

budget_frame.pack(
    pady=10
)


tk.Label(
    budget_frame,
    text="Monthly Budget"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=5
)


budget_entry = tk.Entry(
    budget_frame,
    width=30
)

budget_entry.grid(
    row=0,
    column=1
)


tk.Button(
    budget_frame,
    text="Set Budget",
    command=set_budget_gui,
    width=20
).grid(
    row=0,
    column=2,
    padx=10
)


# ============================================================
# EXPENSE FRAME
# ============================================================

expense_frame = tk.LabelFrame(
    root,
    text="Add Startup Expense",
    padx=10,
    pady=10
)

expense_frame.pack(
    pady=10
)


# Expense ID

tk.Label(
    expense_frame,
    text="Expense ID"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=5
)


expense_id_entry = tk.Entry(
    expense_frame,
    width=35
)

expense_id_entry.grid(
    row=0,
    column=1
)


# Expense Name

tk.Label(
    expense_frame,
    text="Expense Name"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


expense_name_entry = tk.Entry(
    expense_frame,
    width=35
)

expense_name_entry.grid(
    row=1,
    column=1
)


# Expense Type

tk.Label(
    expense_frame,
    text="Expense Type"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=5
)


expense_type_entry = tk.Entry(
    expense_frame,
    width=35
)

expense_type_entry.grid(
    row=2,
    column=1
)


# Amount

tk.Label(
    expense_frame,
    text="Amount"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=5
)


amount_entry = tk.Entry(
    expense_frame,
    width=35
)

amount_entry.grid(
    row=3,
    column=1
)


# Month

tk.Label(
    expense_frame,
    text="Month"
).grid(
    row=4,
    column=0,
    padx=10,
    pady=5
)


month_entry = tk.Entry(
    expense_frame,
    width=35
)

month_entry.grid(
    row=4,
    column=1
)


# Add Expense Button

tk.Button(
    expense_frame,
    text="Add Expense",
    command=add_expense_gui,
    width=25
).grid(
    row=5,
    column=0,
    columnspan=2,
    pady=10
)


# ============================================================
# SEARCH AND DELETE FRAME
# ============================================================

search_frame = tk.LabelFrame(
    root,
    text="Search or Delete Expense",
    padx=10,
    pady=10
)

search_frame.pack(
    pady=10
)


search_expense_entry = tk.Entry(
    search_frame,
    width=25
)

search_expense_entry.grid(
    row=0,
    column=0,
    padx=5
)


tk.Button(
    search_frame,
    text="Search",
    command=search_expense_gui
).grid(
    row=0,
    column=1,
    padx=5
)


tk.Button(
    search_frame,
    text="Delete",
    command=delete_expense_gui
).grid(
    row=0,
    column=2,
    padx=5
)


# ============================================================
# GENERAL BUTTONS
# ============================================================

tk.Button(
    root,
    text="View All Expenses",
    command=view_expenses_gui,
    width=30
).pack(
    pady=5
)


tk.Button(
    root,
    text="Calculate Budget",
    command=budget_calculation_gui,
    width=30
).pack(
    pady=5
)


tk.Button(
    root,
    text="Category-wise Report",
    command=category_report_gui,
    width=30
).pack(
    pady=5
)


tk.Button(
    root,
    text="Show Statistics",
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