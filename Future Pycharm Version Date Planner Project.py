import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta


# ============================================================
# 1. PYTHON IDENTIFIERS AND VARIABLES
# ============================================================

application_name = "PyCharm Future Version Planner"
current_year = 2026
default_days = 30

application_running = True


# ============================================================
# 2. TUPLE
# ============================================================

VERSION_STATUS = (
    "Planned",
    "In Development",
    "Testing",
    "Released"
)


# ============================================================
# 3. LIST
# ============================================================

versions = []


# ============================================================
# 4. SET
# ============================================================

developers = set()


# ============================================================
# 5. DICTIONARY
# ============================================================

project_statistics = {
    "total_versions": 0,
    "total_features": 0,
    "released_versions": 0
}


# ============================================================
# 6. OOP - VERSION CLASS
# ============================================================

class Version:
    """
    Version class stores PyCharm future version information.
    """

    product_name = "PyCharm"

    def __init__(
        self,
        version_number,
        release_date,
        feature,
        developer,
        status
    ):

        self.version_number = version_number
        self.release_date = release_date
        self.feature = feature
        self.developer = developer
        self.status = status

    def display_version(self):

        return (
            f"Version: "
            f"{self.version_number}\n"
            f"Release Date: "
            f"{self.release_date}\n"
            f"Feature: "
            f"{self.feature}\n"
            f"Developer: "
            f"{self.developer}\n"
            f"Status: "
            f"{self.status}\n"
        )

    def __str__(self):

        return (
            f"PyCharm "
            f"{self.version_number}"
        )


# ============================================================
# 7. BUILT-IN CLASS ATTRIBUTES
# ============================================================

print(
    "Class Name:",
    Version.__name__
)

print(
    "Class Module:",
    Version.__module__
)

print(
    "Class Documentation:",
    Version.__doc__
)


# ============================================================
# 8. DATE VALIDATION FUNCTION
# ============================================================

def validate_date(date_text):

    try:

        date_object = datetime.strptime(
            date_text,
            "%Y-%m-%d"
        )

        return date_object

    except ValueError:

        raise ValueError(
            "Date must be in YYYY-MM-DD format."
        )


# ============================================================
# 9. ADD VERSION FUNCTION
# ============================================================

def add_version(
    version_number,
    release_date,
    feature,
    developer,
    status
):

    try:

        if version_number == "":

            raise ValueError(
                "Version number cannot be empty."
            )

        if feature == "":

            raise ValueError(
                "Feature name cannot be empty."
            )

        if developer == "":

            raise ValueError(
                "Developer name cannot be empty."
            )

        if status not in VERSION_STATUS:

            raise ValueError(
                "Invalid version status."
            )

        # Validate date
        validate_date(
            release_date
        )

        # Check duplicate version
        for version in versions:

            if (
                version.version_number
                == version_number
            ):

                raise ValueError(
                    "Version already exists."
                )

        # Create object
        version = Version(
            version_number,
            release_date,
            feature,
            developer,
            status
        )

        # Add to LIST
        versions.append(version)

        # Add developer to SET
        developers.add(developer)

        # Update DICTIONARY
        project_statistics[
            "total_versions"
        ] += 1

        project_statistics[
            "total_features"
        ] += 1

        if status == "Released":

            project_statistics[
                "released_versions"
            ] += 1

        return True, (
            "Future version added successfully."
        )

    except ValueError as error:

        return False, str(error)


# ============================================================
# 10. CALCULATE FUTURE DATE
# ============================================================

def calculate_future_date(
    start_date,
    days
):

    try:

        date_object = validate_date(
            start_date
        )

        days = int(days)

        if days < 0:

            raise ValueError(
                "Days cannot be negative."
            )

        future_date = (
            date_object
            + timedelta(days=days)
        )

        return (
            future_date.strftime(
                "%Y-%m-%d"
            )
        )

    except ValueError as error:

        return str(error)


# ============================================================
# 11. VIEW ALL VERSIONS
# ============================================================

def view_all_versions():

    if len(versions) == 0:

        return "No future versions found."

    output = ""

    for index in range(
        len(versions)
    ):

        output += (
            f"\nVersion "
            f"{index + 1}\n"
        )

        output += "=" * 50

        output += "\n"

        output += (
            versions[index]
            .display_version()
        )

    return output


# ============================================================
# 12. SEARCH VERSION
# ============================================================

def search_version(
    version_number
):

    for version in versions:

        if (
            version.version_number
            == version_number
        ):

            return (
                version
                .display_version()
            )

    return "Version not found."


# ============================================================
# 13. DELETE VERSION
# ============================================================

def delete_version(
    version_number
):

    for version in versions:

        if (
            version.version_number
            == version_number
        ):

            versions.remove(version)

            project_statistics[
                "total_versions"
            ] -= 1

            project_statistics[
                "total_features"
            ] -= 1

            if version.status == "Released":

                project_statistics[
                    "released_versions"
                ] -= 1

            return (
                "Version deleted successfully."
            )

    return "Version not found."


# ============================================================
# 14. PROJECT STATISTICS
# ============================================================

