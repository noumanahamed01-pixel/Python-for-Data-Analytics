# try block → code that might cause an error.

# except block → runs if an error occurs.

# In this example, if the user types something that isn’t an integer, Python raises a ValueError, and the program handles it gracefully.

# Basic Exception Handling Example
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Error: Please enter a valid integer.")
