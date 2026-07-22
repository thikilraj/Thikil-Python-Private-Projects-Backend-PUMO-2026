# ============================================================
# STUDENT RESULT MANAGEMENT SYSTEM
# ============================================================

import tkinter as tk
from tkinter import messagebox


# ============================================================
# 1. BASIC DATA TYPES
# ============================================================

school_name = "ABC Higher Secondary School"  # String
academic_year = 2026                         # Integer
pass_mark = 40.0                             # Float
result_system_active = True                  # Boolean


# ============================================================
# 2. TUPLE
# ============================================================

SUBJECTS = (
    "Python",
    "Mathematics",
    "English",
    "Science",
    "Computer"
)


# ============================================================
# 3. LIST
# ============================================================

students = []


# ============================================================
# 4. SET
# ============================================================

unique_classes = set()


# ============================================================
# 5. DICTIONARY
# ============================================================

result_statistics = {
    "total_students": 0,
    "total_marks": 0
}


# ============================================================
# 6. OOP - STUDENT CLASS
# ============================================================

class Student:
    """
    Student class for managing student result information.
    """

    school = "ABC Higher Secondary School"

    def __init__(
        self,
        student_id,
        name,
        class_name,
        marks
    ):

        self.student_id = student_id
        self.name = name
        self.class_name = class_name
        self.marks = marks

    def calculate_total(self):

        return sum(self.marks)

    def calculate_average(self):

        return (
            self.calculate_total()
            / len(self.marks)
        )

    def calculate_grade(self):

        average = self.calculate_average()

        if average >= 90:
            return "A+"

        elif average >= 80:
            return "A"

        elif average >= 70:
            return "B"

        elif average >= 60:
            return "C"

        elif average >= 50:
            return "D"

        else:
            return "F"

    def calculate_result(self):

        for mark in self.marks:

            if mark < pass_mark:

                return "FAIL"

        return "PASS"

    def display_student(self):

        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Class: {self.class_name}\n"
            f"Marks: {self.marks}\n"
            f"Total: "
            f"{self.calculate_total()}\n"
            f"Average: "
            f"{self.calculate_average():.2f}\n"
            f"Grade: "
            f"{self.calculate_grade()}\n"
            f"Result: "
            f"{self.calculate_result()}\n"
        )

    def __str__(self):

        return (
            f"{self.student_id} - "
            f"{self.name}"
        )


# ============================================================
# 7. BUILT-IN CLASS ATTRIBUTES
# ============================================================

print(
    "Class Name:",
    Student.__name__
)

print(
    "Class Module:",
    Student.__module__
)

print(
    "Class Documentation:",
    Student.__doc__
)


# ============================================================
# 8. FUNCTION: ADD STUDENT
# ============================================================

def add_student(
    student_id,
    name,
    class_name,
    marks
):

    try:

        if student_id == "":

            raise ValueError(
                "Student ID cannot be empty."
            )

        if name == "":

            raise ValueError(
                "Student name cannot be empty."
            )

        # Convert marks to integers
        marks = [
            int(mark)
            for mark in marks
        ]

        # Validate marks
        for mark in marks:

            if mark < 0 or mark > 100:

                raise ValueError(
                    "Marks must be between "
                    "0 and 100."
                )

        # Check duplicate student ID
        for student in students:

            if (
                student.student_id
                == student_id
            ):

                raise ValueError(
                    "Student ID already exists."
                )

        # Create object
        student = Student(
            student_id,
            name,
            class_name,
            marks
        )

        # Add to list
        students.append(student)

        # Add class to set
        unique_classes.add(class_name)

        # Update dictionary
        result_statistics[
            "total_students"
        ] += 1

        result_statistics[
            "total_marks"
        ] += student.calculate_total()

        return True, (
            "Student added successfully."
        )

    except ValueError as error:

        return False, str(error)


# ============================================================
# 9. FUNCTION: VIEW ALL STUDENTS
# ============================================================

def view_all_students():

    if len(students) == 0:

        return "No student records found."

    output = ""

    # RANGE
    for index in range(
        len(students)
    ):

        output += (
            f"\nStudent "
            f"{index + 1}\n"
        )

        output += "=" * 45

        output += "\n"

        output += (
            students[index]
            .display_student()
        )

    return output


# ============================================================
# 10. FUNCTION: SEARCH STUDENT
# ============================================================

