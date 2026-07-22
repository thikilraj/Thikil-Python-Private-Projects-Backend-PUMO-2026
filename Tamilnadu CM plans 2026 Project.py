import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


DATA_FILE = "tamilnadu_plans.json"


class TamilNaduCMPlans:

    # Class attributes
    project_title = "Tamil Nadu Chief Minister Development Plans 2026"
    state = "Tamil Nadu"

    def __init__(self):

        # List
        self.plans = []

        # Set
        self.departments = set()

        # Dictionary
        self.finance = {
            "total_budget": 0
        }

        # Tuple
        self.status_options = (
            "Planned",
            "Ongoing",
            "Completed"
        )

        self.load_default_plans()

    # -----------------------------------------
    # DEFAULT PLANS
    # -----------------------------------------

    def load_default_plans(self):

        default_plans = [

            {
                "plan_id": "TN2026-001",
                "plan_name": "Health and Welfare Development",
                "department": "Health",
                "budget": 100000000,
                "status": "Ongoing",
                "beneficiaries": 1000000
            },

            {
                "plan_id": "TN2026-002",
                "plan_name": "Youth Skill Development",
                "department": "Skill Development",
                "budget": 75000000,
                "status": "Planned",
                "beneficiaries": 500000
            },

            {
                "plan_id": "TN2026-003",
                "plan_name": "Rural Infrastructure Development",
                "department": "Rural Development",
                "budget": 125000000,
                "status": "Ongoing",
                "beneficiaries": 750000
            },

            {
                "plan_id": "TN2026-004",
                "plan_name": "Green Tamil Nadu Initiative",
                "department": "Environment",
                "budget": 90000000,
                "status": "Planned",
                "beneficiaries": 600000
            }

        ]

        for plan in default_plans:

            self.plans.append(plan)

            self.departments.add(
                plan["department"]
            )

            self.finance["total_budget"] += (
                plan["budget"]
            )

    # -----------------------------------------
    # ADD PLAN
    # -----------------------------------------

    def add_plan(
        self,
        plan_id,
        plan_name,
        department,
        budget,
        status,
        beneficiaries
    ):

        if not plan_id:
            raise ValueError(
                "Plan ID is required."
            )

        if not plan_name:
            raise ValueError(
                "Plan name is required."
            )

        if not department:
            raise ValueError(
                "Department is required."
            )

        if budget <= 0:
            raise ValueError(
                "Budget must be greater than zero."
            )

        if beneficiaries < 0:
            raise ValueError(
                "Beneficiaries cannot be negative."
            )

        for plan in self.plans:

            if plan["plan_id"] == plan_id:

                raise ValueError(
                    "Plan ID already exists."
                )

        new_plan = {

            "plan_id": plan_id,
            "plan_name": plan_name,
            "department": department,
            "budget": budget,
            "status": status,
            "beneficiaries": beneficiaries

        }

        self.plans.append(new_plan)

        self.departments.add(department)

        self.finance["total_budget"] += budget

    # -----------------------------------------
    # UPDATE STATUS
    # -----------------------------------------

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

    # -----------------------------------------
    # SEARCH PLAN
    # -----------------------------------------

    def search_plan(self, plan_id):

        for plan in self.plans:

            if plan["plan_id"] == plan_id:

                return plan

        return None

    # -----------------------------------------
    # TOTAL PLANS
    # -----------------------------------------

    def total_plans(self):

        return len(self.plans)

    # -----------------------------------------
    # COMPLETED PLANS
    # -----------------------------------------

    def completed_plans(self):

        count = 0

        for plan in self.plans:

            if plan["status"] == "Completed":

                count += 1

        return count

    # -----------------------------------------
    # TOTAL BENEFICIARIES
    # -----------------------------------------

    def total_beneficiaries(self):

        total = 0

        for plan in self.plans:

            total += plan["beneficiaries"]

        return total

    # -----------------------------------------
    # SAVE DATA
    # -----------------------------------------

    def save_data(self):

        data = {

            "project_title":
            self.project_title,

            "state":
            self.state,

            "plans":
            self.plans,

            "finance":
            self.finance,

            "departments":
            list(self.departments)

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

    # -----------------------------------------
    # LOAD DATA
    # -----------------------------------------

    def load_data(self):

        if not os.path.exists(DATA_FILE):

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

                self.finance = data.get(
                    "finance",
                    self.finance
                )

                self.departments = set(
                    data.get(
                        "departments",
                        []
                    )
                )

        except json.JSONDecodeError:

            messagebox.showerror(
                "Error",
                "Invalid JSON file."
            )


# ==================================================
# TKINTER GUI
# ==================================================

class TamilNaduCMApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Tamil Nadu Chief Minister Plans 2026"
        )

        self.root.geometry(
            "1450x850"
        )

        self.manager = TamilNaduCMPlans()

        self.manager.load_data()

        # ------------------------------------------
        # TITLE
        # ------------------------------------------

        title = tk.Label(

            root,

            text=(
                "TAMIL NADU CHIEF MINISTER "
                "DEVELOPMENT PLANS 2026"
            ),

            font=(
                "Arial",
                24,
                "bold"
            )

        )

        title.pack(pady=15)

        subtitle = tk.Label(

            root,

            text=(
                "Development Plan and Budget "
                "Management System"
            ),

            font=(
                "Arial",
                12
            )

        )

        subtitle.pack()

        # ------------------------------------------
        # INPUT FRAME
        # ------------------------------------------

        input_frame = tk.Frame(root)

        input_frame.pack(pady=20)

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
            width=30
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

        # Department

        tk.Label(
            input_frame,
            text="Department"
        ).grid(
            row=1,
            column=0,
            padx=5
        )

        self.department_entry = tk.Entry(
            input_frame,
            width=30
        )

        self.department_entry.grid(
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
            width=30
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

            values=self.manager.status_options,

            state="readonly",

            width=27

        )

        self.status_combo.grid(
            row=2,
            column=3
        )

        # ------------------------------------------
        # BUTTONS
        # ------------------------------------------

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

        # ------------------------------------------
        # TABLE
        # ------------------------------------------

        columns = (

            "Plan ID",
            "Plan Name",
            "Department",
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
                width=210
            )

        self.table.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10
        )

        self.show_plans()

    # ------------------------------------------
    # ADD PLAN
    # ------------------------------------------

    def add_plan(self):

        try:

            plan_id = (
                self.plan_id_entry.get()
            )

            plan_name = (
                self.plan_name_entry.get()
            )

            department = (
                self.department_entry.get()
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
                department,
                budget,
                status,
                beneficiaries

            )

            self.manager.save_data()

            self.show_plans()

            messagebox.showinfo(
                "Success",
                "Plan added successfully."
            )

            self.clear_fields()

        except ValueError as error:

            messagebox.showerror(
                "Input Error",
                str(error)
            )

    # ------------------------------------------
    # UPDATE STATUS
    # ------------------------------------------

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
                "Plan status updated."
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ------------------------------------------
    # SHOW PLANS
    # ------------------------------------------

    def show_plans(self):

        for item in self.table.get_children():

            self.table.delete(item)

        for plan in self.manager.plans:

            self.table.insert(

                "",

                tk.END,

                values=(

                    plan["plan_id"],

                    plan["plan_name"],

                    plan["department"],

                    f"₹{plan['budget']:,.2f}",

                    plan["status"],

                    f"{plan['beneficiaries']:,}"

                )

            )

    # ------------------------------------------
    # SUMMARY
    # ------------------------------------------

    def show_summary(self):

        total_plans = (
            self.manager.total_plans()
        )

        completed = (
            self.manager.completed_plans()
        )

        beneficiaries = (
            self.manager.total_beneficiaries()
        )

        budget = (
            self.manager.finance[
                "total_budget"
            ]
        )

        departments = len(
            self.manager.departments
        )

        messagebox.showinfo(

            "Tamil Nadu Project Summary",

            (

                "TAMIL NADU DEVELOPMENT PLANS 2026\n\n"

                f"Total Plans: {total_plans}\n"

                f"Completed Plans: {completed}\n"

                f"Departments: {departments}\n"

                f"Beneficiaries: {beneficiaries:,}\n"

                f"Total Budget: ₹{budget:,.2f}"

            )

        )

    # ------------------------------------------
    # CLEAR FIELDS
    # ------------------------------------------

    def clear_fields(self):

        self.plan_id_entry.delete(
            0,
            tk.END
        )

        self.plan_name_entry.delete(
            0,
            tk.END
        )

        self.department_entry.delete(
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


# ==================================================
# MAIN FUNCTION
# ==================================================

def main():

    root = tk.Tk()

    app = TamilNaduCMApp(root)

    root.mainloop()


if __name__ == "__main__":

    main()