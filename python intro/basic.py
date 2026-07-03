# #day 1 practice session
# print("Hello, Nouman!")
# print("Welcome to Python Programming")
# print(100)
# print(2+5)
# # print("I want to become a Data Engineer")
# name="Nouman"
# age=20
# City="Bangalore"
# print(name)
# print(age)
# print(City)
# int 
# age=20
# print(type(age))
# #float
# salary=50000.50
# print(type(salary))
# #string
# name="Nouman"    
# print(type(name))
# #boolean
# is_adult=True   
# print(type(is_adult))
# #list
# fruits=["apple","banana","mango"]
# print(type(fruits))
# #dictionary
# person={"name":"Nouman","age":20,"city":"Bangalore"}
# print(type(person))
# #tuple
# coordinates=(10.0,20.0)
# print(type(coordinates))
# #set
# unique_numbers={1,2,3,4,5}
# print(type(unique_numbers))
# #none
# value=None
# print(type(value))
##Day 2 practice session
#operators
#Arithmetic operators
# a= 10
# b=5
# print("Addition:",a+b)
# print("Subtraction:",a-b)
# print("Multiplication:",a*b)
# print("Division:",a/b)
# print("Modulus:",a%b)
# print("Exponentiation:",a**b)
#Assignments operators
# a+=15
# b-=3
# c=10
# c*=2
# d=20
# d/=4
# print("a:",a)
# print("b:",b)       
# print("c:",c)
# print("d:",d)
#Comparison operators
# a=10
# b=5
# print("Equal to:",a==b)
# c=10
# print("Not equal to:",a!=c)
# print("Greater than:",a>b)
# print("Less than:",a<b)
# print("Greater than or equal to:",a>=b)
# print("Less than or equal to:",a<=b)
#Logical operators
# a= True
# b= False
# print("a and b:",a and b)
# print("a or b:",a or b)
# print("not a:",not a)
# c= 0
# b= 1
# print("c and b:",c and b)
# print("c or b:",c or b)
# print("not c:",not c)
#Membership operttors
# name="Python"
# print("y" in name)
# print("z" not in name)  
# print("x" in name)

#Identity Operators
# a=10
# b=10    
# print("a is b:",a is b)
# print("a is not b:",a is not b)

#Input Functions
# name=input("Enter your name:\n")
# print(f"Hello, Myself {name}! Welcome To Python Training Session")
# # age=input("Enter your age:\n")
# # age=int(age)
# #Or we can directly convert the input to integer in one line
# age=int(input("Enter Your Age:\n"))
# print(f"You are {age} years old.")

# #Output Functions
# name="Nouman"
# age=20
# print("Hello, Myself",name,"! Welcome To Python Training Session")
# print(f"You are {age} years old.")
# print("Hello, Myself {}! Welcome To Python Training Session".format(name))
# print("You are {} years old.".format(age))

