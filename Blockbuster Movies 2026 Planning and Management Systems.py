import tkinter as tk
from tkinter import messagebox


# ============================================================
# 1. INTRODUCTION TO PYTHON
# ============================================================

project_name = "Blockbuster Movies 2026 Management System"

planning_year = 2026

currency = "₹"


# ============================================================
# 2. IDENTIFIERS AND VARIABLES
# ============================================================

movies = []

movie_genres = set()

total_movie_budget = 0.0


# ============================================================
# 3. TUPLES
# ============================================================

MOVIE_GENRES = (
    "Action",
    "Comedy",
    "Drama",
    "Science Fiction",
    "Thriller",
    "Animation",
    "Fantasy"
)


MOVIE_STATUS = (
    "Planned",
    "Pre-Production",
    "Production",
    "Post-Production",
    "Released"
)


# ============================================================
# 4. DICTIONARY
# ============================================================

movie_statistics = {

    "total_movies": 0,

    "total_budget": 0.0,

    "total_rating": 0.0,

    "released_movies": 0

}


# ============================================================
# 5. OOP - MOVIE CLASS
# ============================================================

class Movie:

    """
    Movie class stores blockbuster movie information.
    """

    production_company = "Blockbuster Studios"

    def __init__(
        self,
        movie_id,
        movie_name,
        genre,
        language,
        lead_actor,
        budget,
        release_date,
        status,
        rating
    ):

        self.movie_id = movie_id

        self.movie_name = movie_name

        self.genre = genre

        self.language = language

        self.lead_actor = lead_actor

        self.budget = budget

        self.release_date = release_date

        self.status = status

        self.rating = rating


    def display_movie(self):

        return (

            f"Movie ID: {self.movie_id}\n"

            f"Movie Name: {self.movie_name}\n"

            f"Genre: {self.genre}\n"

            f"Language: {self.language}\n"

            f"Lead Actor: {self.lead_actor}\n"

            f"Production Budget: "
            f"₹{self.budget:.2f}\n"

            f"Release Date: "
            f"{self.release_date}\n"

            f"Production Status: "
            f"{self.status}\n"

            f"Audience Rating: "
            f"{self.rating}/10\n"

        )


    def __str__(self):

        return (

            f"{self.movie_id} - "

            f"{self.movie_name}"

        )


# ============================================================
# 6. BUILT-IN CLASS ATTRIBUTES
# ============================================================

print(

    "Class Name:",

    Movie.__name__

)


print(

    "Class Module:",

    Movie.__module__

)


print(

    "Class Documentation:",

    Movie.__doc__

)


# ============================================================
# 7. SET TOTAL BUDGET
# ============================================================

def set_total_budget(amount):

    global total_movie_budget

    try:

        amount = float(amount)


        if amount <= 0:

            raise ValueError(

                "Budget must be greater than zero."

            )


        total_movie_budget = amount


        return (

            True,

            "Total movie budget saved successfully."

        )


    except ValueError as error:

        return False, str(error)


# ============================================================
# 8. ADD MOVIE
# ============================================================

