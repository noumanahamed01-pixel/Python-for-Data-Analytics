# File Handling - Read File Example
# Modes:

        # "r" → read

        # "w" → write

        # "a" → append

        # "r+" → read + write

# open() → opens file, must be closed with .close().

# with open() → automatically closes file (recommended).

# .read() → reads entire file.

# .readlines() → returns list of lines.

# Looping → iterate line by line.

# Open file in read mode
file = open("sample.txt", "r")

# Read entire content
content = file.read()
print("File Content:\n", content)

# Close the file
file.close()

# Reading line by line
file = open("sample.txt", "r")
for line in file:
    print("Line:", line.strip())
file.close()

# Using 'with' (better practice, auto-closes file)
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("Lines as list:", lines)
