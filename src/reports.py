from storage import read_data


ROOM_FILE = "data/rooms.csv"
CUSTOMER_FILE = "data/customers.csv"
BOOKING_FILE = "data/bookings.csv"


def show_hotel_summary():
    rooms = read_data(ROOM_FILE)
    customers = read_data(CUSTOMER_FILE)
    bookings = read_data(BOOKING_FILE)

    total_rooms = len(rooms)
    available_rooms = 0
    occupied_rooms = 0

    for room in rooms:
        if room["status"] == "Available":
            available_rooms += 1
        elif room["status"] == "Occupied":
            occupied_rooms += 1

    total_customers = len(customers)

    active_bookings = 0
    cancelled_bookings = 0

    for booking in bookings:
        if booking["status"] == "Active":
            active_bookings += 1
        elif booking["status"] == "Cancelled":
            cancelled_bookings += 1

    print("\n========== HOTEL SUMMARY ==========")
    print("Total Rooms:", total_rooms)
    print("Available Rooms:", available_rooms)
    print("Occupied Rooms:", occupied_rooms)
    print("Total Customers:", total_customers)
    print("Active Bookings:", active_bookings)
    print("Cancelled Bookings:", cancelled_bookings)
    print("===================================")


def show_available_rooms():
    rooms = read_data(ROOM_FILE)

    print("\n========== AVAILABLE ROOMS ==========")

    found = False

    for room in rooms:
        if room["status"] == "Available":
            print(
                "Room:",
                room["room_number"],
                "| Type:",
                room["room_type"],
                "| Price: ₹" + room["price"]
            )
            found = True

    if not found:
        print("No rooms are currently available.")

    print("=====================================")