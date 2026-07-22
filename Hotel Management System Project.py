import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


# =====================================================
# CONSTANTS
# =====================================================

ROOM_FILE = "rooms.json"
GUEST_FILE = "guests.json"


# =====================================================
# ROOM CLASS
# =====================================================

class Room:

    # Class attribute
    hotel_name = "Python Grand Hotel"

    def __init__(
        self,
        room_number,
        room_type,
        price
    ):

        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.available = True

    # Built-in class method
    def __str__(self):

        return (
            f"Room {self.room_number} - "
            f"{self.room_type}"
        )

    # Convert object to dictionary
    def to_dictionary(self):

        return {
            "room_number": self.room_number,
            "room_type": self.room_type,
            "price": self.price,
            "available": self.available
        }


# =====================================================
# GUEST CLASS
# =====================================================

class Guest:

    def __init__(
        self,
        guest_id,
        name,
        phone,
        room_number
    ):

        self.guest_id = guest_id
        self.name = name
        self.phone = phone
        self.room_number = room_number

    def to_dictionary(self):

        return {
            "guest_id": self.guest_id,
            "name": self.name,
            "phone": self.phone,
            "room_number": self.room_number
        }


# =====================================================
# HOTEL MANAGER CLASS
# =====================================================

class HotelManager:

    def __init__(self):

        # Lists
        self.rooms = []

        self.guests = []

    # =================================================
    # ADD ROOM
    # =================================================

    def add_room(self, room):

        for existing_room in self.rooms:

            if (
                existing_room.room_number
                == room.room_number
            ):

                raise ValueError(
                    "Room number already exists."
                )

        self.rooms.append(room)

    # =================================================
    # ADD GUEST
    # =================================================

    def add_guest(self, guest):

        for existing_guest in self.guests:

            if (
                existing_guest.guest_id
                == guest.guest_id
            ):

                raise ValueError(
                    "Guest ID already exists."
                )

        self.guests.append(guest)

    # =================================================
    # BOOK ROOM
    # =================================================

    def book_room(self, guest):

        selected_room = None

        for room in self.rooms:

            if (
                room.room_number
                == guest.room_number
            ):

                selected_room = room

        if selected_room is None:

            raise ValueError(
                "Room not found."
            )

        if not selected_room.available:

            raise ValueError(
                "Room is already booked."
            )

        selected_room.available = False

        self.add_guest(
            guest
        )

    # =================================================
    # CHECK OUT
    # =================================================

    def checkout_guest(self, guest_id):

        selected_guest = None

        for guest in self.guests:

            if guest.guest_id == guest_id:

                selected_guest = guest

        if selected_guest is None:

            raise ValueError(
                "Guest not found."
            )

        for room in self.rooms:

            if (
                room.room_number
                == selected_guest.room_number
            ):

                room.available = True

        self.guests.remove(
            selected_guest
        )

    # =================================================
    # SEARCH ROOMS
    # =================================================

    def search_rooms(self, room_type):

        result = []

        for room in self.rooms:

            if (
                room_type.lower()
                in room.room_type.lower()
            ):

                result.append(room)

        return result

    # =================================================
    # UNIQUE ROOM TYPES
    # SET CONCEPT
    # =================================================

    def get_room_types(self):

        room_types = set()

        for room in self.rooms:

            room_types.add(
                room.room_type
            )

        return room_types

    # =================================================
    # SAVE DATA
    # FILE OUTPUT
    # =================================================

    def save_data(self):

        rooms_data = []

        guests_data = []

        for room in self.rooms:

            rooms_data.append(
                room.to_dictionary()
            )

        for guest in self.guests:

            guests_data.append(
                guest.to_dictionary()
            )

        with open(
            ROOM_FILE,
            "w"
        ) as file:

            json.dump(
                rooms_data,
                file,
                indent=4
            )

        with open(
            GUEST_FILE,
            "w"
        ) as file:

            json.dump(
                guests_data,
                file,
                indent=4
            )

    # =================================================
    # LOAD DATA
    # FILE INPUT
    # =================================================

    def load_data(self):

        # Load rooms
        if os.path.exists(
            ROOM_FILE
        ):

            try:

                with open(
                    ROOM_FILE,
                    "r"
                ) as file:

                    data = json.load(file)

                    for item in data:

                        room = Room(
                            item["room_number"],
                            item["room_type"],
                            item["price"]
                        )

                        room.available = (
                            item["available"]
                        )

                        self.rooms.append(
                            room
                        )

            except json.JSONDecodeError:

                messagebox.showerror(
                    "Error",
                    "Invalid rooms JSON file."
                )

        # Load guests
        if os.path.exists(
            GUEST_FILE
        ):

            try:

                with open(
                    GUEST_FILE,
                    "r"
                ) as file:

                    data = json.load(file)

                    for item in data:

                        guest = Guest(
                            item["guest_id"],
                            item["name"],
                            item["phone"],
                            item["room_number"]
                        )

                        self.guests.append(
                            guest
                        )

            except json.JSONDecodeError:

                messagebox.showerror(
                    "Error",
                    "Invalid guests JSON file."
                )


