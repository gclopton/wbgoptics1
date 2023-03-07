import fileinput
from filenames import system, chg, functional

# Set the filename of the text file to update
filename = 'vasp5_submit'

# Set the new value for the #SBATCH -J option
new_value = system + chg + functional

# Open the file in place for editing
with fileinput.FileInput(filename, inplace=True) as file:
    # Iterate over each line in the file
    for line in file:
        # Check if the line contains "#SBATCH -J"
        if line.startswith('#SBATCH -J'):
            # Replace the value of #SBATCH -J with the new value
            line = f"#SBATCH -J {new_value}\n"
        # Write the line to the output file
        print(line, end='')