def add_movie(

    movie_id,

    movie_name,

    genre,

    language,

    lead_actor,

    budget,

    release_date,

    status,

    rating

):

    try:

        # Empty value validation

        if movie_id == "":

            raise ValueError(

                "Movie ID cannot be empty."

            )


        if movie_name == "":

            raise ValueError(

                "Movie name cannot be empty."

            )


        if language == "":

            raise ValueError(

                "Language cannot be empty."

            )


        if lead_actor == "":

            raise ValueError(

                "Lead actor cannot be empty."

            )


        if release_date == "":

            raise ValueError(

                "Release date cannot be empty."

            )


        # Validate genre

        if genre not in MOVIE_GENRES:

            raise ValueError(

                "Invalid movie genre."

            )


        # Validate status

        if status not in MOVIE_STATUS:

            raise ValueError(

                "Invalid movie status."

            )


        # Convert values

        budget = float(budget)

        rating = float(rating)


        # Validate numbers

        if budget <= 0:

            raise ValueError(

                "Budget must be greater than zero."

            )


        if rating < 0 or rating > 10:

            raise ValueError(

                "Rating must be between 0 and 10."

            )


        # Check duplicate movie ID

        for movie in movies:

            if movie.movie_id == movie_id:

                raise ValueError(

                    "Movie ID already exists."

                )


        # Create Movie Object

        movie = Movie(

            movie_id,

            movie_name,

            genre,

            language,

            lead_actor,

            budget,

            release_date,

            status,

            rating

        )


        # Add to LIST

        movies.append(movie)


        # Add genre to SET

        movie_genres.add(genre)


        # Update DICTIONARY

        movie_statistics[

            "total_movies"

        ] += 1


        movie_statistics[

            "total_budget"

        ] += budget


        movie_statistics[

            "total_rating"

        ] += rating


        if status == "Released":

            movie_statistics[

                "released_movies"

            ] += 1


        return (

            True,

            "Movie added successfully."

        )


    except ValueError as error:

        return False, str(error)


# ============================================================
# 9. VIEW ALL MOVIES
# ============================================================

def view_movies():

    if len(movies) == 0:

        return (

            "No movies found."

        )


    output = ""


    for index in range(

        len(movies)

    ):


        output += (

            f"\nMovie "

            f"{index + 1}\n"

        )


        output += (

            "=" * 60

        )


        output += "\n"


        output += (

            movies[index]

            .display_movie()

        )


    return output


# ============================================================
# 10. SEARCH MOVIE
# ============================================================

def search_movie(movie_id):

    for movie in movies:

        if movie.movie_id == movie_id:

            return (

                movie.display_movie()

            )


    return (

        "Movie not found."

    )


# ============================================================
# 11. DELETE MOVIE
# ============================================================

def delete_movie(movie_id):

    for movie in movies:

        if movie.movie_id == movie_id:

            movies.remove(movie)


            movie_statistics[

                "total_movies"

            ] -= 1


            movie_statistics[

                "total_budget"

            ] -= movie.budget


            movie_statistics[

                "total_rating"

            ] -= movie.rating


            if movie.status == "Released":

                movie_statistics[

                    "released_movies"

                ] -= 1


            return (

                "Movie deleted successfully."

            )


    return (

        "Movie not found."

    )


# ============================================================
# 12. RELEASE PLAN REPORT
# ============================================================

def release_plan_report():

    if len(movies) == 0:

        return (

            "No movie release plans available."

        )


    output = ""


    for movie in movies:


        output += (

            f"Movie: "

            f"{movie.movie_name}\n"

        )


        output += (

            f"Genre: "

            f"{movie.genre}\n"

        )


        output += (

            f"Release Date: "

            f"{movie.release_date}\n"

        )


        output += (

            f"Status: "

            f"{movie.status}\n"

        )


        output += (

            "-" * 50

        )


        output += "\n"


    return output


# ============================================================
# 13. GENRE-WISE REPORT
# ============================================================

def genre_report():

    if len(movies) == 0:

        return (

            "No movies available."

        )


    genre_data = {}


    for movie in movies:


        genre = movie.genre


        if genre not in genre_data:

            genre_data[genre] = 0


        genre_data[genre] += 1


    output = ""


    for genre in genre_data:


        output += (

            f"{genre}: "

            f"{genre_data[genre]} movie(s)\n"

        )


    return output


# ============================================================
# 14. LANGUAGE-WISE REPORT
# ============================================================

def language_report():

    if len(movies) == 0:

        return (

            "No movies available."

        )


    language_data = {}


    for movie in movies:


        language = movie.language


        if language not in language_data:

            language_data[language] = 0


        language_data[language] += 1


    output = ""


    for language in language_data:


        output += (

            f"{language}: "

            f"{language_data[language]} movie(s)\n"

        )


    return output


# ============================================================
# 15. MOVIE STATISTICS
# ============================================================

