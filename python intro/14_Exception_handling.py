try:  #try block contains code that may raise an exception
    #Ask the user for two numbers
    num1=int(input("Enter a number 1:\n"))
    num2=int(input("Enter a number 2:\n"))
    #divide the first number by second.
    print(num1/num2)
#except block handles the exception so the program does not crash.
except ZeroDivisionError: #
    print("cannot divisible by zero.")
except ValueError:
    print("please enter a valid number.")
else:  #else block runs only if no exception occurs.
    print("Program Executed Successfully.")
finally: #finally block always executes, whether an exception occurs or not.
    print("Program finished. ")

