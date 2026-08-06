# Dictionaries Practice

# Creating a dictionary
student = {
    "name": "M",
    "course": "BCA",
    "year": "Final",
    "marks": [85, 90, 78]
}

# Accessing values
print("Name:", student["name"])
print("Course:", student.get("course"))  # safer way

# Updating values
student["year"] = "Graduated"
print("Updated Year:", student["year"])

# Adding new key-value pair
student["cgpa"] = 8.5
print("After adding CGPA:", student)

# Removing key-value pair
student.pop("marks")
print("After removing marks:", student)

# Looping through dictionary
print("\nLooping through dictionary:")
for key, value in student.items():
    print(key, ":", value)

# Nested dictionary
students = {
    1: {"name": "Alice", "course": "BCA"},
    2: {"name": "Bob", "course": "Data Science"},
    3: {"name": "Charlie", "course": "Web Development"}
}

print("\nNested Dictionary Example:")
print("Student 2:", students[2]["name"], "-", students[2]["course"])
