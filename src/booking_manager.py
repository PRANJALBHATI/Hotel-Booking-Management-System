from storage import read_data, write_data
from validation import get_non_empty_input, get_positive_integer


ROOM_FILE = "data/rooms.csv"
CUSTOMER_FILE = "data/customers.csv"
BOOKING_FILE = "data/bookings.csv"


def create_booking():
    rooms = read_data(ROOM_FILE)
    customers = read_data(CUSTOMER_FILE)
    bookings = read_data(BOOKING_FILE)

    customer_id = get_non_empty_input("Enter customer ID: ")

    customer_found = False

    for customer in customers:
        if customer["customer_id"] == customer_id:
            customer_found = True
            break

    if not customer_found:
        print("Customer not found. Please add the customer first.")
        return

    room_number = get_non_empty_input("Enter room number: ")

    room_found = False

    for room in rooms:
        if room["room_number"] == room_number:

            room_found = True

            if room["status"] == "Occupied":
                print("Room is already occupied.")
                return

            break

    if not room_found:
        print("Room not found.")
        return

    booking_id = str(len(bookings) + 1)

    number_of_nights = get_positive_integer(
        "Enter number of nights: "
    )

    new_booking = {
        "booking_id": booking_id,
        "customer_id": customer_id,
        "room_number": room_number,
        "number_of_nights": str(number_of_nights),
        "status": "Active"
    }

    bookings.append(new_booking)

    booking_fields = [
        "booking_id",
        "customer_id",
        "room_number",
        "number_of_nights",
        "status"
    ]

    write_data(BOOKING_FILE, bookings, booking_fields)

    for room in rooms:
        if room["room_number"] == room_number:
            room["status"] = "Occupied"
            break

    room_fields = [
        "room_number",
        "room_type",
        "price",
        "status"
    ]

    write_data(ROOM_FILE, rooms, room_fields)

    print("Booking created successfully.")
    print("Booking ID:", booking_id)


def view_bookings():
    bookings = read_data(BOOKING_FILE)

    if len(bookings) == 0:
        print("No bookings found.")
        return

    print("\nBooking ID | Customer ID | Room | Nights | Status")
    print("-------------------------------------------------")

    for booking in bookings:
        print(
            booking["booking_id"],
            "|",
            booking["customer_id"],
            "|",
            booking["room_number"],
            "|",
            booking["number_of_nights"],
            "|",
            booking["status"]
        )


def cancel_booking():
    bookings = read_data(BOOKING_FILE)
    rooms = read_data(ROOM_FILE)

    booking_id = get_non_empty_input(
        "Enter booking ID to cancel: "
    )

    for booking in bookings:

        if booking["booking_id"] == booking_id:

            if booking["status"] == "Cancelled":
                print("Booking is already cancelled.")
                return

            booking["status"] = "Cancelled"

            room_number = booking["room_number"]

            for room in rooms:
                if room["room_number"] == room_number:
                    room["status"] = "Available"
                    break

            booking_fields = [
                "booking_id",
                "customer_id",
                "room_number",
                "number_of_nights",
                "status"
            ]

            room_fields = [
                "room_number",
                "room_type",
                "price",
                "status"
            ]

            write_data(
                BOOKING_FILE,
                bookings,
                booking_fields
            )

            write_data(
                ROOM_FILE,
                rooms,
                room_fields
            )

            print("Booking cancelled successfully.")
            return

    print("Booking not found.")