# ============================================================
# EMPLOYEE PAYROLL MANAGEMENT SYSTEM
# ============================================================

import tkinter as tk
from tkinter import messagebox


# ============================================================
# 1. BASIC DATA TYPES
# ============================================================

company_name = "ABC Technologies"  # String
financial_year = 2026              # Integer
tax_rate = 10.0                    # Float
system_active = True               # Boolean


# ============================================================
# 2. TUPLE
# ============================================================

DEPARTMENTS = (
    "IT",
    "HR",
    "Finance",
    "Marketing",
    "Sales"
)


# ============================================================
# 3. LIST
# ============================================================

employees = []


# ============================================================
# 4. SET
# ============================================================

unique_departments = set()


# ============================================================
# 5. DICTIONARY
# ============================================================

payroll_statistics = {
    "total_employees": 0,
    "total_salary": 0.0
}


# ============================================================
# 6. OOP - EMPLOYEE CLASS
# ============================================================

class Employee:
    """
    Employee class for payroll management.
    """

    company = "ABC Technologies"

    def __init__(
        self,
        employee_id,
        name,
        department,
        basic_salary
    ):

        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.basic_salary = basic_salary

    def calculate_hra(self):

        return self.basic_salary * 0.20

    def calculate_da(self):

        return self.basic_salary * 0.10

    def calculate_tax(self):

        return self.basic_salary * (
            tax_rate / 100
        )

    def calculate_gross_salary(self):

        return (
            self.basic_salary
            + self.calculate_hra()
            + self.calculate_da()
        )

    def calculate_net_salary(self):

        return (
            self.calculate_gross_salary()
            - self.calculate_tax()
        )

    def display_payslip(self):

        return (
            f"Employee ID: "
            f"{self.employee_id}\n"
            f"Employee Name: "
            f"{self.name}\n"
            f"Department: "
            f"{self.department}\n"
            f"Basic Salary: "
            f"₹{self.basic_salary:.2f}\n"
            f"HRA: "
            f"₹{self.calculate_hra():.2f}\n"
            f"DA: "
            f"₹{self.calculate_da():.2f}\n"
            f"Tax: "
            f"₹{self.calculate_tax():.2f}\n"
            f"Gross Salary: "
            f"₹{self.calculate_gross_salary():.2f}\n"
            f"Net Salary: "
            f"₹{self.calculate_net_salary():.2f}\n"
        )

    def __str__(self):

        return (
            f"{self.employee_id} - "
            f"{self.name}"
        )


# ============================================================
# 7. BUILT-IN CLASS ATTRIBUTES
# ============================================================

print(
    "Class Name:",
    Employee.__name__
)

print(
    "Class Module:",
    Employee.__module__
)

print(
    "Class Documentation:",
    Employee.__doc__
)


# ============================================================
# 8. FUNCTION: ADD EMPLOYEE
# ============================================================

def add_employee(
    employee_id,
    name,
    department,
    basic_salary
):

    try:

        if employee_id == "":

            raise ValueError(
                "Employee ID cannot be empty."
            )

        if name == "":

            raise ValueError(
                "Employee name cannot be empty."
            )

        if department == "":

            raise ValueError(
                "Department cannot be empty."
            )

        # Convert salary to float
        basic_salary = float(
            basic_salary
        )

        if basic_salary <= 0:

            raise ValueError(
                "Salary must be greater than zero."
            )

        # Check duplicate ID
        for employee in employees:

            if (
                employee.employee_id
                == employee_id
            ):

                raise ValueError(
                    "Employee ID already exists."
                )

        # Create object
        employee = Employee(
            employee_id,
            name,
            department,
            basic_salary
        )

        # Add employee to list
        employees.append(employee)

        # Add department to set
        unique_departments.add(
            department
        )

        # Update dictionary
        payroll_statistics[
            "total_employees"
        ] += 1

        payroll_statistics[
            "total_salary"
        ] += employee.calculate_net_salary()

        return True, (
            "Employee added successfully."
        )

    except ValueError as error:

        return False, str(error)


# ============================================================
# 9. FUNCTION: VIEW ALL EMPLOYEES
# ============================================================

def view_all_employees():

    if len(employees) == 0:

        return "No employees found."

    output = ""

    # RANGE
    for index in range(
        len(employees)
    ):

        output += (
            f"\nEmployee "
            f"{index + 1}\n"
        )

        output += "=" * 50

        output += "\n"

        output += (
            employees[index]
            .display_payslip()
        )

    return output


