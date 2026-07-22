import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


# =====================================================
# FILE NAME
# =====================================================

DATA_FILE = "election_data.json"


# =====================================================
# ELECTION MANAGEMENT CLASS
# =====================================================

class TamilNaduElection:

    # Class attributes
    election_name = "Tamil Nadu Assembly Election 2026"

    total_constituencies = 234

    def __init__(self):

        # List
        self.voters = []

        # List
        self.parties = []

        # Dictionary
        self.votes = {}

        # Set
        self.voter_ids = set()

        # Default parties
        self.load_default_parties()

    # =================================================
    # LOAD DEFAULT PARTIES
    # =================================================

    def load_default_parties(self):

        self.parties = [

            (
                "DMK",
                "Dravida Munnetra Kazhagam"
            ),

            (
                "AIADMK",
                "All India Anna Dravida Munnetra Kazhagam"
            ),

            (
                "TVK",
                "Tamilaga Vettri Kazhagam"
            ),

            (
                "BJP",
                "Bharatiya Janata Party"
            ),

            (
                "INC",
                "Indian National Congress"
            ),

            (
                "PMK",
                "Pattali Makkal Katchi"
            ),

            (
                "NTK",
                "Naam Tamilar Katchi"
            )

        ]

        for party in self.parties:

            self.votes[party[0]] = 0

    # =================================================
    # REGISTER VOTER
    # =================================================

    def register_voter(

        self,

        voter_id,

        name,

        age,

        constituency

    ):

        if voter_id == "":

            raise ValueError(

                "Voter ID cannot be empty."

            )

        if name == "":

            raise ValueError(

                "Voter name cannot be empty."

            )

        if age < 18:

            raise ValueError(

                "Voter must be 18 years or above."

            )

        if voter_id in self.voter_ids:

            raise ValueError(

                "Voter ID already registered."

            )

        voter = {

            "voter_id": voter_id,

            "name": name,

            "age": age,

            "constituency": constituency,

            "has_voted": False

        }

        self.voters.append(voter)

        self.voter_ids.add(voter_id)

    # =================================================
    # CAST VOTE
    # =================================================

    def cast_vote(

        self,

        voter_id,

        party

    ):

        if voter_id not in self.voter_ids:

            raise ValueError(

                "Voter is not registered."

            )

        selected_voter = None

        for voter in self.voters:

            if voter["voter_id"] == voter_id:

                selected_voter = voter

                break

        if selected_voter["has_voted"]:

            raise ValueError(

                "This voter has already voted."

            )

        valid_parties = set()

        for item in self.parties:

            valid_parties.add(item[0])

        if party not in valid_parties:

            raise ValueError(

                "Invalid party selected."

            )

        self.votes[party] += 1

        selected_voter["has_voted"] = True

    # =================================================
    # GET WINNER
    # =================================================

    def get_winner(self):

        if not self.votes:

            return None

        winner = max(

            self.votes,

            key=self.votes.get

        )

        return winner

    # =================================================
    # TOTAL VOTES
    # =================================================

    def total_votes(self):

        return sum(

            self.votes.values()

        )

    # =================================================
    # SAVE DATA
    # =================================================

    def save_data(self):

        data = {

            "election_name":

            self.election_name,

            "voters":

            self.voters,

            "votes":

            self.votes

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

                self.voters = data.get(

                    "voters",

                    []

                )

                self.votes.update(

                    data.get(

                        "votes",

                        {}

                    )

                )

                self.voter_ids = set(

                    voter["voter_id"]

                    for voter in self.voters

                )

        except json.JSONDecodeError:

            messagebox.showerror(

                "File Error",

                "Election data file is invalid."

            )


# =====================================================
# TKINTER GUI APPLICATION
# =====================================================

class ElectionApp:

    def __init__(self, root):

        self.root = root

        self.root.title(

            "Tamil Nadu Election 2026 Voting System"

        )

        self.root.geometry(

            "1400x850"

        )

        self.election = TamilNaduElection()

        self.election.load_data()

        # =================================================
        # TITLE
        # =================================================

        title = tk.Label(

            root,

            text=(

                "TAMIL NADU ASSEMBLY ELECTION 2026"

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

                "Educational Voting Management System"

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

        # Voter ID

        tk.Label(

            input_frame,

            text="Voter ID"

        ).grid(

            row=0,

            column=0,

            padx=5,

            pady=5

        )

        self.voter_id_entry = tk.Entry(

            input_frame,

            width=25

        )

        self.voter_id_entry.grid(

            row=0,

            column=1

        )

        # Voter Name

        tk.Label(

            input_frame,

            text="Voter Name"

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

        # Constituency

        tk.Label(

            input_frame,

            text="Constituency No."

        ).grid(

            row=1,

            column=2,

            padx=5

        )

        self.constituency_entry = tk.Entry(

            input_frame,

            width=25

        )

        self.constituency_entry.grid(

            row=1,

            column=3

        )

        # Party

        tk.Label(

            input_frame,

            text="Party"

        ).grid(

            row=2,

            column=0,

            padx=5

        )

        self.party_combo = ttk.Combobox(

            input_frame,

            values=[

                party[0]

                for party in self.election.parties

            ],

            width=22,

            state="readonly"

        )

        self.party_combo.grid(

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

            text="Register Voter",

            command=self.register_voter

        ).grid(

            row=0,

            column=0,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Cast Vote",

            command=self.cast_vote

        ).grid(

            row=0,

            column=1,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Show Results",

            command=self.show_results

        ).grid(

            row=0,

            column=2,

            padx=5

        )

        tk.Button(

            button_frame,

            text="Show Winner",

            command=self.show_winner

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
        # VOTER TABLE
        # =================================================

        columns = (

            "Voter ID",

            "Name",

            "Age",

            "Constituency",

            "Vote Status"

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

        self.show_voters()

    # =================================================
    # REGISTER VOTER
    # =================================================

    def register_voter(self):

        try:

            voter_id = (

                self.voter_id_entry.get()

            )

            name = (

                self.name_entry.get()

            )

            age = int(

                self.age_entry.get()

            )

            constituency = (

                self.constituency_entry.get()

            )

            self.election.register_voter(

                voter_id,

                name,

                age,

                constituency

            )

            self.election.save_data()

            self.show_voters()

            messagebox.showinfo(

                "Success",

                "Voter registered successfully."

            )

            self.clear_fields()

        except ValueError as error:

            messagebox.showerror(

                "Registration Error",

                str(error)

            )

    # =================================================
    # CAST VOTE
    # =================================================

    def cast_vote(self):

        try:

            voter_id = (

                self.voter_id_entry.get()

            )

            party = (

                self.party_combo.get()

            )

            self.election.cast_vote(

                voter_id,

                party

            )

            self.election.save_data()

            self.show_voters()

            messagebox.showinfo(

                "Vote Recorded",

                (

                    "Your vote has been "

                    "recorded successfully."

                )

            )

            self.clear_fields()

        except ValueError as error:

            messagebox.showerror(

                "Voting Error",

                str(error)

            )

    # =================================================
    # SHOW VOTERS
    # =================================================

    def show_voters(self):

        for item in (

            self.table.get_children()

        ):

            self.table.delete(item)

        for voter in (

            self.election.voters

        ):

            status = (

                "VOTED"

                if voter["has_voted"]

                else

                "NOT VOTED"

            )

            self.table.insert(

                "",

                tk.END,

                values=(

                    voter["voter_id"],

                    voter["name"],

                    voter["age"],

                    voter["constituency"],

                    status

                )

            )

    # =================================================
    # SHOW RESULTS
    # =================================================

    def show_results(self):

        output = (

            "TAMIL NADU ELECTION 2026 RESULTS\n\n"

        )

        for party, votes in (

            self.election.votes.items()

        ):

            output += (

                f"{party}: "

                f"{votes} votes\n"

            )

        output += (

            f"\nTotal Votes: "

            f"{self.election.total_votes()}"

        )

        messagebox.showinfo(

            "Election Results",

            output

        )

    # =================================================
    # SHOW WINNER
    # =================================================

    def show_winner(self):

        winner = (

            self.election.get_winner()

        )

        if (

            self.election.total_votes()

            == 0

        ):

            messagebox.showinfo(

                "Winner",

                "No votes have been recorded yet."

            )

            return

        messagebox.showinfo(

            "Election Winner",

            (

                f"Leading Party: {winner}\n\n"

                f"Votes: "

                f"{self.election.votes[winner]}"

            )

        )

    # =================================================
    # CLEAR INPUT FIELDS
    # =================================================

    def clear_fields(self):

        self.voter_id_entry.delete(

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

        self.constituency_entry.delete(

            0,

            tk.END

        )

        self.party_combo.set("")


# =====================================================
# MAIN FUNCTION
# =====================================================

def main():

    root = tk.Tk()

    app = ElectionApp(root)

    root.mainloop()


# =====================================================
# PROGRAM START
# =====================================================

if __name__ == "__main__":

    main()