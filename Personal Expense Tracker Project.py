# ============================================================
# PERSONAL EXPENSE TRACKER
# ============================================================

import tkinter as tk
from tkinter import messagebox


# ============================================================
# BASIC DATA TYPES
# ============================================================

app_name = "Personal Expense Tracker"   # String
total_expense = 0.0                     # Float
expense_count = 0                       # Integer
app_running = True                       # Boolean


# ============================================================
# TUPLE
# ============================================================

EXPENSE_CATEGORIES = (
    "Food",
    "Travel",
    "Education",
    "Shopping",
    "Bills",
    "Entertainment",
    "Other"
)


# ============================================================
# LIST
# ============================================================

expenses = []


# ============================================================
# SET
# ============================================================

unique_categories = set()


# ============================================================
# DICTIONARY
# ============================================================

expense_summary = {
    "total_expense": 0.0,
    "number_of_expenses": 0
}


# ============================================================
# OOP - EXPENSE CLASS
# ============================================================

class Expense:
    """
    Expense class for storing expense information.
    """

    application = "Personal Expense Tracker"

    def __init__(self, expense_id, title, amount, category):
        self.expense_id = expense_id
        self.title = title
        self.amount = amount
        self.category = category

    def display_expense(self):

        return (
            f"Expense ID: {self.expense_id}\n"
            f"Title: {self.title}\n"
            f"Amount: ₹{self.amount:.2f}\n"
            f"Category: {self.category}\n"
        )

    def __str__(self):

        return f"{self.expense_id} - {self.title}"


# ============================================================
# BUILT-IN CLASS ATTRIBUTES
# ============================================================

print("Class Name:", Expense.__name__)
print("Class Module:", Expense.__module__)
print("Class Documentation:", Expense.__doc__)


# ============================================================
# FUNCTION: ADD EXPENSE
# ============================================================

def add_expense(expense_id, title, amount, category):

    try:

        if expense_id == "":
            raise ValueError(
                "Expense ID cannot be empty."
            )

        if title == "":
            raise ValueError(
                "Expense title cannot be empty."
            )

        # Convert amount to float
        amount = float(amount)

        if amount <= 0:
            raise ValueError(
                "Amount must be greater than zero."
            )

        # Check duplicate expense ID
        for expense in expenses:

            if expense.expense_id == expense_id:

                raise ValueError(
                    "Expense ID already exists."
                )

        # Create object
        expense = Expense(
            expense_id,
            title,
            amount,
            category
        )

        # Add object to list
        expenses.append(expense)

        # Add category to set
        unique_categories.add(category)

        # Update dictionary
        expense_summary["total_expense"] += amount

        expense_summary["number_of_expenses"] += 1

        return True, "Expense added successfully."

    except ValueError as error:

        return False, str(error)


# ============================================================
# FUNCTION: VIEW ALL EXPENSES
# ============================================================

def view_all_expenses():

    if len(expenses) == 0:

        return "No expenses found."

    output = ""

    # RANGE
    for index in range(len(expenses)):

        output += f"\nExpense {index + 1}\n"
        output += "=" * 40
        output += "\n"
        output += expenses[index].display_expense()

    return output


# ============================================================
# FUNCTION: SEARCH BY CATEGORY
# ============================================================

def search_by_category(category):

    output = ""

    found = False

    for expense in expenses:

        if expense.category.lower() == category.lower():

            output += expense.display_expense()
            output += "\n"

            found = True

    if found:

        return output

    return "No expenses found for this category."


# ============================================================
# FUNCTION: DELETE EXPENSE
# ============================================================

def delete_expense(expense_id):

    for expense in expenses:

        if expense.expense_id == expense_id:

            expenses.remove(expense)

            expense_summary["total_expense"] -= expense.amount

            expense_summary["number_of_expenses"] -= 1

            return "Expense deleted successfully."

    return "Expense not found."


# ============================================================
# FUNCTION: SHOW SUMMARY
# ============================================================

def show_summary():

    categories = ", ".join(unique_categories)

    return (
        f"Application: {app_name}\n"
        f"Total Expenses: "
        f"{expense_summary['number_of_expenses']}\n"
        f"Total Amount: ₹"
        f"{expense_summary['total_expense']:.2f}\n"
        f"Categories Used: {categories}"
    )


# ============================================================
# TKINTER FUNCTIONS
# ============================================================

def add_expense_gui():

    expense_id = id_entry.get()
    title = title_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()

    success, message = add_expense(
        expense_id,
        title,
        amount,
        category
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


def view_expenses_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    result = view_all_expenses()

    output_text.insert(
        tk.END,
        result
    )


def search_category_gui():

    category = search_entry.get()

    result = search_by_category(category)

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        result
    )


def delete_expense_gui():

    expense_id = search_entry.get()

    result = delete_expense(expense_id)

    messagebox.showinfo(
        "Delete Result",
        result
    )

    view_expenses_gui()


def summary_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    result = show_summary()

    output_text.insert(
        tk.END,
        result
    )


def clear_fields():

    id_entry.delete(
        0,
        tk.END
    )

    title_entry.delete(
        0,
        tk.END
    )

    amount_entry.delete(
        0,
        tk.END
    )

    category_entry.delete(
        0,
        tk.END
    )


# ============================================================
# TKINTER WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "Personal Expense Tracker"
)

root.geometry(
    "800x750"
)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="PERSONAL EXPENSE TRACKER",
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


# Expense ID

tk.Label(
    form_frame,
    text="Expense ID"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=5
)


id_entry = tk.Entry(
    form_frame,
    width=35
)

id_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)


# Title

tk.Label(
    form_frame,
    text="Title"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


title_entry = tk.Entry(
    form_frame,
    width=35
)

title_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


# Amount

tk.Label(
    form_frame,
    text="Amount"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=5
)


amount_entry = tk.Entry(
    form_frame,
    width=35
)

amount_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)


# Category

tk.Label(
    form_frame,
    text="Category"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=5
)


category_entry = tk.Entry(
    form_frame,
    width=35
)

category_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=5
)


# ============================================================
# BUTTONS
# ============================================================

add_button = tk.Button(
    root,
    text="Add Expense",
    width=25,
    command=add_expense_gui
)

add_button.pack(
    pady=5
)


view_button = tk.Button(
    root,
    text="View All Expenses",
    width=25,
    command=view_expenses_gui
)

view_button.pack(
    pady=5
)


summary_button = tk.Button(
    root,
    text="Show Summary",
    width=25,
    command=summary_gui
)

summary_button.pack(
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
    text="Category / Expense ID"
).grid(
    row=0,
    column=0,
    padx=5
)


search_entry = tk.Entry(
    search_frame,
    width=25
)

search_entry.grid(
    row=0,
    column=1,
    padx=5
)


search_button = tk.Button(
    search_frame,
    text="Search Category",
    command=search_category_gui
)

search_button.grid(
    row=0,
    column=2,
    padx=5
)


delete_button = tk.Button(
    search_frame,
    text="Delete Expense ID",
    command=delete_expense_gui
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
    width=90,
    height=20
)

output_text.pack(
    pady=15
)


# ============================================================
# PROGRAM START
# ============================================================

root.mainloop()