# System Workflow

## Main Workflow

```text
Start
  |
  v
Launch Application
  |
  v
Display Main Menu
  |
  +-----------------------------+
  |                             |
  v                             v
Room Management          Customer Management
  |                             |
  +-------------+---------------+
                |
                v
        Booking Management
                |
                v
        Check Customer
                |
                v
         Check Room Status
                |
          +-----+-----+
          |           |
       Available    Occupied
          |           |
          v           v
    Create Booking  Reject Booking
          |
          v
     Update Room
       Status
          |
          v
      Generate Bill
          |
          v
       View Reports
          |
          v
       Main Menu
          |
          v
          Exit

Booking Workflow
1- User selects Booking Management.
2- User enters the customer ID.
3- System checks whether the customer exists.
4- User enters the room number.
5- System checks whether the room exists.
6- System checks the room status.
7- If the room is available, the booking is created.
8- The room status is changed to Occupied.
9- The booking is stored in bookings.csv.
10- The user can generate a bill using the booking ID.


Cancellation Workflow
1- User selects Cancel Booking.
2- User enters the booking ID.
3- System searches for the booking.
4- System checks whether the booking is already cancelled.
5- The booking status is changed to Cancelled.
6- The related room status is changed back to Available.
7- The updated information is saved to the CSV files.