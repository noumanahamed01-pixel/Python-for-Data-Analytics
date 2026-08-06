# Tuples Practice

# Creating a tuple
coordinates = (10, 20, 30)
student_info = ("M", "BCA", "Final")

# Accessing elements
print("First coordinate:", coordinates[0])
print("Last coordinate:", coordinates[-1])
print("Student Name:", student_info[0])

# Slicing
print("First two coordinates:", coordinates[:2])

# Looping through tuple
for value in coordinates:
    print("Coordinate:", value)

# Tuple methods
numbers = (5, 10, 5, 20, 5)
print("Count of 5:", numbers.count(5))
print("Index of 20:", numbers.index(20))

# Nested tuple
nested = (("Alice", 21), ("Bob", 22), ("Charlie", 23))
print("Second student's name:", nested[1][0])
print("Second student's age:", nested[1][1])


# Practice programs
#tuple is ordered,immutable collections in python.

# #1. create a tuple of 5 fruits and print it.
fruits=('apple','mango','pineapple','grapes','orange')
print(fruits)
print(type(fruits))

# # 2. print the first and last elements of a tuple.
fruits=('apple','mango','pineapple','grapes','orange')
print(fruits[0])
print(fruits[-1])

# #3. create a tuple of 5 number and print the third element.
number=(23,54,94,61,78)
print(type(number))
print(number[2])

# #4. find the length of a tuple using len()
number=(23,54,94,61,78)
print(len(number))

# #5. check whether apple exist in the tuple or not
fruits=('apple','mango','pineapple','grapes','orange')
if 'apple' in fruits:
    print("Yes,Apple is in tuple list")
else:
    print("No, Apple is not in the list")

# #6. count how many time a number appear in the tuple.
num=(23,76,54,94,26,54)
print(num.count(54))

# #find the index of banana using index()
fruits=('apple','mango','pineapple','banana','grapes','orange')
print(fruits.index('banana'))

# #8. iterate through a tuple using for loop.
fruits=('apple','mango','pineapple','banana','grapes','orange')
for i in fruits:
    print(i)

# #9. concatenate two tuples.
fruits=('mango','apple','grapes')
new_fruits=('kiwi','avagado')
result=fruits + new_fruits
print(result)

# #create a tuple containing student details(name,age,course) and print each value using indexing.
student=('alice',20,'BCA')
print(student[0])
print(student[1])
print(student[2])