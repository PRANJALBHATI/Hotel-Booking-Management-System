# Data Storage Design

## Storage Method

The system uses CSV files for persistent data storage.

The three main data files are:

- `rooms.csv`
- `customers.csv`
- `bookings.csv`

## Room Data

| Field | Description |
|---|---|
| room_number | Unique room number |
| room_type | Type of room |
| price | Price per night |
| status | Available or Occupied |

## Customer Data

| Field | Description |
|---|---|
| customer_id | Unique customer ID |
| name | Customer name |
| phone | Customer phone number |
| email | Customer email |

## Booking Data

| Field | Description |
|---|---|
| booking_id | Unique booking ID |
| customer_id | ID of the customer |
| room_number | Booked room number |
| number_of_nights | Number of nights |
| status | Active or Cancelled |

## Data Relationships

```text
+------------------+
|    CUSTOMER      |
+------------------+
| customer_id (PK) |
| name             |
| phone            |
| email            |
+--------+---------+
         |
         | customer_id
         |
         v
+------------------+
|     BOOKING      |
+------------------+
| booking_id (PK)  |
| customer_id (FK) |
| room_number (FK) |
| number_of_nights |
| status           |
+--------+---------+
         |
         | room_number
         |
         v
+------------------+
|      ROOM        |
+------------------+
| room_number (PK) |
| room_type       |
| price            |
| status           |
+------------------+

Relationship Description
-One customer can have multiple bookings.
-Each booking is associated with one customer.
-Each booking is associated with one room.
-Room status is updated when a booking is created or cancelled.
-Storage Module

The storage.py module provides functions to:

-Read data from CSV files.
-Write updated data to CSV files.

This keeps file-handling logic separate from the main application modules.