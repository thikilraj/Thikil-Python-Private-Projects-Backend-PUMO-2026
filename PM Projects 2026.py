import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


# =====================================================
# FILE NAME
# =====================================================

DATA_FILE = "plans_data.json"


# =====================================================
# PRIME MINISTER PLANS CLASS
# =====================================================

class PrimeMinisterPlans:

    # Built-in class attributes
    project_title = "Prime Minister National Development Plans 2026"

    country = "India"

    def __init__(self):

        # List
        self.plans = []

        # Dictionary
        self.budget = {

            "total_budget": 0.0

        }

        # Set
        self.ministries = set()

        # Load sample plans
        self.load_default_plans()

    # =================================================
    # DEFAULT PLANS
    # =================================================

    def load_default_plans(self):

        sample_plans = [

            {
                "plan_id": "PM2026-001",

                "plan_name":
                "Digital India Expansion",

                "ministry":
                "Technology",

                "budget":
                500000000,

                "status":
                "Ongoing",

                "beneficiaries":
                1000000

            },

            {
                "plan_id": "PM2026-002",

                "plan_name":
                "National Skill Development",

                "ministry":
                "Education",

                "budget":
                750000000,

                "status":
                "Planned",

                "beneficiaries":
                500000

            },

            {
                "plan_id": "PM2026-003",

                "plan_name":
                "Green Energy Mission",

                "ministry":
                "Environment",

                "budget":
                900000000,

                "status":
                "Ongoing",

                "beneficiaries":
                2000000

            }

        ]

        for plan in sample_plans:

            self.plans.append(plan)

            self.ministries.add(

                plan["ministry"]

            )

            self.budget["total_budget"] += (

                plan["budget"]

            )

    # =================================================
    # ADD NEW PLAN
    # =================================================

    def add_plan(

        self,

        plan_id,

        plan_name,

        ministry,

        budget,

        status,

        beneficiaries

    ):

        if plan_id == "":

            raise ValueError(

                "Plan ID is required."

            )

        if plan_name == "":

            raise ValueError(

                "Plan name is required."

            )

        if budget <= 0:

            raise ValueError(

                "Budget must be greater than zero."

            )

        if beneficiaries < 0:

            raise ValueError(

                "Beneficiaries cannot be negative."

            )

        # Check duplicate plan ID

        for plan in self.plans:

            if plan["plan_id"] == plan_id:

                raise ValueError(

                    "Plan ID already exists."

                )

        new_plan = {

            "plan_id": plan_id,

            "plan_name": plan_name,

            "ministry": ministry,

            "budget": budget,

            "status": status,

            "beneficiaries": beneficiaries

        }

        self.plans.append(new_plan)

        self.ministries.add(ministry)

        self.budget["total_budget"] += budget

    # =================================================
    # UPDATE PLAN STATUS
    # =================================================

    def update_status(

        self,

        plan_id,

        new_status

    ):

        for plan in self.plans:

            if plan["plan_id"] == plan_id:

                plan["status"] = new_status

                return

        raise ValueError(

            "Plan ID not found."

        )

    # =================================================
    # SEARCH PLAN
    # =================================================

    def search_plan(

        self,

        plan_id

    ):

        for plan in self.plans:

            if plan["plan_id"] == plan_id:

                return plan

        return None

    # =================================================
    # GET TOTAL PLANS
    # =================================================

    def get_total_plans(self):

        return len(self.plans)

    # =================================================
    # GET COMPLETED PLANS
    # =================================================

    def get_completed_plans(self):

        completed = 0

        for plan in self.plans:

            if plan["status"] == "Completed":

                completed += 1

        return completed

    # =================================================
    # GET TOTAL BENEFICIARIES
    # =================================================

    def get_total_beneficiaries(self):

        total = 0

        for plan in self.plans:

            total += plan["beneficiaries"]

        return total

    # =================================================
    # SAVE DATA
    # =================================================

    def save_data(self):

        data = {

            "project_title":

            self.project_title,

            "plans":

            self.plans,

            "budget":

            self.budget,

            "ministries":

            list(self.ministries)

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

                self.plans = data.get(

                    "plans",

                    self.plans

                )

                self.budget = data.get(

                    "budget",

                    self.budget

                )

                self.ministries = set(

                    data.get(

                        "ministries",

                        []

                    )

                )

        except json.JSONDecodeError:

            messagebox.showerror(

                "File Error",

                "Invalid JSON data."

            )


# =====================================================
# TKINTER APPLICATION
# =====================================================

class PlansApp:

    def __init__(self, root):

        self.root = root

        self.root.title(

            "Prime Minister Plans Project 2026"

        )

        self.root.geometry(

            "1500x850"

        )

        self.manager = PrimeMinisterPlans()

        self.manager.load_data()

        # =================================================
        # TITLE
        # =================================================

        title = tk.Label(

            root,

            text=(

                "PRIME MINISTER NATIONAL DEVELOPMENT PLANS 2026"

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

                "Educational National Project Management System"

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

        # Plan ID

        tk.Label(

            input_frame,

            text="Plan ID"

        ).grid(

            row=0,

            column=0,

            padx=5,

            pady=5

        )

        self.plan_id_entry = tk.Entry(

            input_frame,

            width=25

        )

        self.plan_id_entry.grid(

            row=0,

            column=1

        )

        # Plan Name

        tk.Label(

            input_frame,

            text="Plan Name"

        ).grid(

            row=0,

            column=2,

            padx=5

        )

        self.plan_name_entry = tk.Entry(

            input_frame,

            width=30

        )

        self.plan_name_entry.grid(

            row=0,

            column=3

        )

        # Ministry

        tk.Label(

            input_frame,

            text="Ministry"

        ).grid(

            row=1,

            column=0,

            padx=5

        )

        self.ministry_entry = tk.Entry(

            input_frame,

            width=25

        )

        self.ministry_entry.grid(

            row=1,

            column=1

        )

        # Budget

        tk.Label(

            input_frame,

            text="Budget"

        ).grid(

            row=1,

            column=2,

            padx=5

        )

        self.budget_entry = tk.Entry(

            input_frame,

            width=30

        )

        self.budget_entry.grid(

            row=1,

            column=3

        )

        # Beneficiaries

        tk.Label(

            input_frame,

            text="Beneficiaries"

        ).grid(

            row=2,

            column=0,

            padx=5

        )

        self.beneficiaries_entry = tk.Entry(

            input_frame,

            width=25

        )

        self.beneficiaries_entry.grid(

            row=2,

            column=1

        )

        # Status

        tk.Label(

            input_frame,

            text="Status"

        ).grid(

            row=2,

            column=2,

            padx=5

        )

        self.status_combo = ttk.Combobox(

            input_frame,

            values=[

                "Planned",

                "Ongoing",

                "Completed"

            ],

            width=27,

            state="readonly"

        )

        self.status_combo.grid(

            row=2,

            column=3

        )

        # =================================================
        # BUTTONS
        # =================================================

        button_frame = tk.Frame(root)

        button_frame.pack(pady=10)

        tk.Button(

            button_frame,

            text="Add Plan",

            command=self.add_plan

        ).grid(

            row=0,

            column=0,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Update Status",

            command=self.update_status

        ).grid(

            row=0,

            column=1,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Show Plans",

            command=self.show_plans

        ).grid(

            row=0,

            column=2,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Project Summary",

            command=self.show_summary

        ).grid(

            row=0,

            column=3,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Clear",

            command=self.clear_fields

        ).grid(

            row=0,

            column=4,

            padx=5

        )

        # =================================================
        # TABLE
        # =================================================

        columns = (

            "Plan ID",

            "Plan Name",

            "Ministry",

            "Budget",

            "Status",

            "Beneficiaries"

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

                width=220

            )

        self.table.pack(

            fill=tk.BOTH,

            expand=True,

            padx=10,

            pady=10

        )

        self.show_plans()

    # =================================================
    # ADD PLAN
    # =================================================

    def add_plan(self):

        try:

            plan_id = (

                self.plan_id_entry.get()

            )

            plan_name = (

                self.plan_name_entry.get()

            )

            ministry = (

                self.ministry_entry.get()

            )

            budget = float(

                self.budget_entry.get()

            )

            beneficiaries = int(

                self.beneficiaries_entry.get()

            )

            status = (

                self.status_combo.get()

            )

            self.manager.add_plan(

                plan_id,

                plan_name,

                ministry,

                budget,

                status,

                beneficiaries

            )

            self.manager.save_data()

            self.show_plans()

            messagebox.showinfo(

                "Success",

                "New plan added successfully."

            )

            self.clear_fields()

        except ValueError as error:

            messagebox.showerror(

                "Input Error",

                str(error)

            )

    # =================================================
    # UPDATE STATUS
    # =================================================

    def update_status(self):

        try:

            plan_id = (

                self.plan_id_entry.get()

            )

            new_status = (

                self.status_combo.get()

            )

            self.manager.update_status(

                plan_id,

                new_status

            )

            self.manager.save_data()

            self.show_plans()

            messagebox.showinfo(

                "Success",

                "Plan status updated successfully."

            )

        except ValueError as error:

            messagebox.showerror(

                "Update Error",

                str(error)

            )

    # =================================================
    # SHOW PLANS
    # =================================================

    def show_plans(self):

        for item in (

            self.table.get_children()

        ):

            self.table.delete(item)

        for plan in (

            self.manager.plans

        ):

            self.table.insert(

                "",

                tk.END,

                values=(

                    plan["plan_id"],

                    plan["plan_name"],

                    plan["ministry"],

                    f"₹{plan['budget']:,.2f}",

                    plan["status"],

                    f"{plan['beneficiaries']:,}"

                )

            )

    # =================================================
    # SHOW SUMMARY
    # =================================================

    def show_summary(self):

        total_plans = (

            self.manager.get_total_plans()

        )

        completed_plans = (

            self.manager.get_completed_plans()

        )

        beneficiaries = (

            self.manager.get_total_beneficiaries()

        )

        budget = (

            self.manager.budget["total_budget"]

        )

        ministries = len(

            self.manager.ministries

        )

        messagebox.showinfo(

            "Project Summary",

            (

                "PRIME MINISTER PLANS 2026\n\n"

                f"Total Plans: {total_plans}\n"

                f"Completed Plans: "

                f"{completed_plans}\n"

                f"Total Ministries: "

                f"{ministries}\n"

                f"Total Beneficiaries: "

                f"{beneficiaries:,}\n"

                f"Total Budget: "

                f"₹{budget:,.2f}"

            )

        )

    # =================================================
    # CLEAR FIELDS
    # =================================================

    def clear_fields(self):

        self.plan_id_entry.delete(

            0,

            tk.END

        )

        self.plan_name_entry.delete(

            0,

            tk.END

        )

        self.ministry_entry.delete(

            0,

            tk.END

        )

        self.budget_entry.delete(

            0,

            tk.END

        )

        self.beneficiaries_entry.delete(

            0,

            tk.END

        )

        self.status_combo.set("")


# =====================================================
# MAIN FUNCTION
# =====================================================

def main():

    root = tk.Tk()

    app = PlansApp(root)

    root.mainloop()


# =====================================================
# PROGRAM START
# =====================================================

if __name__ == "__main__":

    main()