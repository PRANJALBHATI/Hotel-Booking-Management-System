def get_non_empty_input(message):
    while True:
        value = input(message)

        if value.strip() != "":
            return value

        print("Input cannot be empty.")


def get_positive_number(message):
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value

            print("Please enter a positive number.")

        except ValueError:
            print("Please enter a valid number.")


def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Please enter a positive integer.")

        except ValueError:
            print("Please enter a valid integer.")