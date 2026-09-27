# Sequence Diagram

## Booking Creation Sequence

The following sequence describes how a new hotel booking is created.

```text
User
 |
 | Select Booking Management
 v
main.py
 |
 | Request customer ID
 v
booking_manager.py
 |
 | Check customer
 v
storage.py
 |
 | Read customers.csv
 v
booking_manager.py
 |
 | Request room number
 v
storage.py
 |
 | Read rooms.csv
 v
booking_manager.py
 |
 | Check room availability
 |
 | Create booking
 v
storage.py
 |
 | Write booking to bookings.csv
 |
 | Update room status
 v
storage.py
 |
 | Write updated room to rooms.csv
 |
 v
User
 |
 | Booking created successfully



 Sequence Steps
1- The user selects Booking Management from the main menu.
2- main.py calls the booking management function.
3- booking_manager.py requests the customer ID.
4- The system checks the customer information using storage.py.
5- The user enters the room number.
6- The system checks the room information and availability.
7- The user enters the number of nights.
8- The booking information is stored in bookings.csv.
9- The room status is changed to Occupied.
10- The updated room information is stored in rooms.csv.
11- The system displays a successful booking message.

Components Involved
-User
-main.py
-booking_manager.py
-storage.py
-customers.csv
-rooms.csv
-bookings.csv