# ============================================================
# 10. FUNCTION: SEARCH EMPLOYEE
# ============================================================

def search_employee(employee_id):

    for employee in employees:

        if (
            employee.employee_id
            == employee_id
        ):

            return (
                employee
                .display_payslip()
            )

    return "Employee not found."


# ============================================================
# 11. FUNCTION: DELETE EMPLOYEE
# ============================================================

def delete_employee(employee_id):

    for employee in employees:

        if (
            employee.employee_id
            == employee_id
        ):

            payroll_statistics[
                "total_employees"
            ] -= 1

            payroll_statistics[
                "total_salary"
            ] -= (
                employee.calculate_net_salary()
            )

            employees.remove(employee)

            return (
                "Employee deleted successfully."
            )

    return "Employee not found."


# ============================================================
# 12. FUNCTION: SHOW STATISTICS
# ============================================================

def show_statistics():

    total_employees = (
        payroll_statistics[
            "total_employees"
        ]
    )

    total_salary = (
        payroll_statistics[
            "total_salary"
        ]
    )

    if total_employees > 0:

        average_salary = (
            total_salary
            / total_employees
        )

    else:

        average_salary = 0

    return (
        f"Company: "
        f"{company_name}\n"
        f"Financial Year: "
        f"{financial_year}\n"
        f"Total Employees: "
        f"{total_employees}\n"
        f"Total Net Salary: "
        f"₹{total_salary:.2f}\n"
        f"Average Net Salary: "
        f"₹{average_salary:.2f}\n"
        f"Departments: "
        f"{len(unique_departments)}"
    )


# ============================================================
# 13. TKINTER FUNCTIONS
# ============================================================

def add_employee_gui():

    employee_id = id_entry.get()

    name = name_entry.get()

    department = department_entry.get()

    salary = salary_entry.get()

    success, message = add_employee(
        employee_id,
        name,
        department,
        salary
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


def view_employees_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    result = view_all_employees()

    output_text.insert(
        tk.END,
        result
    )


def search_employee_gui():

    employee_id = search_entry.get()

    result = search_employee(
        employee_id
    )

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        result
    )


def delete_employee_gui():

    employee_id = search_entry.get()

    result = delete_employee(
        employee_id
    )

    messagebox.showinfo(
        "Delete Employee",
        result
    )

    view_employees_gui()


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

    id_entry.delete(
        0,
        tk.END
    )

    name_entry.delete(
        0,
        tk.END
    )

    department_entry.delete(
        0,
        tk.END
    )

    salary_entry.delete(
        0,
        tk.END
    )


# ============================================================
# 14. TKINTER WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "Employee Payroll Management System"
)

root.geometry(
    "1000x900"
)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="EMPLOYEE PAYROLL MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold")
)

title_label.pack(
    pady=15
)


# ============================================================
# FORM
# ============================================================

form_frame = tk.Frame(root)

form_frame.pack(
    pady=10
)


# Employee ID

tk.Label(
    form_frame,
    text="Employee ID"
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


# Name

tk.Label(
    form_frame,
    text="Employee Name"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


name_entry = tk.Entry(
    form_frame,
    width=35
)

name_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


# Department

tk.Label(
    form_frame,
    text="Department"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=5
)


department_entry = tk.Entry(
    form_frame,
    width=35
)

department_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)


# Basic Salary

tk.Label(
    form_frame,
    text="Basic Salary"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=5
)


salary_entry = tk.Entry(
    form_frame,
    width=35
)

salary_entry.grid(
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
    text="Add Employee",
    width=25,
    command=add_employee_gui
)

add_button.pack(
    pady=5
)


view_button = tk.Button(
    root,
    text="View All Employees",
    width=25,
    command=view_employees_gui
)

view_button.pack(
    pady=5
)


statistics_button = tk.Button(
    root,
    text="Payroll Statistics",
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
    text="Employee ID"
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
    command=search_employee_gui
)

search_button.grid(
    row=0,
    column=2,
    padx=5
)


delete_button = tk.Button(
    search_frame,
    text="Delete",
    command=delete_employee_gui
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
    width=110,
    height=25
)

output_text.pack(
    pady=15
)


# ============================================================
# PROGRAM START
# ============================================================

root.mainloop()