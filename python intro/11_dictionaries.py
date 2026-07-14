#1. Create a dictionary of a student (name, age, course).
student={'name':'nouman', 'age': 20, 'course':'bca'}
# Print the complete dictionary.
print(student)
print(type(student))
# Print only the student's name.
print(student['name'])
# Print only the student's age.
print(student['age'])
# Find the length of the dictionary.
print(len(student))
# Level 2
# Add a new key called "Marks".
student['marks']=67
print(student)
# Update the student's age.
student['age']=21
print(student)
# Remove "course" using pop().
student.pop('course')
print(student)
# Display all keys using keys().
print(student.keys())

# Display all values using values().
print(student.values())
# Level 3
# Display both keys and values using items().
print(student.items())
# Check whether "age" exists.
if 'age' in student:
    print("yes,age column exist")
else:
    print(" NO< Age column NOT exist.")
# Check whether "salary" exists.
if 'salary' in student:
    print("yes,Salary column exist")
else:
    print("No, salary coulmn not exist")

# Clear the dictionary.
student.clear()
print(student)
# Create a dictionary of 3 students and print their names.
# dictionary of students
students = {
    1: {"name": "Alice", "course": "BCA"},
    2: {"name": "Bob", "course": "Data Science"},
    3: {"name": "Charlie", "course": "Web Development"}
}

# print names of all students
for student_id, details in students.items():
    print(details["name"])
