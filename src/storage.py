import csv


def read_data(filename):
    data = []

    try:
        file = open(filename, "r", newline="")
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

        file.close()

    except FileNotFoundError:
        print("File not found:", filename)

    return data


def write_data(filename, data, fieldnames):
    file = open(filename, "w", newline="")
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for row in data:
        writer.writerow(row)

    file.close()