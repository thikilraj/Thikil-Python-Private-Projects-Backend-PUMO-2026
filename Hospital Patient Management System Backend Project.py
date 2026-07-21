import tkinter as tk
from tkinter import messagebox


# =====================================
# OOP: Patient Class
# =====================================

class Patient:

    # Class attribute
    hospital_name = "Python Care Hospital"

    def __init__(self, patient_id, name, age, disease):

        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def get_details(self):

        # Tuple
        return (
            self.patient_id,
            self.name,
            self.age,
            self.disease
        )


# =====================================
# Dictionary: Store Patient Records
# =====================================

patients = {}


# =====================================
# Set: Store Diseases
# =====================================

diseases = set()


# =====================================
# Function: Add Patient
# =====================================

def add_patient():

    try:

        patient_id = id_entry.get()
        name = name_entry.get()
        age = int(age_entry.get())
        disease = disease_entry.get()

        if patient_id == "" or name == "" or disease == "":
            raise ValueError("Please fill all fields")

        if age <= 0:
            raise ValueError("Age must be greater than zero")

        if patient_id in patients:
            raise ValueError("Patient ID already exists")

        patient = Patient(
            patient_id,
            name,
            age,
            disease
        )

        patients[patient_id] = patient

        diseases.add(disease)

        messagebox.showinfo(
            "Success",
            "Patient added successfully!"
        )

        clear_fields()

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# =====================================
# Function: View Patients
# =====================================

def view_patients():

    try:

        if len(patients) == 0:
            raise ValueError("No patient records found")

        output = ""

        # List
        patient_list = list(patients.values())

        # Range
        for i in range(len(patient_list)):

            patient = patient_list[i]

            details = patient.get_details()

            output += f"""
Patient {i + 1}

Patient ID: {details[0]}
Name: {details[1]}
Age: {details[2]}
Disease: {details[3]}

-------------------------
"""

        messagebox.showinfo(
            "Patient Records",
            output
        )

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# =====================================
# Function: Search Patient
# =====================================

def search_patient():

    try:

        patient_id = id_entry.get()

        if patient_id not in patients:
            raise ValueError("Patient not found")

        patient = patients[patient_id]

        details = patient.get_details()

        output = f"""
Hospital: {Patient.hospital_name}

Patient ID: {details[0]}
Name: {details[1]}
Age: {details[2]}
Disease: {details[3]}
"""

        messagebox.showinfo(
            "Patient Details",
            output
        )

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# =====================================
# Function: Delete Patient
# =====================================

def delete_patient():

    try:

        patient_id = id_entry.get()

        if patient_id not in patients:
            raise ValueError("Patient not found")

        del patients[patient_id]

        messagebox.showinfo(
            "Success",
            "Patient record deleted successfully!"
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
    disease_entry.delete(0, tk.END)


# =====================================
# Tkinter GUI
# =====================================

root = tk.Tk()

root.title("Hospital Patient Management System")

root.geometry("500x600")


# Title
tk.Label(
    root,
    text="HOSPITAL PATIENT MANAGEMENT",
    font=("Arial", 18, "bold")
).pack(pady=20)


# Patient ID
tk.Label(
    root,
    text="Patient ID"
).pack()

id_entry = tk.Entry(root)

id_entry.pack(pady=5)


# Patient Name
tk.Label(
    root,
    text="Patient Name"
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


# Disease
tk.Label(
    root,
    text="Disease"
).pack()

disease_entry = tk.Entry(root)

disease_entry.pack(pady=5)


# Buttons
tk.Button(
    root,
    text="Add Patient",
    width=25,
    command=add_patient
).pack(pady=10)


tk.Button(
    root,
    text="View Patients",
    width=25,
    command=view_patients
).pack(pady=5)


tk.Button(
    root,
    text="Search Patient",
    width=25,
    command=search_patient
).pack(pady=5)


tk.Button(
    root,
    text="Delete Patient",
    width=25,
    command=delete_patient
).pack(pady=5)


tk.Button(
    root,
    text="Clear Fields",
    width=25,
    command=clear_fields
).pack(pady=5)


# Start Application
root.mainloop()