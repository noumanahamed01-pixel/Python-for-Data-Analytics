# File Handling - Write File Example

# Writing to a file (overwrites existing content)
file = open("sample.txt", "w")
file.write("Hello M!\n")
file.write("This is your Python file handling practice.\n")
file.write("Writing data into files is easy!\n")
file.close()

print("Data written successfully.")

# Appending to a file (adds content without overwriting)
file = open("sample.txt", "a")
file.write("This line is appended at the end.\n")
file.close()

print("Data appended successfully.")

# Using 'with' (recommended)
with open("sample.txt", "w") as file:
    file.write("Using 'with' ensures file closes automatically.\n")
    file.write("No need to call file.close().\n")
