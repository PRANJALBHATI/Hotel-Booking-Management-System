# Use Case Diagram

## Actors

### Hotel Staff
The hotel staff member operates the system and performs room, customer, booking, billing, and reporting operations.

## Use Cases

The Hotel Staff can:

- Manage rooms
- Add, update, view, and delete rooms
- Manage customers
- Add, update, view, and delete customers
- Create bookings
- View bookings
- Cancel bookings
- Generate bills
- View hotel summary
- View available rooms

## Use Case Relationship

```text
                 +----------------------------------+
                 | Hotel Booking Management System  |
                 |                                  |
Hotel Staff ---->| Manage Rooms                     |
                 |                                  |
Hotel Staff ---->| Manage Customers                 |
                 |                                  |
Hotel Staff ---->| Create Booking                   |
                 |                                  |
Hotel Staff ---->| View Bookings                    |
                 |                                  |
Hotel Staff ---->| Cancel Booking                   |
                 |                                  |
Hotel Staff ---->| Generate Bill                    |
                 |                                  |
Hotel Staff ---->| View Hotel Reports               |
                 |                                  |
                 +----------------------------------+  

Description

The Hotel Staff is the primary actor of the system.

The actor interacts with the system through the command-line interface to perform hotel management operations.

The system processes the requested operation and stores or retrieves information from the CSV files.