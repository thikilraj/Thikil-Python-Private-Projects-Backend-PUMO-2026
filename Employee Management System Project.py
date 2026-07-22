# ============================================================
# EMPLOYEE MANAGEMENT SYSTEM
# ============================================================

import tkinter as tk
from tkinter import messagebox


# ============================================================
# PYTHON BASIC DATA TYPES
# ============================================================

company_name = "ABC Technologies"   # String
total_employees = 0                  # Integer
company_rating = 4.5                 # Float
company_active = True                # Boolean


# ============================================================
# TUPLE
# ============================================================

DEPARTMENTS = (
    "IT",
    "HR",
    "Finance",
    "Marketing",
    "Sales"
)


# ============================================================
# LIST
# ============================================================

employees = []


# ============================================================
# SET
# ============================================================

skills = set()


# ============================================================
# DICTIONARY
# ============================================================

employee_statistics = {
    "total": 0,
    "active": 0
}


# ============================================================
# OOP - CLASS
# ============================================================

class Employee:
    """
    Employee class for storing employee information.
    """

    company = "ABC Technologies"

    def __init__(self, employee_id, name, age, department, salary, employee_skills):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
        self.employee_skills = employee_skills

    def display_employee(self):
        """
        Return employee details.
        """

        return (
            f"Employee ID: {self.employee_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Department: {self.department}\n"
            f"Salary: ₹{self.salary}\n"
            f"Skills: {', '.join(self.employee_skills)}\n"
            f"Company: {self.company}\n"
        )

    def __str__(self):
        return f"{self.employee_id} - {self.name}"


# ============================================================
# BUILT-IN CLASS ATTRIBUTES
# ============================================================

print("Class Name:", Employee.__name__)
print("Class Module:", Employee.__module__)
print("Class Documentation:", Employee.__doc__)


# ============================================================
# FUNCTION: ADD EMPLOYEE
# ============================================================

def add_employee(employee_id, name, age, department, salary, employee_skills):

    global total_employees

    try:

        # Validate employee ID
        if employee_id == "":
            raise ValueError("Employee ID cannot be empty.")

        # Validate name
        if name == "":
            raise ValueError("Name cannot be empty.")

        # Convert age to integer
        age = int(age)

        if age < 18:
            raise ValueError("Employee age must be 18 or above.")

        # Convert salary to float
        salary = float(salary)

        if salary <= 0:
            raise ValueError("Salary must be greater than zero.")

        # Check duplicate employee ID
        for employee in employees:
            if employee.employee_id == employee_id:
                raise ValueError("Employee ID already exists.")

        # Convert skills into a list
        skill_list = employee_skills.split(",")

        # Remove unnecessary spaces
        skill_list = [
            skill.strip()
            for skill in skill_list
        ]

        # Add skills to SET
        for skill in skill_list:
            skills.add(skill)

        # Create Employee Object
        employee = Employee(
            employee_id,
            name,
            age,
            department,
            salary,
            skill_list
        )

        # Add object to LIST
        employees.append(employee)

        # Update statistics DICTIONARY
        total_employees += 1

        employee_statistics["total"] = total_employees
        employee_statistics["active"] += 1

        return True, "Employee added successfully."

    except ValueError as error:

        return False, str(error)


# ============================================================
# FUNCTION: DISPLAY ALL EMPLOYEES
# ============================================================

def display_all_employees():

    if len(employees) == 0:

        return "No employees found."

    output = ""

    # RANGE
    for index in range(len(employees)):

        output += f"\nEmployee {index + 1}\n"
        output += "=" * 40
        output += "\n"
        output += employees[index].display_employee()
        output += "\n"

    return output


# ============================================================
# FUNCTION: SEARCH EMPLOYEE
# ============================================================

def search_employee(employee_id):

    for employee in employees:

        if employee.employee_id == employee_id:

            return employee.display_employee()

    return "Employee not found."


# ============================================================
# FUNCTION: DELETE EMPLOYEE
# ============================================================

def delete_employee(employee_id):

    global total_employees

    for employee in employees:

        if employee.employee_id == employee_id:

            employees.remove(employee)

            total_employees -= 1

            employee_statistics["total"] = total_employees
            employee_statistics["active"] -= 1

            return "Employee deleted successfully."

    return "Employee not found."


# ============================================================
# FUNCTION: SHOW STATISTICS
# ============================================================

def show_statistics():

    unique_skills = ", ".join(skills)

    return (
        f"Total Employees: {employee_statistics['total']}\n"
        f"Active Employees: {employee_statistics['active']}\n"
        f"Available Skills: {unique_skills}"
    )


# ============================================================
# TKINTER FUNCTIONS
# ============================================================

def add_employee_gui():

    employee_id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    department = department_entry.get()
    salary = salary_entry.get()
    employee_skills = skills_entry.get()

    success, message = add_employee(
        employee_id,
        name,
        age,
        department,
        salary,
        employee_skills
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

    output = display_all_employees()

    output_text.insert(
        tk.END,
        output
    )


def search_employee_gui():

    employee_id = search_entry.get()

    result = search_employee(employee_id)

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

    result = delete_employee(employee_id)

    messagebox.showinfo(
        "Delete Result",
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

    age_entry.delete(
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

    skills_entry.delete(
        0,
        tk.END
    )


# ============================================================
# TKINTER GUI
# ============================================================

root = tk.Tk()

root.title(
    "Employee Management System"
)

root.geometry(
    "800x750"
)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="EMPLOYEE MANAGEMENT SYSTEM",
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
    text="Name"
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


# Age

tk.Label(
    form_frame,
    text="Age"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=5
)


age_entry = tk.Entry(
    form_frame,
    width=35
)

age_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)


# Department

tk.Label(
    form_frame,
    text="Department"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=5
)


department_entry = tk.Entry(
    form_frame,
    width=35
)

department_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=5
)


# Salary

tk.Label(
    form_frame,
    text="Salary"
).grid(
    row=4,
    column=0,
    padx=10,
    pady=5
)


salary_entry = tk.Entry(
    form_frame,
    width=35
)

salary_entry.grid(
    row=4,
    column=1,
    padx=10,
    pady=5
)


# Skills

tk.Label(
    form_frame,
    text="Skills"
).grid(
    row=5,
    column=0,
    padx=10,
    pady=5
)


skills_entry = tk.Entry(
    form_frame,
    width=35
)

skills_entry.grid(
    row=5,
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
    text="Show Statistics",
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
    width=25
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