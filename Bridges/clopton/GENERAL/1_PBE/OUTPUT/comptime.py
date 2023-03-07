# Open the OUTCAR file for reading
with open('OUTCAR', 'r') as f:
    # Iterate through each line in the file
    for line in f:
        # Check if the line contains "User time (sec):"
        if 'User time (sec):' in line:
            # Extract the numerical value following the colon
            value_str = line.split(':')[1].strip()
            # Convert the value to a float
            value = float(value_str)
            # Compute the comptime variable
            comptime = value / 3600 * 64
            # Print the comptime variable to the screen
            print(comptime)
            # Exit the loop since we found the line we were looking for
            break
