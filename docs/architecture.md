# System Architecture

## Architecture Overview

The Hotel Booking Management System follows a simple modular architecture.

The system is divided into separate modules, where each module is responsible for a specific part of the application.

## Architecture Components

### 1. User Interface
The command-line interface allows the user to interact with the system through menus and inputs.

### 2. Application Modules
The main Python modules handle different operations:

- `main.py` - Main menu and application control
- `room_manager.py` - Room management
- `customer_manager.py` - Customer management
- `booking_manager.py` - Booking and cancellation
- `billing.py` - Bill generation
- `reports.py` - Hotel reports
- `validation.py` - Input validation
- `storage.py` - CSV data reading and writing

### 3. Data Storage
The system stores information in CSV files:

- `rooms.csv` - Room information
- `customers.csv` - Customer information
- `bookings.csv` - Booking information

## Architecture Flow

```text
User
  |
  v
Command-Line Interface
  |
  v
main.py
  |
  +-------------------+
  |        |          |
  v        v          v
Room    Customer    Booking
Manager  Manager     Manager
  |        |          |
  +--------+----------+
           |
           v
       Billing / Reports
           |
           v
        storage.py
           |
           v
        CSV Files

Design Approach

The project uses a modular design so that each major functionality is handled by a separate Python file.

This improves:

Code organization
Maintainability
Readability
Reusability
Error handling