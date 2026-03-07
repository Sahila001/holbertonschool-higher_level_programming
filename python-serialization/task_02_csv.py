#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(filename):
    """
    Convert CSV data to JSON format and save it to data.json

    Args:
        filename: CSV file name

    Returns:
        True if successful, False otherwise
    """
    try:
        data_list = []

        with open(filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                data_list.append(row)

        with open("data.json", "w") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
