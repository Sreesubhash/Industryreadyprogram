# salary as ascending order
emp_data = []
with open("emp.csv") as f:
    columns = f.readline()
    for line in f:
        row = line.rstrip("\n").split(",")
        row[7] = int(row[7])
        emp_data.append(row[:8])

emp_data.sort(key=lambda x: x[7])

for row in emp_data:
    print(row)

# salary as descending order
emp_data = []
with open("emp.csv") as f:
    columns = f.readline()
    for line in f:
        row = line.rstrip("\n").split(",")
        row[7] = int(row[7])
        emp_data.append(row[:8])

emp_data.sort(key=lambda x: x[7], reverse = True)

for row in emp_data:
    print(row)

# string as name in descending order
emp_data = []
with open("emp.csv") as f:
    columns = f.readline()
    for line in f:
        row = line.rstrip("\n").split(",")
        row[1] = str(row[1])
        emp_data.append(row[:8])

emp_data.sort(key=lambda x: x[1], reverse = True)

for row in emp_data:
    print(row)