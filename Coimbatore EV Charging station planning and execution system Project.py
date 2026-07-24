import tkinter as tk
from tkinter import messagebox


# ============================================================
# 1. INTRODUCTION TO PYTHON
# ============================================================

project_name = (
    "Coimbatore EV Charging Station "
    "Planning and Execution System"
)

planning_year = 2026

currency = "₹"


# ============================================================
# 2. IDENTIFIERS AND VARIABLES
# ============================================================

total_project_budget = 0.0

ev_stations = []

station_locations = set()


# ============================================================
# 3. TUPLES
# ============================================================

CHARGER_TYPES = (
    "AC Charger",
    "DC Fast Charger",
    "Ultra Fast Charger"
)


EXECUTION_STATUS = (
    "Planned",
    "Land Survey",
    "Installation",
    "Testing",
    "Operational"
)


# ============================================================
# 4. DICTIONARY
# ============================================================

project_statistics = {

    "total_stations": 0,

    "total_budget": 0.0,

    "total_progress": 0,

    "operational_stations": 0

}


# ============================================================
# 5. OOP - EV STATION CLASS
# ============================================================

class EVStation:
    """
    EVStation class stores EV charging station information.
    """

    project_name = (
        "Coimbatore EV Charging Project"
    )

    def __init__(
        self,
        station_id,
        station_name,
        location,
        charger_type,
        charging_points,
        budget,
        planned_date,
        status,
        progress
    ):

        self.station_id = station_id

        self.station_name = station_name

        self.location = location

        self.charger_type = charger_type

        self.charging_points = charging_points

        self.budget = budget

        self.planned_date = planned_date

        self.status = status

        self.progress = progress


    def display_station(self):

        return (

            f"Station ID: {self.station_id}\n"

            f"Station Name: {self.station_name}\n"

            f"Location: {self.location}\n"

            f"Charger Type: {self.charger_type}\n"

            f"Charging Points: "
            f"{self.charging_points}\n"

            f"Estimated Budget: "
            f"₹{self.budget:.2f}\n"

            f"Planned Date: "
            f"{self.planned_date}\n"

            f"Execution Status: "
            f"{self.status}\n"

            f"Progress: "
            f"{self.progress}%\n"

        )


    def __str__(self):

        return (

            f"{self.station_id} - "

            f"{self.station_name}"

        )


# ============================================================
# 6. BUILT-IN CLASS ATTRIBUTES
# ============================================================

print(

    "Class Name:",

    EVStation.__name__

)


print(

    "Class Module:",

    EVStation.__module__

)


print(

    "Class Documentation:",

    EVStation.__doc__

)


# ============================================================
# 7. SET TOTAL PROJECT BUDGET
# ============================================================

def set_project_budget(amount):

    global total_project_budget

    try:

        amount = float(amount)


        if amount <= 0:

            raise ValueError(

                "Budget must be greater than zero."

            )


        total_project_budget = amount


        return (

            True,

            "Project budget saved successfully."

        )


    except ValueError as error:

        return False, str(error)


# ============================================================
# 8. ADD EV STATION
# ============================================================

def add_station(

    station_id,

    station_name,

    location,

    charger_type,

    charging_points,

    budget,

    planned_date,

    status,

    progress

):

    try:

        # Empty value validation

        if station_id == "":

            raise ValueError(

                "Station ID cannot be empty."

            )


        if station_name == "":

            raise ValueError(

                "Station name cannot be empty."

            )


        if location == "":

            raise ValueError(

                "Location cannot be empty."

            )


        if planned_date == "":

            raise ValueError(

                "Planned date cannot be empty."

            )


        # Validate charger type

        if charger_type not in CHARGER_TYPES:

            raise ValueError(

                "Invalid charger type."

            )


        # Validate execution status

        if status not in EXECUTION_STATUS:

            raise ValueError(

                "Invalid execution status."

            )


        # Convert numeric values

        charging_points = int(

            charging_points

        )


        budget = float(

            budget

        )


        progress = int(

            progress

        )


        # Numeric validation

        if charging_points <= 0:

            raise ValueError(

                "Charging points must be greater than zero."

            )


        if budget <= 0:

            raise ValueError(

                "Budget must be greater than zero."

            )


        if progress < 0 or progress > 100:

            raise ValueError(

                "Progress must be between 0 and 100."

            )


        # Check duplicate station ID

        for station in ev_stations:

            if (

                station.station_id

                == station_id

            ):

                raise ValueError(

                    "Station ID already exists."

                )


        # Create object

        station = EVStation(

            station_id,

            station_name,

            location,

            charger_type,

            charging_points,

            budget,

            planned_date,

            status,

            progress

        )


        # Add object to LIST

        ev_stations.append(

            station

        )


        # Add location to SET

        station_locations.add(

            location

        )


        # Update DICTIONARY

        project_statistics[

            "total_stations"

        ] += 1


        project_statistics[

            "total_budget"

        ] += budget


        project_statistics[

            "total_progress"

        ] += progress


        if status == "Operational":

            project_statistics[

                "operational_stations"

            ] += 1


        return (

            True,

            "EV station added successfully."

        )


    except ValueError as error:

        return False, str(error)


