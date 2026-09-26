from storage import read_data, write_data
from validation import get_non_empty_input, get_positive_number


ROOM_FILE = "data/rooms.csv"


def view_rooms():
    rooms = read_data(ROOM_FILE)

    if len(rooms) == 0:
        print("No rooms available.")
        return

    print("\nRoom Number | Room Type | Price | Status")
    print("------------------------------------------")

    for room in rooms:
        print(
            room["room_number"],
            "|",
            room["room_type"],
            "| ₹" + room["price"],
            "|",
            room["status"]
        )


def add_room():
    rooms = read_data(ROOM_FILE)

    room_number = get_non_empty_input("Enter room number: ")

    for room in rooms:
        if room["room_number"] == room_number:
            print("Room already exists.")
            return

    room_type = get_non_empty_input("Enter room type: ")
    price = get_positive_number("Enter room price: ")

    new_room = {
        "room_number": room_number,
        "room_type": room_type,
        "price": str(price),
        "status": "Available"
    }

    rooms.append(new_room)

    fieldnames = ["room_number", "room_type", "price", "status"]

    write_data(ROOM_FILE, rooms, fieldnames)

    print("Room added successfully.")


def update_room():
    rooms = read_data(ROOM_FILE)

    room_number = get_non_empty_input("Enter room number to update: ")

    for room in rooms:
        if room["room_number"] == room_number:

            print("Current room type:", room["room_type"])
            print("Current price:", room["price"])

            room["room_type"] = get_non_empty_input(
                "Enter new room type: "
            )

            room["price"] = str(
                get_positive_number("Enter new room price: ")
            )

            fieldnames = ["room_number", "room_type", "price", "status"]

            write_data(ROOM_FILE, rooms, fieldnames)

            print("Room updated successfully.")
            return

    print("Room not found.")


def delete_room():
    rooms = read_data(ROOM_FILE)

    room_number = get_non_empty_input("Enter room number to delete: ")

    for room in rooms:
        if room["room_number"] == room_number:

            if room["status"] == "Occupied":
                print("Occupied room cannot be deleted.")
                return

            rooms.remove(room)

            fieldnames = ["room_number", "room_type", "price", "status"]

            write_data(ROOM_FILE, rooms, fieldnames)

            print("Room deleted successfully.")
            return

    print("Room not found.")