# =====================================================
# TKINTER APPLICATION
# =====================================================

class HotelApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Hotel Management System"
        )

        self.root.geometry(
            "1250x750"
        )

        # Create manager object
        self.manager = HotelManager()

        # Load saved data
        self.manager.load_data()

        # =================================================
        # TITLE
        # =================================================

        title = tk.Label(
            root,
            text="Hotel Management System",
            font=(
                "Arial",
                22,
                "bold"
            )
        )

        title.pack(
            pady=10
        )

        # =================================================
        # INPUT FORM
        # =================================================

        form_frame = tk.Frame(
            root
        )

        form_frame.pack(
            pady=10
        )

        # Room Number
        tk.Label(
            form_frame,
            text="Room Number"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.room_entry = tk.Entry(
            form_frame
        )

        self.room_entry.grid(
            row=0,
            column=1
        )

        # Room Type
        tk.Label(
            form_frame,
            text="Room Type"
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        self.room_type_entry = tk.Entry(
            form_frame
        )

        self.room_type_entry.grid(
            row=0,
            column=3
        )

        # Price
        tk.Label(
            form_frame,
            text="Price"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.price_entry = tk.Entry(
            form_frame
        )

        self.price_entry.grid(
            row=1,
            column=1
        )

        # Guest ID
        tk.Label(
            form_frame,
            text="Guest ID"
        ).grid(
            row=1,
            column=2,
            padx=5
        )

        self.guest_id_entry = tk.Entry(
            form_frame
        )

        self.guest_id_entry.grid(
            row=1,
            column=3
        )

        # Guest Name
        tk.Label(
            form_frame,
            text="Guest Name"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5
        )

        self.guest_name_entry = tk.Entry(
            form_frame
        )

        self.guest_name_entry.grid(
            row=2,
            column=1
        )

        # Phone
        tk.Label(
            form_frame,
            text="Phone"
        ).grid(
            row=2,
            column=2,
            padx=5
        )

        self.phone_entry = tk.Entry(
            form_frame
        )

        self.phone_entry.grid(
            row=2,
            column=3
        )

        # Search
        tk.Label(
            form_frame,
            text="Search Room Type"
        ).grid(
            row=3,
            column=0,
            padx=5,
            pady=5
        )

        self.search_entry = tk.Entry(
            form_frame
        )

        self.search_entry.grid(
            row=3,
            column=1
        )

        # =================================================
        # BUTTONS
        # =================================================

        button_frame = tk.Frame(
            root
        )

        button_frame.pack(
            pady=10
        )

        tk.Button(
            button_frame,
            text="Add Room",
            command=self.add_room
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Book Room",
            command=self.book_room
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Check Out",
            command=self.checkout
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Search",
            command=self.search_rooms
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Show All",
            command=self.show_all
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Room Types",
            command=self.show_room_types
        ).grid(
            row=0,
            column=5,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_fields
        ).grid(
            row=0,
            column=6,
            padx=5
        )

        # =================================================
        # ROOM TABLE
        # =================================================

        columns = (
            "Room No",
            "Room Type",
            "Price",
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
                width=220
            )

        self.table.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10
        )

        # =================================================
        # STATUS
        # =================================================

        self.status_label = tk.Label(
            root,
            text="Ready"
        )

        self.status_label.pack(
            pady=5
        )

        self.show_all()

    # =================================================
    # ADD ROOM
    # =================================================

    def add_room(self):

        try:

            room_number = int(
                self.room_entry.get()
            )

            room_type = (
                self.room_type_entry.get()
            )

            price = float(
                self.price_entry.get()
            )

            if room_type == "":

                raise ValueError(
                    "Room type is required."
                )

            if price <= 0:

                raise ValueError(
                    "Price must be greater than zero."
                )

            room = Room(
                room_number,
                room_type,
                price
            )

            self.manager.add_room(
                room
            )

            self.manager.save_data()

            self.show_all()

            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Room added successfully."
            )

        except ValueError as error:

            messagebox.showerror(
                "Input Error",
                str(error)
            )

    # =================================================
    # BOOK ROOM
    # =================================================

    def book_room(self):

        try:

            guest_id = int(
                self.guest_id_entry.get()
            )

            name = (
                self.guest_name_entry.get()
            )

            phone = (
                self.phone_entry.get()
            )

            room_number = int(
                self.room_entry.get()
            )

            if name == "":

                raise ValueError(
                    "Guest name is required."
                )

            if phone == "":

                raise ValueError(
                    "Phone number is required."
                )

            guest = Guest(
                guest_id,
                name,
                phone,
                room_number
            )

            self.manager.book_room(
                guest
            )

            self.manager.save_data()

            self.show_all()

            messagebox.showinfo(
                "Success",
                "Room booked successfully."
            )

        except ValueError as error:

            messagebox.showerror(
                "Booking Error",
                str(error)
            )

    # =================================================
    # CHECKOUT
    # =================================================

    def checkout(self):

        try:

            guest_id = int(
                self.guest_id_entry.get()
            )

            self.manager.checkout_guest(
                guest_id
            )

            self.manager.save_data()

            self.show_all()

            messagebox.showinfo(
                "Success",
                "Guest checked out successfully."
            )

        except ValueError as error:

            messagebox.showerror(
                "Checkout Error",
                str(error)
            )

    # =================================================
    # SEARCH ROOMS
    # =================================================

    def search_rooms(self):

        keyword = (
            self.search_entry.get()
        )

        results = (
            self.manager
            .search_rooms(
                keyword
            )
        )

        self.clear_table()

        for room in results:

            status = (
                "Available"
                if room.available
                else "Booked"
            )

            self.table.insert(
                "",
                tk.END,
                values=(
                    room.room_number,
                    room.room_type,
                    room.price,
                    status
                )
            )

        self.status_label.config(
            text=f"{len(results)} room(s) found."
        )

    # =================================================
    # SHOW ALL ROOMS
    # =================================================

    def show_all(self):

        self.clear_table()

        for room in (
            self.manager.rooms
        ):

            status = (
                "Available"
                if room.available
                else "Booked"
            )

            self.table.insert(
                "",
                tk.END,
                values=(
                    room.room_number,
                    room.room_type,
                    room.price,
                    status
                )
            )

        self.status_label.config(
            text=f"Total Rooms: "
            f"{len(self.manager.rooms)}"
        )

    # =================================================
    # SHOW ROOM TYPES
    # =================================================

    def show_room_types(self):

        room_types = (
            self.manager
            .get_room_types()
        )

        if room_types:

            messagebox.showinfo(
                "Room Types",
                "\n".join(room_types)
            )

        else:

            messagebox.showinfo(
                "Room Types",
                "No room types available."
            )

    # =================================================
    # CLEAR TABLE
    # =================================================

    def clear_table(self):

        for item in (
            self.table
            .get_children()
        ):

            self.table.delete(
                item
            )

    # =================================================
    # CLEAR FIELDS
    # =================================================

    def clear_fields(self):

        entries = (
            self.room_entry,
            self.room_type_entry,
            self.price_entry,
            self.guest_id_entry,
            self.guest_name_entry,
            self.phone_entry,
            self.search_entry
        )

        for entry in entries:

            entry.delete(
                0,
                tk.END
            )


# =====================================================
# MAIN FUNCTION
# =====================================================

def main():

    root = tk.Tk()

    app = HotelApp(
        root
    )

    root.mainloop()


# =====================================================
# PROGRAM ENTRY POINT
# =====================================================

if __name__ == "__main__":

    main()