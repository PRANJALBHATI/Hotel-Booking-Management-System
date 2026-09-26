from room_manager import (
    view_rooms,
    add_room,
    update_room,
    delete_room
)

from customer_manager import (
    view_customers,
    add_customer,
    update_customer,
    delete_customer
)

from booking_manager import (
    create_booking,
    view_bookings,
    cancel_booking
)

from billing import generate_bill

from reports import (
    show_hotel_summary,
    show_available_rooms
)


def room_menu():
    while True:
        print("\n========== ROOM MANAGEMENT ==========")
        print("1. View Rooms")
        print("2. Add Room")
        print("3. Update Room")
        print("4. Delete Room")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_rooms()

        elif choice == "2":
            add_room()

        elif choice == "3":
            update_room()

        elif choice == "4":
            delete_room()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


def customer_menu():
    while True:
        print("\n========== CUSTOMER MANAGEMENT ==========")
        print("1. View Customers")
        print("2. Add Customer")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_customers()

        elif choice == "2":
            add_customer()

        elif choice == "3":
            update_customer()

        elif choice == "4":
            delete_customer()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


def booking_menu():
    while True:
        print("\n========== BOOKING MANAGEMENT ==========")
        print("1. Create Booking")
        print("2. View Bookings")
        print("3. Cancel Booking")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_booking()

        elif choice == "2":
            view_bookings()

        elif choice == "3":
            cancel_booking()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\n")
        print("==============================================")
        print("     HOTEL BOOKING MANAGEMENT SYSTEM")
        print("==============================================")
        print("1. Room Management")
        print("2. Customer Management")
        print("3. Booking Management")
        print("4. Generate Bill")
        print("5. Hotel Reports")
        print("6. Exit")
        print("==============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            room_menu()

        elif choice == "2":
            customer_menu()

        elif choice == "3":
            booking_menu()

        elif choice == "4":
            generate_bill()

        elif choice == "5":
            print("\n========== REPORTS ==========")
            print("1. Hotel Summary")
            print("2. Available Rooms")

            report_choice = input("Enter your choice: ")

            if report_choice == "1":
                show_hotel_summary()

            elif report_choice == "2":
                show_available_rooms()

            else:
                print("Invalid choice.")

        elif choice == "6":
            print("Thank you for using Hotel Booking Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


main()