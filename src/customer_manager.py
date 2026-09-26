from storage import read_data, write_data
from validation import get_non_empty_input


CUSTOMER_FILE = "data/customers.csv"


def view_customers():
    customers = read_data(CUSTOMER_FILE)

    if len(customers) == 0:
        print("No customers found.")
        return

    print("\nCustomer ID | Name | Phone | Email")
    print("------------------------------------")

    for customer in customers:
        print(
            customer["customer_id"],
            "|",
            customer["name"],
            "|",
            customer["phone"],
            "|",
            customer["email"]
        )


def add_customer():
    customers = read_data(CUSTOMER_FILE)

    customer_id = get_non_empty_input("Enter customer ID: ")

    for customer in customers:
        if customer["customer_id"] == customer_id:
            print("Customer ID already exists.")
            return

    name = get_non_empty_input("Enter customer name: ")
    phone = get_non_empty_input("Enter phone number: ")
    email = get_non_empty_input("Enter email: ")

    new_customer = {
        "customer_id": customer_id,
        "name": name,
        "phone": phone,
        "email": email
    }

    customers.append(new_customer)

    fieldnames = ["customer_id", "name", "phone", "email"]

    write_data(CUSTOMER_FILE, customers, fieldnames)

    print("Customer added successfully.")


def update_customer():
    customers = read_data(CUSTOMER_FILE)

    customer_id = get_non_empty_input(
        "Enter customer ID to update: "
    )

    for customer in customers:
        if customer["customer_id"] == customer_id:

            customer["name"] = get_non_empty_input(
                "Enter new name: "
            )

            customer["phone"] = get_non_empty_input(
                "Enter new phone number: "
            )

            customer["email"] = get_non_empty_input(
                "Enter new email: "
            )

            fieldnames = ["customer_id", "name", "phone", "email"]

            write_data(CUSTOMER_FILE, customers, fieldnames)

            print("Customer updated successfully.")
            return

    print("Customer not found.")


def delete_customer():
    customers = read_data(CUSTOMER_FILE)

    customer_id = get_non_empty_input(
        "Enter customer ID to delete: "
    )

    for customer in customers:
        if customer["customer_id"] == customer_id:

            customers.remove(customer)

            fieldnames = ["customer_id", "name", "phone", "email"]

            write_data(CUSTOMER_FILE, customers, fieldnames)

            print("Customer deleted successfully.")
            return

    print("Customer not found.")