# Class / Component Diagram

## Main Components

The system is divided into the following components:

- `main.py`
- `room_manager.py`
- `customer_manager.py`
- `booking_manager.py`
- `billing.py`
- `reports.py`
- `validation.py`
- `storage.py`

## Component Relationships

```text
                    +----------------+
                    |    main.py     |
                    | Main Menu      |
                    +-------+--------+
                            |
        +-------------------+-------------------+
        |                   |                   |
        v                   v                   v
+---------------+   +---------------+   +---------------+
| room_manager  |   | customer_     |   | booking_     |
| .py           |   | manager.py    |   | manager.py   |
+-------+-------+   +-------+-------+   +-------+-------+
        |                   |                   |
        +-------------------+-------------------+
                            |
                            v
                    +---------------+
                    |  validation   |
                    |     .py       |
                    +---------------+
                            |
                            v
                    +---------------+
                    |   storage.py  |
                    +-------+-------+
                            |
                            v
                       CSV Files

              +-----------------------+
              | billing.py            |
              | reports.py            |
              +-----------------------+
                         |
                         v
                    storage.py 
                     
| Component             | Responsibility                              |
| --------------------- | ------------------------------------------- |
| `main.py`             | Controls the main menu and application flow |
| `room_manager.py`     | Handles room operations                     |
| `customer_manager.py` | Handles customer operations                 |
| `booking_manager.py`  | Handles bookings and cancellations          |
| `billing.py`          | Calculates and displays bills               |
| `reports.py`          | Generates hotel reports                     |
| `validation.py`       | Validates user input                        |
| `storage.py`          | Reads and writes CSV data                   |

Design

Each component has a specific responsibility. This modular structure makes the project easier to understand, maintain, and modify