import tkinter as tk
from tkinter import messagebox


# =====================================
# OOP: Student Class
# =====================================

class Student:

    # Class attribute
    college_name = "Python Technology College"

    def __init__(self, student_id, name, age, course):

        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def get_details(self):

        # Tuple
        return (
            self.student_id,
            self.name,
            self.age,
            self.course
        )


# =====================================
# Dictionary: Store Students
# =====================================

students = {}


# =====================================
# Set: Store Courses
# =====================================

courses = set()


# =====================================
# Function: Add Student
# =====================================

def add_student():

    try:

        student_id = id_entry.get()
        name = name_entry.get()
        age = int(age_entry.get())
        course = course_entry.get()

        if student_id == "" or name == "" or course == "":
            raise ValueError("Please fill all fields")

        if age <= 0:
            raise ValueError("Age must be greater than zero")

        if student_id in students:
            raise ValueError("Student ID already exists")

        student = Student(
            student_id,
            name,
            age,
            course
        )

        students[student_id] = student

        courses.add(course)

        messagebox.showinfo(
            "Success",
            "Student added successfully!"
        )

        clear_fields()

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# =====================================
# Function: View Students
# =====================================

def view_students():

    try:

        if len(students) == 0:
            raise ValueError("No student records found")

        output = ""

        # List
        student_list = list(students.values())

        # Range
        for i in range(len(student_list)):

            student = student_list[i]

            details = student.get_details()

            output += f"""
Student {i + 1}

Student ID: {details[0]}
Name: {details[1]}
Age: {details[2]}
Course: {details[3]}

-------------------------
"""

        messagebox.showinfo(
            "Student Records",
            output
        )

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# =====================================
# Function: Search Student
# =====================================

def search_student():

    try:

        student_id = id_entry.get()

        if student_id not in students:
            raise ValueError("Student not found")

        student = students[student_id]

        details = student.get_details()

        output = f"""
College: {Student.college_name}

Student ID: {details[0]}
Name: {details[1]}
Age: {details[2]}
Course: {details[3]}
"""

        messagebox.showinfo(
            "Student Details",
            output
        )

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# =====================================
# Function: Delete Student
# =====================================

def delete_student():

    try:

        student_id = id_entry.get()

        if student_id not in students:
            raise ValueError("Student not found")

        del students[student_id]

        messagebox.showinfo(
            "Success",
            "Student deleted successfully!"
        )

        clear_fields()

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# =====================================
# Function: Clear Fields
# =====================================

def clear_fields():

    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)


# =====================================
# Tkinter GUI
# =====================================

root = tk.Tk()

root.title("Student Management System")

root.geometry("500x600")


# Title
tk.Label(
    root,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold")
).pack(pady=20)


# Student ID
tk.Label(
    root,
    text="Student ID"
).pack()

id_entry = tk.Entry(root)

id_entry.pack(pady=5)


# Student Name
tk.Label(
    root,
    text="Student Name"
).pack()

name_entry = tk.Entry(root)

name_entry.pack(pady=5)


# Age
tk.Label(
    root,
    text="Age"
).pack()

age_entry = tk.Entry(root)

age_entry.pack(pady=5)


# Course
tk.Label(
    root,
    text="Course"
).pack()

course_entry = tk.Entry(root)

course_entry.pack(pady=5)


# Buttons
tk.Button(
    root,
    text="Add Student",
    width=25,
    command=add_student
).pack(pady=10)


tk.Button(
    root,
    text="View Students",
    width=25,
    command=view_students
).pack(pady=5)


tk.Button(
    root,
    text="Search Student",
    width=25,
    command=search_student
).pack(pady=5)


tk.Button(
    root,
    text="Delete Student",
    width=25,
    command=delete_student
).pack(pady=5)


tk.Button(
    root,
    text="Clear Fields",
    width=25,
    command=clear_fields
).pack(pady=5)


# Run application
root.mainloop()