# ============================================================
# STUDENT COURSE REGISTRATION SYSTEM
# ============================================================

import tkinter as tk
from tkinter import messagebox


# ============================================================
# 1. BASIC DATA TYPES
# ============================================================

college_name = "ABC College"  # String
college_code = 101            # Integer
registration_fee = 250.50     # Float
college_open = True           # Boolean


# ============================================================
# 2. TUPLE
# ============================================================

COURSES = (
    "Python",
    "Java",
    "Web Development",
    "Data Science",
    "Database"
)


# ============================================================
# 3. LIST
# ============================================================

registrations = []


# ============================================================
# 4. SET
# ============================================================

unique_students = set()


# ============================================================
# 5. DICTIONARY
# ============================================================

college_statistics = {
    "total_registrations": 0,
    "total_fees": 0.0
}


# ============================================================
# 6. OOP - REGISTRATION CLASS
# ============================================================

class Registration:
    """
    Registration class for managing student course registrations.
    """

    college = "ABC College"

    def __init__(
        self,
        registration_id,
        student_name,
        course_name,
        duration,
        fee
    ):

        self.registration_id = registration_id
        self.student_name = student_name
        self.course_name = course_name
        self.duration = duration
        self.fee = fee

    def display_registration(self):

        return (
            f"Registration ID: "
            f"{self.registration_id}\n"
            f"Student Name: "
            f"{self.student_name}\n"
            f"Course: "
            f"{self.course_name}\n"
            f"Duration: "
            f"{self.duration} months\n"
            f"Course Fee: ₹"
            f"{self.fee:.2f}\n"
        )

    def __str__(self):

        return (
            f"{self.registration_id} - "
            f"{self.student_name}"
        )


# ============================================================
# 7. BUILT-IN CLASS ATTRIBUTES
# ============================================================

print(
    "Class Name:",
    Registration.__name__
)

print(
    "Class Module:",
    Registration.__module__
)

print(
    "Class Documentation:",
    Registration.__doc__
)


# ============================================================
# 8. FUNCTION: ADD REGISTRATION
# ============================================================

def add_registration(
    registration_id,
    student_name,
    course_name,
    duration,
    fee
):

    try:

        if registration_id == "":

            raise ValueError(
                "Registration ID cannot be empty."
            )

        if student_name == "":

            raise ValueError(
                "Student name cannot be empty."
            )

        # Convert duration to integer
        duration = int(duration)

        if duration <= 0:

            raise ValueError(
                "Duration must be greater than zero."
            )

        # Convert fee to float
        fee = float(fee)

        if fee <= 0:

            raise ValueError(
                "Fee must be greater than zero."
            )

        # Check duplicate ID
        for registration in registrations:

            if (
                registration.registration_id
                == registration_id
            ):

                raise ValueError(
                    "Registration ID already exists."
                )

        # Create object
        registration = Registration(
            registration_id,
            student_name,
            course_name,
            duration,
            fee
        )

        # Add object to list
        registrations.append(
            registration
        )

        # Add student to set
        unique_students.add(
            student_name
        )

        # Update dictionary
        college_statistics[
            "total_registrations"
        ] += 1

        college_statistics[
            "total_fees"
        ] += fee

        return True, (
            "Registration added successfully."
        )

    except ValueError as error:

        return False, str(error)


# ============================================================
# 9. FUNCTION: VIEW ALL REGISTRATIONS
# ============================================================

def view_all_registrations():

    if len(registrations) == 0:

        return "No registrations found."

    output = ""

    # RANGE
    for index in range(
        len(registrations)
    ):

        output += (
            f"\nRegistration "
            f"{index + 1}\n"
        )

        output += "=" * 40

        output += "\n"

        output += (
            registrations[index]
            .display_registration()
        )

    return output


# ============================================================
# 10. FUNCTION: SEARCH REGISTRATION
# ============================================================

