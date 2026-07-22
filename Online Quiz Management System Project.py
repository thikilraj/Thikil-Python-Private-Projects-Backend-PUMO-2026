# ============================================================
# ONLINE QUIZ MANAGEMENT SYSTEM
# ============================================================

import tkinter as tk
from tkinter import messagebox


# ============================================================
# 1. BASIC DATA TYPES
# ============================================================

quiz_name = "Python Programming Quiz"  # String
total_questions = 5                     # Integer
pass_percentage = 50.0                  # Float
quiz_active = True                      # Boolean


# ============================================================
# 2. TUPLE
# ============================================================

QUIZ_CATEGORIES = (
    "Python",
    "Programming",
    "OOP",
    "Data Structures"
)


# ============================================================
# 3. LIST
# ============================================================

participants = []


# ============================================================
# 4. SET
# ============================================================

unique_participants = set()


# ============================================================
# 5. DICTIONARY
# ============================================================

quiz_statistics = {
    "total_participants": 0,
    "total_score": 0
}


# ============================================================
# 6. OOP - PARTICIPANT CLASS
# ============================================================

class Participant:
    """
    Participant class for managing quiz participants.
    """

    quiz = "Python Programming Quiz"

    def __init__(
        self,
        participant_id,
        name,
        score
    ):

        self.participant_id = participant_id
        self.name = name
        self.score = score

    def calculate_result(self):

        if self.score >= pass_percentage:

            return "PASS"

        return "FAIL"

    def display_participant(self):

        return (
            f"Participant ID: "
            f"{self.participant_id}\n"
            f"Name: {self.name}\n"
            f"Score: {self.score}%\n"
            f"Result: "
            f"{self.calculate_result()}\n"
        )

    def __str__(self):

        return (
            f"{self.participant_id} - "
            f"{self.name}"
        )


# ============================================================
# 7. BUILT-IN CLASS ATTRIBUTES
# ============================================================

print(
    "Class Name:",
    Participant.__name__
)

print(
    "Class Module:",
    Participant.__module__
)

print(
    "Class Documentation:",
    Participant.__doc__
)


# ============================================================
# 8. FUNCTION: ADD PARTICIPANT
# ============================================================

def add_participant(
    participant_id,
    name,
    score
):

    try:

        if participant_id == "":

            raise ValueError(
                "Participant ID cannot be empty."
            )

        if name == "":

            raise ValueError(
                "Participant name cannot be empty."
            )

        # Convert score to integer
        score = int(score)

        if score < 0 or score > 100:

            raise ValueError(
                "Score must be between 0 and 100."
            )

        # Check duplicate participant ID
        for participant in participants:

            if (
                participant.participant_id
                == participant_id
            ):

                raise ValueError(
                    "Participant ID already exists."
                )

        # Create object
        participant = Participant(
            participant_id,
            name,
            score
        )

        # Add object to list
        participants.append(
            participant
        )

        # Add name to set
        unique_participants.add(
            name
        )

        # Update dictionary
        quiz_statistics[
            "total_participants"
        ] += 1

        quiz_statistics[
            "total_score"
        ] += score

        return True, (
            "Participant added successfully."
        )

    except ValueError as error:

        return False, str(error)


# ============================================================
# 9. FUNCTION: VIEW ALL PARTICIPANTS
# ============================================================

def view_all_participants():

    if len(participants) == 0:

        return "No participants found."

    output = ""

    # RANGE
    for index in range(
        len(participants)
    ):

        output += (
            f"\nParticipant "
            f"{index + 1}\n"
        )

        output += "=" * 40

        output += "\n"

        output += (
            participants[index]
            .display_participant()
        )

    return output


# ============================================================
# 10. FUNCTION: SEARCH PARTICIPANT
# ============================================================

def search_participant(
    participant_id
):

    for participant in participants:

        if (
            participant.participant_id
            == participant_id
        ):

            return (
                participant
                .display_participant()
            )

    return "Participant not found."


# ============================================================
# 11. FUNCTION: DELETE PARTICIPANT
# ============================================================

def delete_participant(
    participant_id
):

    for participant in participants:

        if (
            participant.participant_id
            == participant_id
        ):

            quiz_statistics[
                "total_participants"
            ] -= 1

            quiz_statistics[
                "total_score"
            ] -= participant.score

            participants.remove(
                participant
            )

            return (
                "Participant deleted successfully."
            )

    return "Participant not found."


# ============================================================
# 12. FUNCTION: SHOW STATISTICS
# ============================================================

def show_statistics():

    total = (
        quiz_statistics[
            "total_participants"
        ]
    )

    score = (
        quiz_statistics[
            "total_score"
        ]
    )

    if total > 0:

        average = score / total

    else:

        average = 0

    return (
        f"Quiz: {quiz_name}\n"
        f"Total Participants: {total}\n"
        f"Average Score: "
        f"{average:.2f}%\n"
        f"Unique Participants: "
        f"{len(unique_participants)}"
    )


# ============================================================
# 13. TKINTER FUNCTIONS
# ============================================================

def add_participant_gui():

    participant_id = id_entry.get()

    name = name_entry.get()

    score = score_entry.get()

    success, message = add_participant(
        participant_id,
        name,
        score
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


def view_participants_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    result = (
        view_all_participants()
    )

    output_text.insert(
        tk.END,
        result
    )


def search_participant_gui():

    participant_id = search_entry.get()

    result = search_participant(
        participant_id
    )

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        result
    )


def delete_participant_gui():

    participant_id = search_entry.get()

    result = delete_participant(
        participant_id
    )

    messagebox.showinfo(
        "Delete Participant",
        result
    )

    view_participants_gui()


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

    score_entry.delete(
        0,
        tk.END
    )


# ============================================================
# 14. TKINTER WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "Online Quiz Management System"
)

root.geometry(
    "900x750"
)


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="ONLINE QUIZ MANAGEMENT SYSTEM",
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


# Participant ID

tk.Label(
    form_frame,
    text="Participant ID"
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
    text="Participant Name"
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


# Score

tk.Label(
    form_frame,
    text="Score (0-100)"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=5
)


score_entry = tk.Entry(
    form_frame,
    width=35
)

score_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)


# ============================================================
# BUTTONS
# ============================================================

add_button = tk.Button(
    root,
    text="Add Participant",
    width=25,
    command=add_participant_gui
)

add_button.pack(
    pady=5
)


view_button = tk.Button(
    root,
    text="View All Participants",
    width=25,
    command=view_participants_gui
)

view_button.pack(
    pady=5
)


statistics_button = tk.Button(
    root,
    text="Quiz Statistics",
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
    text="Participant ID"
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
    command=search_participant_gui
)

search_button.grid(
    row=0,
    column=2,
    padx=5
)


delete_button = tk.Button(
    search_frame,
    text="Delete",
    command=delete_participant_gui
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
    height=20
)

output_text.pack(
    pady=15
)


# ============================================================
# PROGRAM START
# ============================================================

root.mainloop()