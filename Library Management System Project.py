# ==========================================================
# LIBRARY MANAGEMENT SYSTEM
# ==========================================================

import tkinter as tk
from tkinter import messagebox


# ==========================================================
# BASIC DATA TYPES
# ==========================================================

library_name = "City Central Library"  # String
library_capacity = 1000                # Integer
library_rating = 4.5                   # Float
library_open = True                    # Boolean


# ==========================================================
# TUPLE
# ==========================================================

BOOK_CATEGORIES = (
    "Programming",
    "Database",
    "Networking",
    "Science",
    "Novel"
)


# ==========================================================
# LIST
# ==========================================================

books = []


# ==========================================================
# DICTIONARY
# ==========================================================

library_statistics = {
    "total_books": 0,
    "available_books": 0,
    "borrowed_books": 0
}


# ==========================================================
# SET
# ==========================================================

authors = set()


# ==========================================================
# OOP - BOOK CLASS
# ==========================================================

class Book:
    """
    Book class for the Library Management System.
    """

    library = "City Central Library"

    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.available = True

    def display_book(self):

        status = "Available" if self.available else "Borrowed"

        return (
            f"Book ID: {self.book_id}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Category: {self.category}\n"
            f"Status: {status}\n"
        )

    def __str__(self):

        return f"{self.book_id} - {self.title}"


# ==========================================================
# BUILT-IN CLASS ATTRIBUTES
# ==========================================================

print("Class Name:", Book.__name__)
print("Class Module:", Book.__module__)
print("Class Documentation:", Book.__doc__)


# ==========================================================
# FUNCTION: ADD BOOK
# ==========================================================

def add_book(book_id, title, author, category):

    try:

        if book_id == "":
            raise ValueError("Book ID cannot be empty.")

        if title == "":
            raise ValueError("Book title cannot be empty.")

        if author == "":
            raise ValueError("Author name cannot be empty.")

        # Check duplicate book ID
        for book in books:

            if book.book_id == book_id:

                raise ValueError(
                    "Book ID already exists."
                )

        # Create Book Object
        book = Book(
            book_id,
            title,
            author,
            category
        )

        # Add object to list
        books.append(book)

        # Add author to set
        authors.add(author)

        # Update dictionary
        library_statistics["total_books"] += 1

        library_statistics["available_books"] += 1

        return True, "Book added successfully."

    except ValueError as error:

        return False, str(error)


# ==========================================================
# FUNCTION: VIEW ALL BOOKS
# ==========================================================

def view_all_books():

    if len(books) == 0:

        return "No books available."

    output = ""

    # RANGE
    for index in range(len(books)):

        output += f"\nBook {index + 1}\n"
        output += "=" * 40
        output += "\n"
        output += books[index].display_book()

    return output


# ==========================================================
# FUNCTION: SEARCH BOOK
# ==========================================================

def search_book(book_id):

    for book in books:

        if book.book_id == book_id:

            return book.display_book()

    return "Book not found."


# ==========================================================
# FUNCTION: BORROW BOOK
# ==========================================================

def borrow_book(book_id):

    try:

        for book in books:

            if book.book_id == book_id:

                if not book.available:

                    raise ValueError(
                        "Book is already borrowed."
                    )

                book.available = False

                library_statistics["available_books"] -= 1

                library_statistics["borrowed_books"] += 1

                return "Book borrowed successfully."

        return "Book not found."

    except ValueError as error:

        return str(error)


# ==========================================================
# FUNCTION: RETURN BOOK
# ==========================================================

def return_book(book_id):

    try:

        for book in books:

            if book.book_id == book_id:

                if book.available:

                    raise ValueError(
                        "Book is already available."
                    )

                book.available = True

                library_statistics["available_books"] += 1

                library_statistics["borrowed_books"] -= 1

                return "Book returned successfully."

        return "Book not found."

    except ValueError as error:

        return str(error)


# ==========================================================
# FUNCTION: SHOW STATISTICS
# ==========================================================