def search_registration(
    registration_id
):

    for registration in registrations:

        if (
            registration.registration_id
            == registration_id
        ):

            return (
                registration
                .display_registration()
            )

    return "Registration not found."


# ============================================================
# 11. FUNCTION: DELETE REGISTRATION
# ============================================================

def delete_registration(
    registration_id
):

    for registration in registrations:

        if (
            registration.registration_id
            == registration_id
        ):

            college_statistics[
                "total_registrations"
            ] -= 1

            college_statistics[
                "total_fees"
            ] -= registration.fee

            registrations.remove(
                registration
            )

            return (
                "Registration deleted successfully."
            )

    return "Registration not found."


# ============================================================
# 12. FUNCTION: SHOW STATISTICS
# ============================================================

def show_statistics():

    return (
        f"College: {college_name}\n"
        f"Total Registrations: "
        f"{college_statistics['total_registrations']}\n"
        f"Total Fees Collected: ₹"
        f"{college_statistics['total_fees']:.2f}\n"
        f"Unique Students: "
        f"{len(unique_students)}"
    )


# ============================================================
# 13. TKINTER FUNCTIONS
# ============================================================

def add_registration_gui():

    registration_id = id_entry.get()

    student_name = student_entry.get()

    course_name = course_entry.get()

    duration = duration_entry.get()

    fee = fee_entry.get()

    success, message = add_registration(
        registration_id,
        student_name,
        course_name,
        duration,
        fee
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


def view_registrations_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    result = (
        view_all_registrations()
    )

    output_text.insert(
        tk.END,
        result
    )


def search_registration_gui():

    registration_id = (
        search_entry.get()
    )

    result = search_registration(
        registration_id
    )

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        result
    )


def delete_registration_gui():

    registration_id = (
        search_entry.get()
    )

    result = delete_registration(
        registration_id
    )

    messagebox.showinfo(
        "Delete",
        result
    )

    view_registrations_gui()


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

    student_entry.delete(
        0,
        tk.END
    )

    course_entry.delete(
        0,
        tk.END
    )

    duration_entry.delete(
        0,
        tk.END
    )

    fee_entry.delete(
        0,
        tk.END
    )


# ============================================================
# 14. TKINTER WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "Student Course Registration System"
)

root.geometry(
    "900x800"
)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="STUDENT COURSE REGISTRATION SYSTEM",
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


# Registration ID

tk.Label(
    form_frame,
    text="Registration ID"
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


# Student Name

tk.Label(
    form_frame,
    text="Student Name"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


student_entry = tk.Entry(
    form_frame,
    width=35
)

student_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


# Course Name

tk.Label(
    form_frame,
    text="Course Name"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=5
)


course_entry = tk.Entry(
    form_frame,
    width=35
)

course_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)


# Duration

tk.Label(
    form_frame,
    text="Duration (Months)"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=5
)


duration_entry = tk.Entry(
    form_frame,
    width=35
)

duration_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=5
)


# Fee

tk.Label(
    form_frame,
    text="Course Fee"
).grid(
    row=4,
    column=0,
    padx=10,
    pady=5
)


fee_entry = tk.Entry(
    form_frame,
    width=35
)

fee_entry.grid(
    row=4,
    column=1,
    padx=10,
    pady=5
)


# ============================================================
# BUTTONS
# ============================================================

add_button = tk.Button(
    root,
    text="Add Registration",
    width=25,
    command=add_registration_gui
)

add_button.pack(
    pady=5
)


view_button = tk.Button(
    root,
    text="View All Registrations",
    width=25,
    command=view_registrations_gui
)

view_button.pack(
    pady=5
)


statistics_button = tk.Button(
    root,
    text="College Statistics",
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
    text="Registration ID"
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
    command=search_registration_gui
)

search_button.grid(
    row=0,
    column=2,
    padx=5
)


delete_button = tk.Button(
    search_frame,
    text="Delete",
    command=delete_registration_gui
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