def search_student(student_id):

    for student in students:

        if (
            student.student_id
            == student_id
        ):

            return (
                student
                .display_student()
            )

    return "Student not found."


# ============================================================
# 11. FUNCTION: DELETE STUDENT
# ============================================================

def delete_student(student_id):

    for student in students:

        if (
            student.student_id
            == student_id
        ):

            result_statistics[
                "total_students"
            ] -= 1

            result_statistics[
                "total_marks"
            ] -= student.calculate_total()

            students.remove(student)

            return (
                "Student deleted successfully."
            )

    return "Student not found."


# ============================================================
# 12. FUNCTION: SHOW STATISTICS
# ============================================================

def show_statistics():

    total_students = (
        result_statistics[
            "total_students"
        ]
    )

    total_marks = (
        result_statistics[
            "total_marks"
        ]
    )

    total_subjects = len(SUBJECTS)

    if total_students > 0:

        average = (
            total_marks
            / (
                total_students
                * total_subjects
            )
        )

    else:

        average = 0

    return (
        f"School: {school_name}\n"
        f"Academic Year: "
        f"{academic_year}\n"
        f"Total Students: "
        f"{total_students}\n"
        f"Class Average: "
        f"{average:.2f}\n"
        f"Classes: "
        f"{len(unique_classes)}"
    )


# ============================================================
# 13. TKINTER FUNCTIONS
# ============================================================

def add_student_gui():

    student_id = id_entry.get()

    name = name_entry.get()

    class_name = class_entry.get()

    marks = [
        python_entry.get(),
        maths_entry.get(),
        english_entry.get(),
        science_entry.get(),
        computer_entry.get()
    ]

    success, message = add_student(
        student_id,
        name,
        class_name,
        marks
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

    result = search_student(
        student_id
    )

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        result
    )


def delete_student_gui():

    student_id = search_entry.get()

    result = delete_student(
        student_id
    )

    messagebox.showinfo(
        "Delete Student",
        result
    )

    view_students_gui()


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

    class_entry.delete(
        0,
        tk.END
    )

    python_entry.delete(
        0,
        tk.END
    )

    maths_entry.delete(
        0,
        tk.END
    )

    english_entry.delete(
        0,
        tk.END
    )

    science_entry.delete(
        0,
        tk.END
    )

    computer_entry.delete(
        0,
        tk.END
    )


# ============================================================
# 14. TKINTER WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "Student Result Management System"
)

root.geometry(
    "1000x900"
)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="STUDENT RESULT MANAGEMENT SYSTEM",
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


# Class

tk.Label(
    form_frame,
    text="Class"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=5
)


class_entry = tk.Entry(
    form_frame,
    width=35
)

class_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)


# ============================================================
# MARKS
# ============================================================

tk.Label(
    form_frame,
    text="Python"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=5
)


python_entry = tk.Entry(
    form_frame,
    width=35
)

python_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=5
)


tk.Label(
    form_frame,
    text="Mathematics"
).grid(
    row=4,
    column=0,
    padx=10,
    pady=5
)


maths_entry = tk.Entry(
    form_frame,
    width=35
)

maths_entry.grid(
    row=4,
    column=1,
    padx=10,
    pady=5
)


tk.Label(
    form_frame,
    text="English"
).grid(
    row=5,
    column=0,
    padx=10,
    pady=5
)


english_entry = tk.Entry(
    form_frame,
    width=35
)

english_entry.grid(
    row=5,
    column=1,
    padx=10,
    pady=5
)


tk.Label(
    form_frame,
    text="Science"
).grid(
    row=6,
    column=0,
    padx=10,
    pady=5
)


science_entry = tk.Entry(
    form_frame,
    width=35
)

science_entry.grid(
    row=6,
    column=1,
    padx=10,
    pady=5
)


tk.Label(
    form_frame,
    text="Computer"
).grid(
    row=7,
    column=0,
    padx=10,
    pady=5
)


computer_entry = tk.Entry(
    form_frame,
    width=35
)

computer_entry.grid(
    row=7,
    column=1,
    padx=10,
    pady=5
)


# ============================================================
# BUTTONS
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


statistics_button = tk.Button(
    root,
    text="Result Statistics",
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


delete_button = tk.Button(
    search_frame,
    text="Delete",
    command=delete_student_gui
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
    height=22
)

output_text.pack(
    pady=15
)


# ============================================================
# PROGRAM START
# ============================================================

root.mainloop()