'''
Experiment No. 9
Title: File Handling and I/O - Reading/writing files (CSV and JSON)
Aim: Write a program to read data from a CSV file and convert the data to JSON format. 
     Write the JSON data to .json output file.
'''

import csv
import json
import os

def create_sample_csv(csv_filepath="input.csv"):
    """Helper function to create a sample CSV file if it does not already exist."""
    if not os.path.exists(csv_filepath):
        sample_rows = [
            ["Name", "Branch", "Year", "CGPA"],
            ["Nikhil", "COE", "2", "9.0"],
            ["Sanchit", "COE", "2", "9.1"],
            ["Aditya", "IT", "2", "9.3"],
            ["Sagar", "SE", "1", "9.5"],
            ["Prateek", "MCE", "3", "7.8"],
            ["Sahil", "EP", "2", "9.1"]
        ]
        with open(csv_filepath, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(sample_rows)
        print(f"Sample CSV file '{csv_filepath}' created successfully.")

def csv_to_json(csv_filepath="input.csv", json_filepath="output.json"):
    """
    Reads data from a CSV file, converts each row into a dictionary,
    and writes the list of dictionaries to a JSON file.
    """
    # Ensure sample CSV file exists for demonstration
    create_sample_csv(csv_filepath)

    # Step 1: Create an empty list to store row dictionaries
    json_array = []

    # Step 2: Open and read the CSV file
    print(f"\nReading data from CSV file '{csv_filepath}'...")
    with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
        # Load CSV file data using csv library's DictReader
        csv_reader = csv.DictReader(csv_file)
        
        # Step 3: Convert each CSV row into a Python dictionary and append to list
        for row in csv_reader:
            json_array.append(row)

    print(f"Total records converted: {len(json_array)}")

    # Step 4: Write the list of dictionaries to a JSON file
    print(f"\nWriting converted data to JSON file '{json_filepath}'...")
    with open(json_filepath, mode='w', encoding='utf-8') as json_file:
        # Serialize python list of dictionaries to formatted JSON string
        json_string = json.dumps(json_array, indent=4)
        json_file.write(json_string)

    print(f"Data successfully written to '{json_filepath}'.")

    # Step 5: Verification - Display contents of both files
    print(f"\n--- Content of Input CSV ('{csv_filepath}') ---")
    with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
        print(csv_file.read().strip())

    print(f"\n--- Content of Output JSON ('{json_filepath}') ---")
    with open(json_filepath, mode='r', encoding='utf-8') as json_file:
        print(json_file.read().strip())

if __name__ == "__main__":
    # Define file paths
    input_csv = "input.csv"
    output_json = "output.json"
    
    csv_to_json(input_csv, output_json)
