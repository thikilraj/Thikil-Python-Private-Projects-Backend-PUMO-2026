# ============================================================
# STUDENT ATTENDANCE MANAGEMENT SYSTEM
# ============================================================

import tkinter as tk
from tkinter import messagebox


# ============================================================
# BASIC DATA TYPES
# ============================================================

school_name = "ABC Higher Secondary School"  # String
school_code = 101                            # Integer
attendance_percentage = 95.5                 # Float
system_active = True                         # Boolean


# ============================================================
# TUPLE
# ============================================================

DEPARTMENTS = (
    "Computer Science",
    "Commerce",
    "Science",
    "Arts"
)


# ============================================================
# LIST
# ============================================================

students = []


# ============================================================
# SET
# ============================================================

unique_departments = set()


# ============================================================
# DICTIONARY
# ============================================================

attendance_summary = {
    "total_students": 0,
    "present_students": 0,
    "absent_students": 0
}


# ============================================================
# OOP - STUDENT CLASS
# ============================================================

class Student:
    """
    Student class for managing student attendance.
    """

    school = "ABC Higher Secondary School"

    def __init__(self, student_id, name, age, department):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.department = department
        self.status = "Not Marked"

    def mark_present(self):
        self.status = "Present"

    def mark_absent(self):
        self.status = "Absent"

    def display_student(self):

        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Department: {self.department}\n"
            f"Attendance: {self.status}\n"
        )

    def __str__(self):

        return f"{self.student_id} - {self.name}"


# ============================================================
# BUILT-IN CLASS ATTRIBUTES
# ============================================================

print("Class Name:", Student.__name__)
print("Class Module:", Student.__module__)
print("Class Documentation:", Student.__doc__)


# ============================================================
# FUNCTION: ADD STUDENT
# ============================================================

def add_student(student_id, name, age, department):

    try:

        if student_id == "":
            raise ValueError(
                "Student ID cannot be empty."
            )

        if name == "":
            raise ValueError(
                "Student name cannot be empty."
            )

        # Convert input string into integer
        age = int(age)

        if age <= 0:
            raise ValueError(
                "Age must be greater than zero."
            )

        # Check duplicate ID
        for student in students:

            if student.student_id == student_id:

                raise ValueError(
                    "Student ID already exists."
                )

        # Create Student Object
        student = Student(
            student_id,
            name,
            age,
            department
        )

        # Add object to list
        students.append(student)

        # Add department to set
        unique_departments.add(department)

        # Update dictionary
        attendance_summary["total_students"] += 1

        return True, "Student added successfully."

    except ValueError as error:

        return False, str(error)


# ============================================================
# FUNCTION: VIEW ALL STUDENTS
# ============================================================

def view_all_students():

    if len(students) == 0:

        return "No students found."

    output = ""

    # RANGE
    for index in range(len(students)):

        output += f"\nStudent {index + 1}\n"
        output += "=" * 40
        output += "\n"
        output += students[index].display_student()

    return output


# ============================================================
# FUNCTION: SEARCH STUDENT
# ============================================================

def search_student(student_id):

    for student in students:

        if student.student_id == student_id:

            return student.display_student()

    return "Student not found."


# ============================================================
# FUNCTION: MARK ATTENDANCE
# ============================================================

def mark_attendance(student_id, status):

    try:

        for student in students:

            if student.student_id == student_id:

                # Remove previous attendance count
                if student.status == "Present":

                    attendance_summary[
                        "present_students"
                    ] -= 1

                elif student.status == "Absent":

                    attendance_summary[
                        "absent_students"
                    ] -= 1

                # Mark new status
                if status.lower() == "present":

                    student.mark_present()

                    attendance_summary[
                        "present_students"
                    ] += 1

                elif status.lower() == "absent":

                    student.mark_absent()

                    attendance_summary[
                        "absent_students"
                    ] += 1

                else:

                    raise ValueError(
                        "Status must be Present or Absent."
                    )

                return "Attendance marked successfully."

        return "Student not found."

    except ValueError as error:

        return str(error)