#Write a program to take two numbers as input from the user and print their sum, difference, product, and quotient.
# num1=int(input("Enter First Number:\n"))
# num2=int(input("Enter Second Number:\n"))
# print(f"Sum of {num1} and {num2} is: {num1+num2}")
# print(f"Differnce of {num1} and {num2} is : {num1-num2}")
# print(f"Product of {num1} and {num2} is: {num1*num2}")
# #write a program to take a name, age from the user and print a message using f-string and format method.
# name=input("enter the name:\n")
# age=int(input("Enter the age:\n"))
# print(f" Hello, Myself {name}! Welcome to Python Practce session.\n I am {age} Years Old.")
# #Write a Program to find  area of a rectangle,length, breadth from the user and print the area.
# Length=float(input("Enter the length of the rectangle:\n"))
# Breadth=float(input("Enter the breadth of the rectangle:\n"))
# Area_of_rectangle=Length*Breadth
# print(f"The Area of Rectangle with {Length} and {Breadth} is: {Area_of_rectangle}")
# #Write a Program to find area of circle, take radius from the user and print the area.
# radius=float(input("Enter the radius of the circle:\n"))
# area=3.14*radius**2
# print(f"The Area of the circle with Radius {radius} is : {area}")
# #Write a Program to swap two numbers, take two numbers from the user and swap them without using a third variable.
# num1=int(input("Enter First Number:\n"))
# num2=int(input("Enter Second Number:\n"))
# print(f"Before Swapping: num1={num1}, num2={num2}")
# num1=num1+num2
# num2=num1-num2
# num1=num1-num2
# print(f"After Swapping: num1={num1}, num2={num2}")
# #write a program to convert temperature from Celsius to Fahrenheit, take temperature in Celsius from the user and print the temperature in Fahrenheit.
# celsius=float(input("Enter the temperature in celcius:\n"))
# fahrenheit=(celsius*9/5)+32
# print(f"The temperature in fahrenheit is:{fahrenheit}")
#writ a program to take marks of 5 subjects from the user and print the total marks, average marks and percentage.
# mark=[]
# for i in range(5):
#     marks=int(input(f"Enter the marks of the subject {i+1}:\n"))
#     mark.append(marks)
# total_marks=sum(mark)
# average=total_marks/5
# percentage=total_marks/500*100
# print(f"Total Marks: {total_marks}\n")
# print(f"Average marks: {average}\n")
# print(f"Percentage: {percentage}\n")
# #write a program to take a salary from user and increase it by 10% and tax of 2% and print the new salary.
# salary=float(input("Enter your salary:\n"))
# salary_after_increase= salary+(salary*10/100)
# salary_after_tax=salary_after_increase-(salary_after_increase*2/100)
# print(f"Your Salary after 10% increase and 2% tax is : {salary_after_tax}")
# a=15
# b=4
# print(a//b)
# print(a%b)
#practice programs
#write a program to take a user first name and last name and display using concatenation and f-string.
# first_name=input("enter the users first name:\n")
# last_name=input("enter the users last name:\n")
# print("HELLO, Myself " + first_name + " " + last_name + "! Welcome to Python Practice Session.")
# print(f"This is Done using f-string:\n Hello, Myself {first_name} {last_name}! Welcome to python practice session.")
#write a program to take a name and age from the user and display a message using f-string and format method.
# name=input("Enter the name:\n")
# age=int(input("enter the age:\n"))
# print(f"Hello, Myself {name}! Welcome to python practice session and I am {age} years old.")
# print("This is done using format method : \n Hello, Myself {}! Welcome to python practice session and I am {} years old.".format(name, age))
# #write a program to convert name to uppercase and make a sentence to lowercase and print the length of the sentence.
# name=input("enter the name: \n")
# sentence=input("enter the sentence:\n")
# uppercase_name=name.upper()
# lowercase_senstence=sentence.lower()
# print(f"Uppercase Name: {uppercase_name}\nLowercase_Sentence: {lowercase_senstence}\nLength of the sentence: {len(lowercase_senstence)}")
# #write a program to fetch first and last character of a string and print them.
# c1=input("enter the character:\n")
# print(f"First Character: {c1[0]}\nLast Character: {c1[-1]}")
# #write a program to take a sentense and remove extra spaces from the sentense using strip() method.
# sentence=input("Enter the sentence:\n")
# sentence_without_space=sentence.strip()
# print(f"Sentence without extra spaces:\n{sentence_without_space}")
#write a program to create a student profile 
# print("-----------Student Profile-----------")
# Name=input("Enter the name of the Student: ")
# Age=int(input("Enter the age of the student: "))
# Course=int(input("Enter the course of the student:\n1. Data Science\n2. Web Development\n3. Machine Learning\n4. Artificial Intelligence\n5. Cloud Computing\n6. Cyber Security\n7. DevOps\n8. Mobile App Development\n9. UI/UX Design\n10. Blockchain Development\n"))
# Dream_job=input("Enter the dream job of the student: ")
# print(f"Student Name: {Name}")
# print(f"Student Age: {Age}")
# print(f"Student Course: {Course}")
# print(f"Student Dream Job: {Dream_job}")
# print("-----------End of Student Profile-----------")
#write a program to create a function to print your name and age.
def name_and_age(name, age):
    print(f"Hello, Myself {name} and I am {age} years old.")
name=input("Enter your name: ")
age=int(input("Enter your age: "))
name_and_age(name, age)