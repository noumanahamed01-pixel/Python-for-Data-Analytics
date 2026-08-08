# File Handling - Append Example

# Open file in append mode
file = open("sample.txt", "a")

# Add new content at the end
file.write("This line is added using append mode.\n")
file.write("Appending keeps old data safe.\n")

# Close the file
file.close()

print("Data appended successfully.")

# Verify by reading the file
with open("sample.txt", "r") as file:
    content = file.read()
    print("Updated File Content:\n", content)