def show_statistics():

    return (
        f"Application: "
        f"{application_name}\n"
        f"Current Year: "
        f"{current_year}\n"
        f"Product: "
        f"{Version.product_name}\n"
        f"Total Versions: "
        f"{project_statistics['total_versions']}\n"
        f"Total Features: "
        f"{project_statistics['total_features']}\n"
        f"Released Versions: "
        f"{project_statistics['released_versions']}\n"
        f"Developers: "
        f"{len(developers)}"
    )


# ============================================================
# 15. TKINTER GUI FUNCTIONS
# ============================================================

def add_version_gui():

    version_number = version_entry.get()

    release_date = date_entry.get()

    feature = feature_entry.get()

    developer = developer_entry.get()

    status = status_entry.get()

    success, message = add_version(
        version_number,
        release_date,
        feature,
        developer,
        status
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


def view_versions_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        view_all_versions()
    )


def search_version_gui():

    version_number = (
        search_entry.get()
    )

    result = search_version(
        version_number
    )

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        result
    )


def delete_version_gui():

    version_number = (
        search_entry.get()
    )

    result = delete_version(
        version_number
    )

    messagebox.showinfo(
        "Delete Version",
        result
    )

    view_versions_gui()


def statistics_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        show_statistics()
    )


def future_date_gui():

    start_date = (
        start_date_entry.get()
    )

    days = (
        days_entry.get()
    )

    result = calculate_future_date(
        start_date,
        days
    )

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        f"Start Date: {start_date}\n"
        f"Days Added: {days}\n"
        f"Future Date: {result}"
    )


def clear_fields():

    version_entry.delete(
        0,
        tk.END
    )

    date_entry.delete(
        0,
        tk.END
    )

    feature_entry.delete(
        0,
        tk.END
    )

    developer_entry.delete(
        0,
        tk.END
    )

    status_entry.delete(
        0,
        tk.END
    )


# ============================================================
# 16. TKINTER WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "PyCharm Future Version Planner"
)

root.geometry(
    "1000x950"
)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="PYCHARM FUTURE VERSION PLANNER",
    font=("Arial", 20, "bold")
)

title_label.pack(
    pady=15
)


# ============================================================
# ADD VERSION FRAME
# ============================================================

version_frame = tk.LabelFrame(
    root,
    text="Add Future PyCharm Version",
    padx=10,
    pady=10
)

version_frame.pack(
    pady=10
)


# Version

tk.Label(
    version_frame,
    text="Version Number"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=5
)


version_entry = tk.Entry(
    version_frame,
    width=35
)

version_entry.grid(
    row=0,
    column=1
)


# Date

tk.Label(
    version_frame,
    text="Release Date YYYY-MM-DD"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


date_entry = tk.Entry(
    version_frame,
    width=35
)

date_entry.grid(
    row=1,
    column=1
)


# Feature

tk.Label(
    version_frame,
    text="Feature"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=5
)


feature_entry = tk.Entry(
    version_frame,
    width=35
)

feature_entry.grid(
    row=2,
    column=1
)


# Developer

tk.Label(
    version_frame,
    text="Developer"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=5
)


developer_entry = tk.Entry(
    version_frame,
    width=35
)

developer_entry.grid(
    row=3,
    column=1
)


# Status

tk.Label(
    version_frame,
    text="Status"
).grid(
    row=4,
    column=0,
    padx=10,
    pady=5
)


status_entry = tk.Entry(
    version_frame,
    width=35
)

status_entry.grid(
    row=4,
    column=1
)


# Add Button

tk.Button(
    version_frame,
    text="Add Future Version",
    command=add_version_gui,
    width=25
).grid(
    row=5,
    column=0,
    columnspan=2,
    pady=10
)


# ============================================================
# FUTURE DATE CALCULATOR
# ============================================================

date_frame = tk.LabelFrame(
    root,
    text="Future Date Calculator",
    padx=10,
    pady=10
)

date_frame.pack(
    pady=10
)


tk.Label(
    date_frame,
    text="Start Date"
).grid(
    row=0,
    column=0,
    padx=5
)


start_date_entry = tk.Entry(
    date_frame,
    width=20
)

start_date_entry.grid(
    row=0,
    column=1,
    padx=5
)


tk.Label(
    date_frame,
    text="Days"
).grid(
    row=0,
    column=2,
    padx=5
)


days_entry = tk.Entry(
    date_frame,
    width=10
)

days_entry.grid(
    row=0,
    column=3,
    padx=5
)


tk.Button(
    date_frame,
    text="Calculate Future Date",
    command=future_date_gui
).grid(
    row=0,
    column=4,
    padx=5
)


# ============================================================
# SEARCH AND DELETE
# ============================================================

search_frame = tk.LabelFrame(
    root,
    text="Search or Delete Version",
    padx=10,
    pady=10
)

search_frame.pack(
    pady=10
)


search_entry = tk.Entry(
    search_frame,
    width=20
)

search_entry.grid(
    row=0,
    column=0,
    padx=5
)


tk.Button(
    search_frame,
    text="Search",
    command=search_version_gui
).grid(
    row=0,
    column=1,
    padx=5
)


tk.Button(
    search_frame,
    text="Delete",
    command=delete_version_gui
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
    text="View All Future Versions",
    command=view_versions_gui,
    width=30
).pack(
    pady=5
)


tk.Button(
    root,
    text="Show Project Statistics",
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
    width=110,
    height=20
)

output_text.pack(
    pady=15
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()