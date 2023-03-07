def read_write_file():
    search_text = " magnetization (x)"  # replace with the text you want to search for
    num_lines = 164  # replace with the number of lines you want to copy

    # Open the input file for reading
    with open("OUTCAR", "r") as f:
        lines = f.readlines()

    # Find the last instance of the search text in the file
    last_match = None
    for i in range(len(lines)-1, -1, -1):
        if search_text in lines[i]:
            last_match = i
            break

    # If a match was found, copy the specified number of lines below it to the output file
    if last_match is not None:
        output_lines = lines[last_match+1:last_match+num_lines+1]
        with open("magnetization_table.txt", "w") as f:
            f.writelines(output_lines)
            print("Copied {} lines to output file".format(num_lines))
    else:
        print("No match found in input file")
read_write_file()

input_file = "magnetization_table.txt"  # replace with the name of your input file

with open(input_file, "r") as f:
    lines = f.readlines()

output_lines = []
for line in lines[2:]:  # ignore the first two header lines
    fields = line.strip().split()
    if len(fields) >= 1:
        try:
            last_col = float(fields[-1])
            if last_col < -0.01 or last_col > 0.01:  # keep lines where the last column is less than -0.01 or greater than 0.01
                output_lines.append(line)
        except ValueError:
            # Ignore lines where the last field is not a valid number
            pass

print('hello')

with open("magnetization_stripped.txt", "w") as f:
    f.writelines(output_lines)