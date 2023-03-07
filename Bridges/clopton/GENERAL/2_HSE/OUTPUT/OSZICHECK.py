with open('OSZICAR', 'r') as f:
    lines = f.readlines()

data = []
for line in lines:
    if line.startswith('SDA') or line.startswith('CGA') or line.startswith('DAV') or line.startswith('RMM'):
        columns = line.split()
        data.append(columns[1])

with open('output.txt', 'w') as f:
    for d in data:
        f.write(d + '\n')

with open("output.txt", "r") as f:
    lines = f.readlines()

has_large_number = False
for line in lines:
    number = int(line.strip())
    if number >= 40:
        has_large_number = True
        break

if has_large_number:
    print("OSZICAR: Calculation Failed. NELM reached Max")
else:
    print("OSZICAR: Calculation Converged")