# ============================================================
# 9. VIEW ALL EV STATIONS
# ============================================================

def view_stations():

    if len(ev_stations) == 0:

        return (

            "No EV charging stations found."

        )


    output = ""


    for index in range(

        len(ev_stations)

    ):


        output += (

            f"\nStation "

            f"{index + 1}\n"

        )


        output += (

            "=" * 60

        )


        output += "\n"


        output += (

            ev_stations[index]

            .display_station()

        )


    return output


# ============================================================
# 10. SEARCH STATION
# ============================================================

def search_station(

    station_id

):

    for station in ev_stations:

        if (

            station.station_id

            == station_id

        ):

            return (

                station

                .display_station()

            )


    return (

        "EV charging station not found."

    )


# ============================================================
# 11. DELETE STATION
# ============================================================

def delete_station(

    station_id

):

    for station in ev_stations:

        if (

            station.station_id

            == station_id

        ):


            ev_stations.remove(

                station

            )


            project_statistics[

                "total_stations"

            ] -= 1


            project_statistics[

                "total_budget"

            ] -= station.budget


            project_statistics[

                "total_progress"

            ] -= station.progress


            if (

                station.status

                == "Operational"

            ):

                project_statistics[

                    "operational_stations"

                ] -= 1


            return (

                "EV station deleted successfully."

            )


    return (

        "EV station not found."

    )


# ============================================================
# 12. EXECUTION PLAN REPORT
# ============================================================

def execution_report():

    if len(ev_stations) == 0:

        return (

            "No execution plans available."

        )


    output = ""


    for station in ev_stations:


        output += (

            f"Station: "

            f"{station.station_name}\n"

        )


        output += (

            f"Location: "

            f"{station.location}\n"

        )


        output += (

            f"Status: "

            f"{station.status}\n"

        )


        output += (

            f"Progress: "

            f"{station.progress}%\n"

        )


        output += (

            "-" * 50

        )


        output += "\n"


    return output


# ============================================================
# 13. LOCATION-WISE REPORT
# ============================================================

def location_report():

    if len(ev_stations) == 0:

        return (

            "No stations available."

        )


    location_data = {}


    for station in ev_stations:


        location = station.location


        if location not in location_data:

            location_data[

                location

            ] = 0


        location_data[

            location

        ] += 1


    output = ""


    for location in location_data:


        output += (

            f"{location}: "

            f"{location_data[location]} "

            f"station(s)\n"

        )


    return output


# ============================================================
# 14. CHARGER TYPE REPORT
# ============================================================

def charger_report():

    if len(ev_stations) == 0:

        return (

            "No stations available."

        )


    charger_data = {}


    for station in ev_stations:


        charger = (

            station.charger_type

        )


        if charger not in charger_data:

            charger_data[

                charger

            ] = 0


        charger_data[

            charger

        ] += station.charging_points


    output = ""


    for charger in charger_data:


        output += (

            f"{charger}: "

            f"{charger_data[charger]} "

            f"charging point(s)\n"

        )


    return output


# ============================================================
# 15. PROJECT STATISTICS
# ============================================================

def show_statistics():

    total_stations = (

        project_statistics[

            "total_stations"

        ]

    )


    if total_stations > 0:

        average_progress = (

            project_statistics[

                "total_progress"

            ]

            / total_stations

        )


    else:

        average_progress = 0


    return (

        f"Planning Year: "

        f"{planning_year}\n"

        f"Total EV Stations: "

        f"{total_stations}\n"

        f"Total Project Budget: ₹"

        f"{project_statistics['total_budget']:.2f}\n"

        f"Operational Stations: "

        f"{project_statistics['operational_stations']}\n"

        f"Average Progress: "

        f"{average_progress:.2f}%\n"

        f"Total Locations: "

        f"{len(station_locations)}"

    )


