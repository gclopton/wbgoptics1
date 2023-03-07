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

search_col1 = system + '/' + chg
search_col2 = 'Joel'

# Open the CSV file
with open('../../../../MAGMOM_PBE.csv', newline='') as csvfile:
    # Create a CSV reader
    reader = csv.reader(csvfile)

    # Initialize a variable to store the third value
    third_value = None

    # Iterate over each row in the file
    for row in reader:
        # Check if the first column contains the search term and the second column contains the search term
        if row[0] == search_col1:
            # Store the third value from the matching row in a variable
            third_value = row[1]
            break

# Open the input and output files
with open('INCAR', 'r') as infile, open('INCAR_updated', 'w') as outfile:
    # Initialize a variable to track if "MAGMOM" has been found in the file
    magmom_found = False

    # Iterate over each line in the input file
    for line in infile:
        # Check if the line contains "MAGMOM ="
        if "MAGMOM =" in line:
            # Update the value of MAGMOM to the value of the third column from the CSV file
            if third_value:
                new_line = f"MAGMOM = {third_value}\n"
            else:
                new_line = line
            magmom_found = True
        else:
            new_line = line

        # Write the line to the output file
        outfile.write(new_line)

    # If "MAGMOM" was not found in the file, add it to the end of the file
    if not magmom_found and third_value:
        outfile.write(f"MAGMOM = {third_value}\n")

# Print the search column 1
print(third_value)