def show_statistics():

    return (
        f"Library: {library_name}\n"
        f"Total Books: "
        f"{library_statistics['total_books']}\n"
        f"Available Books: "
        f"{library_statistics['available_books']}\n"
        f"Borrowed Books: "
        f"{library_statistics['borrowed_books']}\n"
        f"Unique Authors: "
        f"{len(authors)}"
    )


# ==========================================================
# TKINTER FUNCTIONS
# ==========================================================

def add_book_gui():

    book_id = id_entry.get()
    title = title_entry.get()
    author = author_entry.get()
    category = category_entry.get()

    success, message = add_book(
        book_id,
        title,
        author,
        category
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


def view_books_gui():

    output_text.delete(
        "1.0",
        tk.END
    )

    output = view_all_books()

    output_text.insert(
        tk.END,
        output
    )


def search_book_gui():

    book_id = search_entry.get()

    result = search_book(book_id)

    output_text.delete(
        "1.0",
        tk.END
    )

    output_text.insert(
        tk.END,
        result
    )


def borrow_book_gui():

    book_id = search_entry.get()

    result = borrow_book(book_id)

    messagebox.showinfo(
        "Borrow Book",
        result
    )

    view_books_gui()


def return_book_gui():

    book_id = search_entry.get()

    result = return_book(book_id)

    messagebox.showinfo(
        "Return Book",
        result
    )

    view_books_gui()


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

    title_entry.delete(
        0,
        tk.END
    )

    author_entry.delete(
        0,
        tk.END
    )

    category_entry.delete(
        0,
        tk.END
    )


# ==========================================================
# TKINTER WINDOW
# ==========================================================

root = tk.Tk()

root.title(
    "Library Management System"
)

root.geometry(
    "800x750"
)


# ==========================================================
# TITLE
# ==========================================================

title_label = tk.Label(
    root,
    text="LIBRARY MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold")
)

title_label.pack(
    pady=15
)


# ==========================================================
# FORM
# ==========================================================

form_frame = tk.Frame(root)

form_frame.pack(
    pady=10
)


# Book ID

tk.Label(
    form_frame,
    text="Book ID"
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


# Title

tk.Label(
    form_frame,
    text="Book Title"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


title_entry = tk.Entry(
    form_frame,
    width=35
)

title_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


# Author

tk.Label(
    form_frame,
    text="Author"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=5
)


author_entry = tk.Entry(
    form_frame,
    width=35
)

author_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)


# Category

tk.Label(
    form_frame,
    text="Category"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=5
)


category_entry = tk.Entry(
    form_frame,
    width=35
)

category_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=5
)


# ==========================================================
# BUTTONS
# ==========================================================

add_button = tk.Button(
    root,
    text="Add Book",
    width=25,
    command=add_book_gui
)

add_button.pack(
    pady=5
)


view_button = tk.Button(
    root,
    text="View All Books",
    width=25,
    command=view_books_gui
)

view_button.pack(
    pady=5
)


statistics_button = tk.Button(
    root,
    text="Show Statistics",
    width=25,
    command=statistics_gui
)

statistics_button.pack(
    pady=5
)


# ==========================================================
# SEARCH FRAME
# ==========================================================

search_frame = tk.Frame(root)

search_frame.pack(
    pady=15
)


tk.Label(
    search_frame,
    text="Book ID"
).grid(
    row=0,
    column=0,
    padx=5
)


search_entry = tk.Entry(
    search_frame,
    width=25
)

search_entry.grid(
    row=0,
    column=1,
    padx=5
)


search_button = tk.Button(
    search_frame,
    text="Search",
    command=search_book_gui
)

search_button.grid(
    row=0,
    column=2,
    padx=5
)


borrow_button = tk.Button(
    search_frame,
    text="Borrow",
    command=borrow_book_gui
)

borrow_button.grid(
    row=0,
    column=3,
    padx=5
)


return_button = tk.Button(
    search_frame,
    text="Return",
    command=return_book_gui
)

return_button.grid(
    row=0,
    column=4,
    padx=5
)


# ==========================================================
# OUTPUT AREA
# ==========================================================

output_text = tk.Text(
    root,
    width=90,
    height=20
)

output_text.pack(
    pady=15
)


# ==========================================================
# PROGRAM START
# ==========================================================

root.mainloop()