def show_statistics():

    total_movies = (

        movie_statistics[

            "total_movies"

        ]

    )


    if total_movies > 0:

        average_rating = (

            movie_statistics[

                "total_rating"

            ]

            / total_movies

        )


    else:

        average_rating = 0


    return (

        f"Planning Year: "

        f"{planning_year}\n"

        f"Total Movies: "

        f"{total_movies}\n"

        f"Total Production Budget: ₹"

        f"{movie_statistics['total_budget']:.2f}\n"

        f"Released Movies: "

        f"{movie_statistics['released_movies']}\n"

        f"Average Audience Rating: "

        f"{average_rating:.2f}/10\n"

        f"Total Genres: "

        f"{len(movie_genres)}"

    )


# ============================================================
# 16. TKINTER FUNCTIONS
# ============================================================

def set_budget_gui():

    amount = budget_entry.get()


    success, message = (

        set_total_budget(

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


def add_movie_gui():

    movie_id = movie_id_entry.get()

    movie_name = movie_name_entry.get()

    genre = genre_entry.get()

    language = language_entry.get()

    lead_actor = actor_entry.get()

    budget = budget_entry_movie.get()

    release_date = release_date_entry.get()

    status = status_entry.get()

    rating = rating_entry.get()


    success, message = add_movie(

        movie_id,

        movie_name,

        genre,

        language,

        lead_actor,

        budget,

        release_date,

        status,

        rating

    )


    if success:

        messagebox.showinfo(

            "Success",

            message

        )


        clear_movie_fields()


    else:

        messagebox.showerror(

            "Error",

            message

        )


def view_movies_gui():

    output_text.delete(

        "1.0",

        tk.END

    )


    output_text.insert(

        tk.END,

        view_movies()

    )


def search_movie_gui():

    movie_id = search_movie_entry.get()


    result = search_movie(

        movie_id

    )


    output_text.delete(

        "1.0",

        tk.END

    )


    output_text.insert(

        tk.END,

        result

    )


def delete_movie_gui():

    movie_id = search_movie_entry.get()


    result = delete_movie(

        movie_id

    )


    messagebox.showinfo(

        "Delete Movie",

        result

    )


    view_movies_gui()


def release_plan_gui():

    output_text.delete(

        "1.0",

        tk.END

    )


    output_text.insert(

        tk.END,

        release_plan_report()

    )


def genre_report_gui():

    output_text.delete(

        "1.0",

        tk.END

    )


    output_text.insert(

        tk.END,

        genre_report()

    )


def language_report_gui():

    output_text.delete(

        "1.0",

        tk.END

    )


    output_text.insert(

        tk.END,

        language_report()

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


def clear_movie_fields():

    movie_id_entry.delete(

        0,

        tk.END

    )


    movie_name_entry.delete(

        0,

        tk.END

    )


    genre_entry.delete(

        0,

        tk.END

    )


    language_entry.delete(

        0,

        tk.END

    )


    actor_entry.delete(

        0,

        tk.END

    )


    budget_entry_movie.delete(

        0,

        tk.END

    )


    release_date_entry.delete(

        0,

        tk.END

    )


    status_entry.delete(

        0,

        tk.END

    )


    rating_entry.delete(

        0,

        tk.END

    )


# ============================================================
# 17. TKINTER WINDOW
# ============================================================

root = tk.Tk()


root.title(

    "Blockbuster Movies 2026"

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

        "BLOCKBUSTER MOVIES 2026 "

        "MANAGEMENT SYSTEM"

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

    text="Set Total Movie Budget",

    padx=10,

    pady=10

)


budget_frame.pack(

    pady=10

)


tk.Label(

    budget_frame,

    text="Total Budget"

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
# MOVIE FRAME
# ============================================================

movie_frame = tk.LabelFrame(

    root,

    text="Add 2026 Blockbuster Movie",

    padx=10,

    pady=10

)


movie_frame.pack(

    pady=10

)


# Movie ID

tk.Label(

    movie_frame,

    text="Movie ID"

).grid(

    row=0,

    column=0,

    padx=10,

    pady=5

)


movie_id_entry = tk.Entry(

    movie_frame,

    width=35

)


movie_id_entry.grid(

    row=0,

    column=1

)


# Movie Name

tk.Label(

    movie_frame,

    text="Movie Name"

).grid(

    row=1,

    column=0,

    padx=10,

    pady=5

)


movie_name_entry = tk.Entry(

    movie_frame,

    width=35

)


movie_name_entry.grid(

    row=1,

    column=1

)


# Genre

tk.Label(

    movie_frame,

    text="Genre"

).grid(

    row=2,

    column=0,

    padx=10,

    pady=5

)


genre_entry = tk.Entry(

    movie_frame,

    width=35

)


genre_entry.grid(

    row=2,

    column=1

)


# Language

tk.Label(

    movie_frame,

    text="Language"

).grid(

    row=3,

    column=0,

    padx=10,

    pady=5

)


language_entry = tk.Entry(

    movie_frame,

    width=35

)


language_entry.grid(

    row=3,

    column=1

)


# Lead Actor

tk.Label(

    movie_frame,

    text="Lead Actor"

).grid(

    row=4,

    column=0,

    padx=10,

    pady=5

)


actor_entry = tk.Entry(

    movie_frame,

    width=35

)


actor_entry.grid(

    row=4,

    column=1

)


# Budget

tk.Label(

    movie_frame,

    text="Production Budget"

).grid(

    row=5,

    column=0,

    padx=10,

    pady=5

)


budget_entry_movie = tk.Entry(

    movie_frame,

    width=35

)


budget_entry_movie.grid(

    row=5,

    column=1

)


# Release Date

tk.Label(

    movie_frame,

    text="Release Date"

).grid(

    row=6,

    column=0,

    padx=10,

    pady=5

)


release_date_entry = tk.Entry(

    movie_frame,

    width=35

)


release_date_entry.grid(

    row=6,

    column=1

)


# Status

tk.Label(

    movie_frame,

    text="Production Status"

).grid(

    row=7,

    column=0,

    padx=10,

    pady=5

)


status_entry = tk.Entry(

    movie_frame,

    width=35

)


status_entry.grid(

    row=7,

    column=1

)


# Rating

tk.Label(

    movie_frame,

    text="Audience Rating"

).grid(

    row=8,

    column=0,

    padx=10,

    pady=5

)


rating_entry = tk.Entry(

    movie_frame,

    width=35

)


rating_entry.grid(

    row=8,

    column=1

)


# Add Button

tk.Button(

    movie_frame,

    text="Add Movie",

    command=add_movie_gui,

    width=25

).grid(

    row=9,

    column=0,

    columnspan=2,

    pady=10

)


# ============================================================
# SEARCH AND DELETE
# ============================================================

search_frame = tk.LabelFrame(

    root,

    text="Search or Delete Movie",

    padx=10,

    pady=10

)


search_frame.pack(

    pady=10

)


search_movie_entry = tk.Entry(

    search_frame,

    width=25

)


search_movie_entry.grid(

    row=0,

    column=0,

    padx=5

)


tk.Button(

    search_frame,

    text="Search",

    command=search_movie_gui

).grid(

    row=0,

    column=1,

    padx=5

)


tk.Button(

    search_frame,

    text="Delete",

    command=delete_movie_gui

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

    text="View All Movies",

    command=view_movies_gui,

    width=30

).pack(

    pady=5

)


tk.Button(

    root,

    text="Release Plan Report",

    command=release_plan_gui,

    width=30

).pack(

    pady=5

)


tk.Button(

    root,

    text="Genre-wise Report",

    command=genre_report_gui,

    width=30

).pack(

    pady=5

)


tk.Button(

    root,

    text="Language-wise Report",

    command=language_report_gui,

    width=30

).pack(

    pady=5

)


tk.Button(

    root,

    text="Show Movie Statistics",

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