import csv

import os

current_dir = os.getcwd()
print(current_dir)

system_path = os.path.abspath(os.path.join(os.getcwd(), "../../../"))
chg_path = os.path.abspath(os.path.join(os.getcwd(), "../../"))
functional_path = os.path.abspath(os.path.join(os.getcwd(), "../"))

system = os.path.basename(system_path)
print(system)
chg = os.path.basename(chg_path)
print(chg)
functional = os.path.basename(functional_path)
print(functional)


# Store the search terms as variables
search_col1 = system
search_col2 = chg

# Open the CSV file
with open('../../../../NELECT.csv', newline='') as csvfile:
    # Create a CSV reader
    reader = csv.reader(csvfile)

    # Initialize a variable to store the value from the third column
    value = None

    # Iterate over each row in the file
    for row in reader:
        # Check if the first column contains the search term and the second column contains the search term
        if row[0] == search_col1 and row[1] == search_col2:
            # Store the value from the third column in a variable
            value = row[2]

# Open the input and output files
with open('INCAR_updated', 'r') as infile, open('INCAR_final', 'w') as outfile:
    # Keep track of whether the NELECT line has been found
    found_nelect = False

    # Iterate over each line in the input file
    for line in infile:
        # Check if the line contains "NELECT ="
        if "NELECT =" in line:
            # Update the value of NELECT to the value stored in the value variable
            new_line = f"NELECT = {value}\n"
            found_nelect = True
        else:
            new_line = line

        # Write the line to the output file
        outfile.write(new_line)

    # If the NELECT line has not been found, add it to the end of the file
    if not found_nelect:
        outfile.write(f"NELECT = {value}\n")