# ============================================================
# 16. TKINTER GUI FUNCTIONS
# ============================================================

def set_budget_gui():

    amount = (

        budget_entry.get()

    )


    success, message = (

        set_project_budget(

            amount

        )

    )


    if success:


        messagebox.showinfo(

            "Success",

            message

        )


        budget_entry.delete(

            0,

            tk.END

        )


    else:


        messagebox.showerror(

            "Error",

            message

        )


def add_station_gui():

    station_id = (

        station_id_entry.get()

    )


    station_name = (

        station_name_entry.get()

    )


    location = (

        location_entry.get()

    )


    charger_type = (

        charger_type_entry.get()

    )


    charging_points = (

        charging_points_entry.get()

    )


    budget = (

        station_budget_entry.get()

    )


    planned_date = (

        planned_date_entry.get()

    )


    status = (

        status_entry.get()

    )


    progress = (

        progress_entry.get()

    )


    success, message = add_station(

        station_id,

        station_name,

        location,

        charger_type,

        charging_points,

        budget,

        planned_date,

        status,

        progress

    )


    if success:


        messagebox.showinfo(

            "Success",

            message

        )


        clear_station_fields()


    else:


        messagebox.showerror(

            "Error",

            message

        )


def view_stations_gui():

    output_text.delete(

        "1.0",

        tk.END

    )


    output_text.insert(

        tk.END,

        view_stations()

    )


def search_station_gui():

    station_id = (

        search_station_entry.get()

    )


    result = search_station(

        station_id

    )


    output_text.delete(

        "1.0",

        tk.END

    )


    output_text.insert(

        tk.END,

        result

    )


def delete_station_gui():

    station_id = (

        search_station_entry.get()

    )


    result = delete_station(

        station_id

    )


    messagebox.showinfo(

        "Delete Station",

        result

    )


    view_stations_gui()


def execution_report_gui():

    output_text.delete(

        "1.0",

        tk.END

    )


    output_text.insert(

        tk.END,

        execution_report()

    )


def location_report_gui():

    output_text.delete(

        "1.0",

        tk.END

    )


    output_text.insert(

        tk.END,

        location_report()

    )


def charger_report_gui():

    output_text.delete(

        "1.0",

        tk.END

    )


    output_text.insert(

        tk.END,

        charger_report()

    )


def statistics_gui():

    output_text.delete(

        "1.0",

        tk.END

    )


    output_text.insert(

        tk.END,

        show_statistics()

    )


def clear_station_fields():

    station_id_entry.delete(

        0,

        tk.END

    )


    station_name_entry.delete(

        0,

        tk.END

    )


    location_entry.delete(

        0,

        tk.END

    )


    charger_type_entry.delete(

        0,

        tk.END

    )


    charging_points_entry.delete(

        0,

        tk.END

    )


    station_budget_entry.delete(

        0,

        tk.END

    )


    planned_date_entry.delete(

        0,

        tk.END

    )


    status_entry.delete(

        0,

        tk.END

    )


    progress_entry.delete(

        0,

        tk.END


    )


# ============================================================
# 17. TKINTER WINDOW
# ============================================================

root = tk.Tk()


root.title(

    "Coimbatore EV Charging Station Planner"

)


root.geometry(

    "1200x1100"

)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(

    root,

    text=(

        "COIMBATORE EV CHARGING STATION "

        "PLANNING AND EXECUTION SYSTEM"

    ),

    font=(

        "Arial",

        20,

        "bold"

    )

)


title_label.pack(

    pady=15

)


# ============================================================
# BUDGET FRAME
# ============================================================

budget_frame = tk.LabelFrame(

    root,

    text=(

        "Set Total EV Project Budget"

    ),

    padx=10,

    pady=10

)


budget_frame.pack(

    pady=10

)


tk.Label(

    budget_frame,

    text="Total Project Budget"

).grid(

    row=0,

    column=0,

    padx=10

)


budget_entry = tk.Entry(

    budget_frame,

    width=30

)


budget_entry.grid(

    row=0,

    column=1

)


tk.Button(

    budget_frame,

    text="Set Budget",

    command=set_budget_gui,

    width=20

).grid(

    row=0,

    column=2,

    padx=10

)


