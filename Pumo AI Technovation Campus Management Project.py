import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


# =====================================================
# FILE NAME
# =====================================================

DATA_FILE = "campus_data.json"


# =====================================================
# CAMPUS MANAGEMENT CLASS
# =====================================================

class PumoAICampus:

    # Class attributes
    campus_name = "Pumo AI Technovation Campus"

    campus_location = "Tamil Nadu"

    def __init__(self):

        # List
        self.students = []

        # List
        self.courses = []

        # List
        self.enrollments = []

        # Dictionary
        self.finance = {

            "total_revenue": 0.0

        }

        # Set
        self.skills = set()

        self.load_default_courses()

    # =================================================
    # DEFAULT COURSES
    # =================================================

    def load_default_courses(self):

        self.courses = [

            {
                "name": "Python Backend Development",

                "duration": "6 Months",

                "fee": 45000

            },

            {

                "name": "AI and Machine Learning",

                "duration": "6 Months",

                "fee": 55000

            },

            {

                "name": "Data Science",

                "duration": "6 Months",

                "fee": 50000

            },

            {

                "name": "Full Stack Development",

                "duration": "6 Months",

                "fee": 60000

            },

            {

                "name": "Robotics and Automation",

                "duration": "6 Months",

                "fee": 50000

            }

        ]

        for course in self.courses:

            self.skills.add(

                course["name"]

            )

    # =================================================
    # REGISTER STUDENT
    # =================================================

    def register_student(

        self,

        student_id,

        name,

        age,

        phone

    ):

        if student_id == "":

            raise ValueError(

                "Student ID is required."

            )

        if name == "":

            raise ValueError(

                "Student name is required."

            )

        if age < 16:

            raise ValueError(

                "Student must be at least 16 years old."

            )

        if student_id in [

            student["student_id"]

            for student in self.students

        ]:

            raise ValueError(

                "Student ID already exists."

            )

        student = {

            "student_id": student_id,

            "name": name,

            "age": age,

            "phone": phone

        }

        self.students.append(student)

    # =================================================
    # ENROLL STUDENT
    # =================================================

    def enroll_student(

        self,

        student_id,

        course_name

    ):

        student_exists = False

        for student in self.students:

            if student["student_id"] == student_id:

                student_exists = True

                break

        if not student_exists:

            raise ValueError(

                "Student is not registered."

            )

        selected_course = None

        for course in self.courses:

            if course["name"] == course_name:

                selected_course = course

                break

        if selected_course is None:

            raise ValueError(

                "Course not found."

            )

        enrollment = {

            "student_id": student_id,

            "course": course_name,

            "fee": selected_course["fee"],

            "status": "ACTIVE"

        }

        self.enrollments.append(enrollment)

        self.finance["total_revenue"] += (

            selected_course["fee"]

        )

    # =================================================
    # ADD CUSTOM COURSE
    # =================================================

    def add_course(

        self,

        course_name,

        duration,

        fee

    ):

        if course_name == "":

            raise ValueError(

                "Course name is required."

            )

        if fee <= 0:

            raise ValueError(

                "Course fee must be greater than zero."

            )

        course = {

            "name": course_name,

            "duration": duration,

            "fee": fee

        }

        self.courses.append(course)

        self.skills.add(course_name)

    # =================================================
    # GET TOTAL STUDENTS
    # =================================================

    def get_total_students(self):

        return len(self.students)

    # =================================================
    # GET TOTAL ENROLLMENTS
    # =================================================

    def get_total_enrollments(self):

        return len(self.enrollments)

    # =================================================
    # SAVE DATA
    # =================================================

    def save_data(self):

        data = {

            "campus_name": self.campus_name,

            "students": self.students,

            "courses": self.courses,

            "enrollments": self.enrollments,

            "finance": self.finance

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
    # LOAD DATA
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

                self.students = data.get(

                    "students",

                    []

                )

                self.courses = data.get(

                    "courses",

                    self.courses

                )

                self.enrollments = data.get(

                    "enrollments",

                    []

                )

                self.finance = data.get(

                    "finance",

                    {

                        "total_revenue": 0

                    }

                )

        except json.JSONDecodeError:

            messagebox.showerror(

                "File Error",

                "Invalid JSON data."

            )


# =====================================================
# TKINTER GUI
# =====================================================

class CampusApp:

    def __init__(self, root):

        self.root = root

        self.root.title(

            "Pumo AI Technovation Campus"

        )

        self.root.geometry(

            "1450x850"

        )

        self.campus = PumoAICampus()

        self.campus.load_data()

        # =================================================
        # TITLE
        # =================================================

        title = tk.Label(

            root,

            text=(

                "PUMO AI TECHNOVATION CAMPUS"

            ),

            font=(

                "Arial",

                24,

                "bold"

            )

        )

        title.pack(pady=10)

        subtitle = tk.Label(

            root,

            text=(

                "Student and Course Management System"

            ),

            font=(

                "Arial",

                12

            )

        )

        subtitle.pack()

        # =================================================
        # INPUT FRAME
        # =================================================

        input_frame = tk.Frame(root)

        input_frame.pack(pady=15)

        # Student ID

        tk.Label(

            input_frame,

            text="Student ID"

        ).grid(

            row=0,

            column=0,

            padx=5,

            pady=5

        )

        self.student_id_entry = tk.Entry(

            input_frame,

            width=25

        )

        self.student_id_entry.grid(

            row=0,

            column=1

        )

        # Name

        tk.Label(

            input_frame,

            text="Student Name"

        ).grid(

            row=0,

            column=2,

            padx=5

        )

        self.name_entry = tk.Entry(

            input_frame,

            width=25

        )

        self.name_entry.grid(

            row=0,

            column=3

        )

        # Age

        tk.Label(

            input_frame,

            text="Age"

        ).grid(

            row=1,

            column=0,

            padx=5

        )

        self.age_entry = tk.Entry(

            input_frame,

            width=25

        )

        self.age_entry.grid(

            row=1,

            column=1

        )

        # Phone

        tk.Label(

            input_frame,

            text="Phone"

        ).grid(

            row=1,

            column=2,

            padx=5

        )

        self.phone_entry = tk.Entry(

            input_frame,

            width=25

        )

        self.phone_entry.grid(

            row=1,

            column=3

        )

        # Course

        tk.Label(

            input_frame,

            text="Course"

        ).grid(

            row=2,

            column=0,

            padx=5

        )

        self.course_combo = ttk.Combobox(

            input_frame,

            values=[

                course["name"]

                for course in self.campus.courses

            ],

            width=22,

            state="readonly"

        )

        self.course_combo.grid(

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

            text="Register Student",

            command=self.register_student

        ).grid(

            row=0,

            column=0,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Enroll Student",

            command=self.enroll_student

        ).grid(

            row=0,

            column=1,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Show Students",

            command=self.show_students

        ).grid(

            row=0,

            column=2,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Show Courses",

            command=self.show_courses

        ).grid(

            row=0,

            column=3,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Campus Summary",

            command=self.show_summary

        ).grid(

            row=0,

            column=4,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Clear",

            command=self.clear_fields

        ).grid(

            row=0,

            column=5,

            padx=5

        )

        # =================================================
        # TABLE
        # =================================================

        columns = (

            "Student ID",

            "Name",

            "Age",

            "Phone",

            "Course",

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

                width=200

            )

        self.table.pack(

            fill=tk.BOTH,

            expand=True,

            padx=10,

            pady=10

        )

        self.show_students()

    # =================================================
    # REGISTER STUDENT
    # =================================================

    def register_student(self):

        try:

            student_id = (

                self.student_id_entry.get()

            )

            name = (

                self.name_entry.get()

            )

            age = int(

                self.age_entry.get()

            )

            phone = (

                self.phone_entry.get()

            )

            self.campus.register_student(

                student_id,

                name,

                age,

                phone

            )

            self.campus.save_data()

            self.show_students()

            messagebox.showinfo(

                "Success",

                "Student registered successfully."

            )

            self.clear_fields()

        except ValueError as error:

            messagebox.showerror(

                "Registration Error",

                str(error)

            )

    # =================================================
    # ENROLL STUDENT
    # =================================================

    def enroll_student(self):

        try:

            student_id = (

                self.student_id_entry.get()

            )

            course = (

                self.course_combo.get()

            )

            self.campus.enroll_student(

                student_id,

                course

            )

            self.campus.save_data()

            self.show_students()

            messagebox.showinfo(

                "Success",

                "Student enrolled successfully."

            )

            self.clear_fields()

        except ValueError as error:

            messagebox.showerror(

                "Enrollment Error",

                str(error)

            )

    # =================================================
    # SHOW STUDENTS
    # =================================================

    def show_students(self):

        for item in (

            self.table.get_children()

        ):

            self.table.delete(item)

        for student in (

            self.campus.students

        ):

            enrollment = None

            for item in (

                self.campus.enrollments

            ):

                if (

                    item["student_id"]

                    ==

                    student["student_id"]

                ):

                    enrollment = item

                    break

            if enrollment:

                course = enrollment["course"]

                status = enrollment["status"]

            else:

                course = "Not Enrolled"

                status = "REGISTERED"

            self.table.insert(

                "",

                tk.END,

                values=(

                    student["student_id"],

                    student["name"],

                    student["age"],

                    student["phone"],

                    course,

                    status

                )

            )

    # =================================================
    # SHOW COURSES
    # =================================================

    def show_courses(self):

        output = (

            "AVAILABLE COURSES\n\n"

        )

        for course in (

            self.campus.courses

        ):

            output += (

                f"Course: "

                f"{course['name']}\n"

                f"Duration: "

                f"{course['duration']}\n"

                f"Fee: ₹"

                f"{course['fee']}\n\n"

            )

        messagebox.showinfo(

            "Courses",

            output

        )

    # =================================================
    # SHOW SUMMARY
    # =================================================

    def show_summary(self):

        students = (

            self.campus.get_total_students()

        )

        enrollments = (

            self.campus.get_total_enrollments()

        )

        revenue = (

            self.campus.finance[

                "total_revenue"

            ]

        )

        messagebox.showinfo(

            "Campus Summary",

            (

                f"Campus: "

                f"{self.campus.campus_name}\n\n"

                f"Total Students: {students}\n"

                f"Total Enrollments: "

                f"{enrollments}\n"

                f"Total Revenue: ₹{revenue}"

            )

        )

    # =================================================
    # CLEAR FIELDS
    # =================================================

    def clear_fields(self):

        self.student_id_entry.delete(

            0,

            tk.END

        )

        self.name_entry.delete(

            0,

            tk.END

        )

        self.age_entry.delete(

            0,

            tk.END

        )

        self.phone_entry.delete(

            0,

            tk.END

        )

        self.course_combo.set("")


# =====================================================
# MAIN FUNCTION
# =====================================================

def main():

    root = tk.Tk()

    app = CampusApp(root)

    root.mainloop()


# =====================================================
# PROGRAM START
# =====================================================

if __name__ == "__main__":

    main()