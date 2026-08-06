# Conditional Statements Practice

# Example 1: Simple if-elif-else
score = int(input("Enter your exam score: "))

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

# Example 2: Nested if
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
    if age >= 60:
        print("You are also eligible for senior citizen benefits.")
else:
    print("You are not eligible to vote yet.")


#Practice Programs

# #write a program to check whether a given number is positive or negative
def positive_and_negative(num):
    if (num>=0):
        print(f"{num} is a positive number")
    else:
        print(f"{num} is a negative number.")
num=int(input("Enter a number:"))
positive_and_negative(num)

# #write a program to check whether a person can vote 
def vote(age):
    if(age>=18):
        print("Yes, You can vote")
    else:
        print("No, you can't vote")
age=int(input("Enter a age to check whether a you are eligible for voting or not:\n"))
vote(age)

# #write a program to find the largest of two numbers
def Largest(num1,num2,num3):
    if(num1 >  num2 and num3):
        print(f"{num1} is greater than {num2} and {num3}")
    elif(num2 > num1 and num3):
        print(f"{num2} is greater than {num1} and {num3}")
    elif(num3 > num1 and num2):
        print(f"{num3} is greater than {num1} and {num2}")
    else:
        print("ALL Three numbers are same")
num1=int(input("Enter a number1:\n"))
num2=int(input("Enter a number2:\n"))
num3=int(input("Enter a number3:\n"))
Largest(num1,num2,num3)

# #write a program to check whether a given year is leap year or not
def check_leap_year_is_not(year):
    # Program to check if a year is a leap year
    # Leap year conditions:
    # 1. Divisible by 4
    # 2. Not divisible by 100, unless also divisible by 400
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
       print(year, "is a leap year.")
    else:
       print(year, "is not a leap year.")
year = int(input("Enter a year: "))
check_leap_year_is_not(year)

# #write a program to check whether a character is vowel or consonant.
def vowel_consonant(char):
    vowels=['a','e','i','o','u']
    if len(char) != 1:
       print("Please enter only one character.")
       return
    if (char in vowels):
        print(f"{char} is vowel")
    else:
        print(f"{char} is consonant")
char=input("Enter a character:\n")
char=char.lower()
vowel_consonant(char)

# #write a program to calculate grade based on marks
def grade(marks):
    if(marks>=85):
        print("A grade")
    elif(marks>=75 and marks<85):
        print("B grade")
    elif(marks>=65 and marks<75):
        print("C grade")
    else:
        print("Fail")
marks=int(input("Enter a marks"))
grade(marks)