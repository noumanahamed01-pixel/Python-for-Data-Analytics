#These two keywords give you more control over how errors are handled and how cleanup is done.

# raise → explicitly triggers an exception (built-in or custom).

# finally → block that always executes, whether an error occurs or not.

# Useful for cleanup tasks (closing files, releasing resources, logging).

# Together, they make programs robust and predictable.

# Example: finally + raise

class InvalidMarksError(Exception):
    def __init__(self, message="Marks must be between 0 and 100"):
        self.message = message
        super().__init__(self.message)

def calculate_grade(marks):
    try:
        if marks < 0 or marks > 100:
            # Raise custom exception
            raise InvalidMarksError()
        elif marks >= 90:
            return "Grade A"
        elif marks >= 75:
            return "Grade B"
        elif marks >= 60:
            return "Grade C"
        else:
            return "Failed"

    except InvalidMarksError as e:
        print("Error:", e)
    finally:
        print("Grade calculation process completed.")  # Always runs

# Demo
print(calculate_grade(95))   # Valid
print("-----")
print(calculate_grade(120))  # Invalid → triggers raise
