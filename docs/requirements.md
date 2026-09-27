# Project Requirements

## 1. Functional Requirements

### Room Management
- View all hotel rooms.
- Add new rooms.
- Update room details.
- Delete available rooms.
- Track room availability.

### Customer Management
- Add customer information.
- View customer records.
- Update customer information.
- Delete customer records.

### Booking Management
- Create a room booking.
- Check whether a customer exists.
- Check room availability.
- View booking records.
- Cancel bookings.
- Update room status after booking or cancellation.

### Billing
- Generate a bill for an active booking.
- Calculate the total amount using room price and number of nights.

### Reports
- Display total rooms.
- Display available and occupied rooms.
- Display total customers.
- Display active and cancelled bookings.
- Display currently available rooms.

## 2. Non-Functional Requirements

### Usability
The system should be simple and easy to operate through a command-line interface.

### Reliability
The system should validate user input and prevent invalid operations such as booking an occupied room.

### Maintainability
The application should be divided into separate Python modules for different functionalities.

### Data Persistence
Room, customer, and booking information should remain stored in CSV files after the application is closed.

### Performance
The system should perform basic operations quickly for a small hotel dataset.

### Error Handling
The system should display meaningful messages when invalid input or unavailable records are entered.