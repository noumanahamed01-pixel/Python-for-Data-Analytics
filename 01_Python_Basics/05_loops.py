# For loop example
for i in range(1, 6):
    print("Number:", i)

# While loop example
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Looping through a list
students = ["Alice", "Bob", "Charlie"]
for student in students:
    print("Hello,", student)

# Break and Continue
for i in range(1, 10):
    if i == 5:
        break   # stops loop completely
    if i == 3:
        continue  # skips this iteration
    print(i)
