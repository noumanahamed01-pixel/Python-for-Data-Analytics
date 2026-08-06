# #Write a Program to find  area of a rectangle,length, breadth from the user and print the area.
Length=float(input("Enter the length of the rectangle:\n"))
Breadth=float(input("Enter the breadth of the rectangle:\n"))
Area_of_rectangle=Length*Breadth
print(f"The Area of Rectangle with {Length} and {Breadth} is: {Area_of_rectangle}")

# #Write a Program to find area of circle, take radius from the user and print the area.
radius=float(input("Enter the radius of the circle:\n"))
area=3.14*radius**2
print(f"The Area of the circle with Radius {radius} is : {area}")

# #Write a Program to swap two numbers, take two numbers from the user and swap them without using a third variable.
num1=int(input("Enter First Number:\n"))
num2=int(input("Enter Second Number:\n"))
print(f"Before Swapping: num1={num1}, num2={num2}")
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f"After Swapping: num1={num1}, num2={num2}")

# #write a program to convert temperature from Celsius to Fahrenheit, take temperature in Celsius from the user and print the temperature in Fahrenheit.
celsius=float(input("Enter the temperature in celcius:\n"))
fahrenheit=(celsius*9/5)+32
print(f"The temperature in fahrenheit is:{fahrenheit}")

#writ a program to take marks of 5 subjects from the user and print the total marks, average marks and percentage.
mark=[]
for i in range(5):
    marks=int(input(f"Enter the marks of the subject {i+1}:\n"))
    mark.append(marks)
total_marks=sum(mark)
average=total_marks/5
percentage=total_marks/500*100
print(f"Total Marks: {total_marks}\n")
print(f"Average marks: {average}\n")
print(f"Percentage: {percentage}\n")

# #write a program to take a salary from user and increase it by 10% and tax of 2% and print the new salary.
salary=float(input("Enter your salary:\n"))
salary_after_increase= salary+(salary*10/100)
salary_after_tax=salary_after_increase-(salary_after_increase*2/100)
print(f"Your Salary after 10% increase and 2% tax is : {salary_after_tax}")


# #write a program to count how many number are divisible by 3 between 1 to 100
count=0
for i in range(1,101):
    if(i % 3 == 0):
        count+=1
print("the numbers divisible by 3 are:",count)

# #write a program to print this pattern
# #1
# #12
# #123
# #1234
# #12345
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()