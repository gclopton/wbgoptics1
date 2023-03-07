import os
import re
import csv

current_dir = os.getcwd()
print(current_dir)

system_path = os.path.abspath(os.path.join(os.getcwd(), "../../../"))
chg_path = os.path.abspath(os.path.join(os.getcwd(), "../../"))
functional_path = os.path.abspath(os.path.join(os.getcwd(), "../"))

system = os.path.basename(system_path)
chg = os.path.basename(chg_path)
functional = os.path.basename(functional_path)



with open('INCAR', 'r') as file:
    # Read the contents of the file into a list of lines
    lines = file.readlines()

# Search for the line that starts with "MAGMOM ="
magmom_line = [line for line in lines if line.startswith('MAGMOM =')][0]
nelect_line = [line for line in lines if line.startswith('NELECT =')][0]

# Extract the value of MAGMOM using regular expressions
incar_magmom_value = re.search(r'MAGMOM\s*=\s*(.*)', magmom_line).group(1)
incar_nelect_value = re.search(r'NELECT\s*=\s*(.*)', nelect_line).group(1)

# Print the value of MAGMOM
print('\033[34m' + incar_magmom_value + '\033[0m')
# Print the value of NELECT in blue
print('\033[34m' + incar_nelect_value + '\033[0m')

# Set the values of search_col1 and search_col2
search_col1 = system
search_col2 = chg

# Open the CSV file for reading
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
            break

# If a matching row is found, print the value from the third column
if value is not None:
    print(value)
else:
    print(f"No row found with {search_col1} and {search_col2}")


filename = "../../../../MAGMOM_PBE.csv"
search_term = system + '/' + chg
value = None

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row[0] == search_term:
            value = row[1]
            break

if value is not None:
    print(value)
else:
    print(f"No row containing {search_term} was found in the file.")
