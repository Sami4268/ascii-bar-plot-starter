import csv
import os


def load_rows(csv_path):
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(csv_path)

    rows = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(
                (
                    row["type"],
                    float(row["value1"]),
                    float(row["value2"]),
                )
            )

    return rows