# ============================================================
# FUNCTION: DELETE STUDENT
# ============================================================

def delete_student(student_id):

    for student in students:

        if student.student_id == student_id:

            if student.status == "Present":

                attendance_summary[
                    "present_students"
                ] -= 1

            elif student.status == "Absent":

                attendance_summary[
                    "absent_students"
                ] -= 1

            students.remove(student)

            attendance_summary[
                "total_students"
            ] -= 1

            return "Student deleted successfully."

    return "Student not found."


# ============================================================
# FUNCTION: SHOW ATTENDANCE SUMMARY
# ============================================================

def show_summary():

    return (
        f"School: {school_name}\n"
        f"Total Students: "
        f"{attendance_summary['total_students']}\n"
        f"Present Students: "
        f"{attendance_summary['present_students']}\n"
        f"Absent Students: "
        f"{attendance_summary['absent_students']}\n"
        f"Departments: "
        f"{', '.join(unique_departments)}"
    )


# ============================================================
# TKINTER FUNCTIONS
# ============================================================

def add_student_gui():

    student_id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    department = department_entry.get()

    success, message = add_student(
        student_id,
        name,
        age,
        department
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


def view_students_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    result = view_all_students()

    output_text.insert(
        tk.END,
        result
    )


def search_student_gui():

    student_id = search_entry.get()

    result = search_student(student_id)

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        result
    )


def mark_attendance_gui():

    student_id = search_entry.get()
    status = status_entry.get()

    result = mark_attendance(
        student_id,
        status
    )

    messagebox.showinfo(
        "Attendance",
        result
    )

    view_students_gui()


def delete_student_gui():

    student_id = search_entry.get()

    result = delete_student(student_id)

    messagebox.showinfo(
        "Delete",
        result
    )

    view_students_gui()


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


# ============================================================
# TKINTER WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "Student Attendance Management System"
)

root.geometry(
    "850x800"
)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="STUDENT ATTENDANCE MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold")
)

title_label.pack(
    pady=15
)


# ============================================================
# STUDENT FORM
# ============================================================

form_frame = tk.Frame(root)

form_frame.pack(
    pady=10
)


# Student ID

tk.Label(
    form_frame,
    text="Student ID"
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
    text="Student Name"
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


# ============================================================
# ADD AND VIEW BUTTONS
# ============================================================

add_button = tk.Button(
    root,
    text="Add Student",
    width=25,
    command=add_student_gui
)

add_button.pack(
    pady=5
)


view_button = tk.Button(
    root,
    text="View All Students",
    width=25,
    command=view_students_gui
)

view_button.pack(
    pady=5
)


summary_button = tk.Button(
    root,
    text="Attendance Summary",
    width=25,
    command=summary_gui
)

summary_button.pack(
    pady=5
)


# ============================================================
# SEARCH AND ATTENDANCE FRAME
# ============================================================

search_frame = tk.Frame(root)

search_frame.pack(
    pady=15
)


tk.Label(
    search_frame,
    text="Student ID"
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
    command=search_student_gui
)

search_button.grid(
    row=0,
    column=2,
    padx=5
)


tk.Label(
    search_frame,
    text="Status"
).grid(
    row=0,
    column=3,
    padx=5
)


status_entry = tk.Entry(
    search_frame,
    width=15
)

status_entry.grid(
    row=0,
    column=4,
    padx=5
)


attendance_button = tk.Button(
    search_frame,
    text="Mark Attendance",
    command=mark_attendance_gui
)

attendance_button.grid(
    row=0,
    column=5,
    padx=5
)


delete_button = tk.Button(
    search_frame,
    text="Delete",
    command=delete_student_gui
)

delete_button.grid(
    row=0,
    column=6,
    padx=5
)


# ============================================================
# OUTPUT AREA
# ============================================================

output_text = tk.Text(
    root,
    width=95,
    height=22
)

output_text.pack(
    pady=15
)


# ============================================================
# PROGRAM START
# ============================================================

root.mainloop()