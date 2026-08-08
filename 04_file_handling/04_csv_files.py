import csv

# Writing to a CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # Header row
    writer.writerow(["Name", "Age", "Marks"])
    # Data rows
    writer.writerow(["M", 21, 85])
    writer.writerow(["Alice", 22, 90])
    writer.writerow(["Bob", 20, 78])

print("CSV file created successfully.")

# Reading from a CSV file
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print("Row:", row)

# Using DictWriter and DictReader (more readable)
with open("students_dict.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "Marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "M", "Age": 21, "Marks": 85})
    writer.writerow({"Name": "Alice", "Age": 22, "Marks": 90})
    writer.writerow({"Name": "Bob", "Age": 20, "Marks": 78})

print("CSV file with DictWriter created successfully.")

with open("students_dict.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("Name:", row["Name"], "| Age:", row["Age"], "| Marks:", row["Marks"])
