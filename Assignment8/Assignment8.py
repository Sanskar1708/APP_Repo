'''
Experiment No. 8
Aim: Create a Python script to read data from an input file. Perform count lines, 
extract the first two lines, and write the extracted data into a new file.
'''

import os

def create_sample_input_file(filename="input.txt"):
    """Helper function to create a sample input file if it does not already exist."""
    if not os.path.exists(filename):
        sample_data = [
            "Line 1: Python is a powerful programming language.\n",
            "Line 2: File handling is an essential part of programming.\n",
            "Line 3: It allows reading and writing operations on secondary storage.\n",
            "Line 4: This is the fourth line of the sample text file.\n",
            "Line 5: End of the sample input file.\n"
        ]
        with open(filename, "w") as f:
            f.writelines(sample_data)
        print(f"Sample '{filename}' created successfully.")

def process_file(input_filename="input.txt", output_filename="output.txt"):
    # Ensure the input file exists for demonstration
    create_sample_input_file(input_filename)

    # Step 1: Open the input file in read mode ('r')
    print(f"Opening '{input_filename}' to read data...")
    input_file = open(input_filename, "r")

    # Step 2: Read all lines from the file into a list
    lines = input_file.readlines()

    # Step 3: Count the number of lines
    total_lines = len(lines)
    print(f"\n--- File Content of '{input_filename}' ---")
    for line in lines:
        print(line, end="")
    print(f"\n\nTotal number of lines in '{input_filename}': {total_lines}")

    # Step 4: Extract the first two lines
    first_two_lines = lines[:2]
    print(f"\nExtracted first two lines ({len(first_two_lines)} lines):")
    for line in first_two_lines:
        print(line, end="")

    # Close the input file
    input_file.close()

    # Step 5: Open the output file in write mode ('w')
    output_file = open(output_filename, "w")

    # Step 6: Write the extracted lines to the output file
    output_file.writelines(first_two_lines)

    # Step 7: Close the output file
    output_file.close()
    print(f"\nSuccessfully written extracted lines to '{output_filename}'.")

    # Verification: Display content of output.txt
    print(f"\n--- Content of '{output_filename}' ---")
    with open(output_filename, "r") as out_f:
        print(out_f.read(), end="")

if __name__ == "__main__":
    process_file()
