from storage import read_data
from validation import get_non_empty_input


ROOM_FILE = "data/rooms.csv"
BOOKING_FILE = "data/bookings.csv"


def generate_bill():
    rooms = read_data(ROOM_FILE)
    bookings = read_data(BOOKING_FILE)

    booking_id = get_non_empty_input(
        "Enter booking ID: "
    )

    selected_booking = None

    for booking in bookings:
        if booking["booking_id"] == booking_id:
            selected_booking = booking
            break

    if selected_booking is None:
        print("Booking not found.")
        return

    if selected_booking["status"] == "Cancelled":
        print("Cannot generate bill for a cancelled booking.")
        return

    room_number = selected_booking["room_number"]
    number_of_nights = int(
        selected_booking["number_of_nights"]
    )

    room_price = 0

    for room in rooms:
        if room["room_number"] == room_number:
            room_price = float(room["price"])
            break

    if room_price == 0:
        print("Room information not found.")
        return

    total_amount = room_price * number_of_nights

    print("\n========== HOTEL BILL ==========")
    print("Booking ID:", booking_id)
    print("Customer ID:", selected_booking["customer_id"])
    print("Room Number:", room_number)
    print("Room Price per Night: ₹", room_price)
    print("Number of Nights:", number_of_nights)
    print("--------------------------------")
    print("Total Amount: ₹", total_amount)
    print("================================")