# ============================================================
# STATION FRAME
# ============================================================

station_frame = tk.LabelFrame(

    root,

    text=(

        "Add EV Charging Station Plan"

    ),

    padx=10,

    pady=10

)


station_frame.pack(

    pady=10

)


# Station ID

tk.Label(

    station_frame,

    text="Station ID"

).grid(

    row=0,

    column=0,

    padx=10,

    pady=5

)


station_id_entry = tk.Entry(

    station_frame,

    width=35

)


station_id_entry.grid(

    row=0,

    column=1

)


# Station Name

tk.Label(

    station_frame,

    text="Station Name"

).grid(

    row=1,

    column=0,

    padx=10,

    pady=5

)


station_name_entry = tk.Entry(

    station_frame,

    width=35

)


station_name_entry.grid(

    row=1,

    column=1

)


# Location

tk.Label(

    station_frame,

    text="Location"

).grid(

    row=2,

    column=0,

    padx=10,

    pady=5

)


location_entry = tk.Entry(

    station_frame,

    width=35

)


location_entry.grid(

    row=2,

    column=1

)


# Charger Type

tk.Label(

    station_frame,

    text="Charger Type"

).grid(

    row=3,

    column=0,

    padx=10,

    pady=5

)


charger_type_entry = tk.Entry(

    station_frame,

    width=35

)


charger_type_entry.grid(

    row=3,

    column=1

)


# Charging Points

tk.Label(

    station_frame,

    text="Charging Points"

).grid(

    row=4,

    column=0,

    padx=10,

    pady=5

)


charging_points_entry = tk.Entry(

    station_frame,

    width=35

)


charging_points_entry.grid(

    row=4,

    column=1

)


# Budget

tk.Label(

    station_frame,

    text="Station Budget"

).grid(

    row=5,

    column=0,

    padx=10,

    pady=5

)


station_budget_entry = tk.Entry(

    station_frame,

    width=35

)


station_budget_entry.grid(

    row=5,

    column=1

)


# Planned Date

tk.Label(

    station_frame,

    text="Planned Date"

).grid(

    row=6,

    column=0,

    padx=10,

    pady=5

)


planned_date_entry = tk.Entry(

    station_frame,

    width=35

)


planned_date_entry.grid(

    row=6,

    column=1

)


# Status

tk.Label(

    station_frame,

    text="Execution Status"

).grid(

    row=7,

    column=0,

    padx=10,

    pady=5

)


status_entry = tk.Entry(

    station_frame,

    width=35

)


status_entry.grid(

    row=7,

    column=1

)


# Progress

tk.Label(

    station_frame,

    text="Progress (%)"

).grid(

    row=8,

    column=0,

    padx=10,

    pady=5

)


progress_entry = tk.Entry(

    station_frame,

    width=35

)


progress_entry.grid(

    row=8,

    column=1

)


# Add Button

tk.Button(

    station_frame,

    text="Add EV Station",

    command=add_station_gui,

    width=25

).grid(

    row=9,

    column=0,

    columnspan=2,

    pady=10

)


# ============================================================
# SEARCH AND DELETE FRAME
# ============================================================

search_frame = tk.LabelFrame(

    root,

    text=(

        "Search or Delete EV Station"

    ),

    padx=10,

    pady=10

)


search_frame.pack(

    pady=10

)


search_station_entry = tk.Entry(

    search_frame,

    width=25

)


search_station_entry.grid(

    row=0,

    column=0,

    padx=5

)


tk.Button(

    search_frame,

    text="Search",

    command=search_station_gui

).grid(

    row=0,

    column=1,

    padx=5

)


tk.Button(

    search_frame,

    text="Delete",

    command=delete_station_gui

).grid(

    row=0,

    column=2,

    padx=5

)


# ============================================================
# REPORT BUTTONS
# ============================================================

tk.Button(

    root,

    text="View All EV Stations",

    command=view_stations_gui,

    width=30

).pack(

    pady=5

)


tk.Button(

    root,

    text="Execution Plan Report",

    command=execution_report_gui,

    width=30

).pack(

    pady=5

)


tk.Button(

    root,

    text="Location-wise Report",

    command=location_report_gui,

    width=30

).pack(

    pady=5

)


tk.Button(

    root,

    text="Charger Type Report",

    command=charger_report_gui,

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

    width=130,

    height=20

)


output_text.pack(

    pady=15

)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()