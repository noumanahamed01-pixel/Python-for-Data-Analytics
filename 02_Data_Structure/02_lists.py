# Lists Practice

# Creating a list
numbers = [10, 20, 30, 40, 50]
students = ["Alice", "Bob", "Charlie"]

# Accessing elements
print("First number:", numbers[0])
print("Last student:", students[-1])

# Slicing
print("First three numbers:", numbers[:3])
print("Students from index 1 onwards:", students[1:])

# Adding elements
students.append("David")
print("After append:", students)

students.insert(1, "Eve")
print("After insert at index 1:", students)

# Removing elements
students.remove("Charlie")
print("After remove:", students)

removed = students.pop()  # removes last element
print("Removed:", removed)
print("After pop:", students)

# Updating elements
numbers[2] = 99
print("Updated numbers:", numbers)

# Looping through list
for student in students:
    print("Student:", student)

# List functions
print("Length of numbers:", len(numbers))
print("Max number:", max(numbers))
print("Min number:", min(numbers))
print("Sum of numbers:", sum(numbers))

# List comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

#practice programs
# #write a program to create a lists of 5 fruits and print.
fruits=['apple', 'banana', 'cherry', 'mango', 'orange']
print(fruits)
print(type(fruits))
# #write a program to create a lists of 5 students name and print the first and lastname
firstname=['kishan', 'rowdy', 'nouman']
lastname=['kumar', 'rathore', 'ahmed']
print(firstname[0],lastname[0])
print(firstname[1],lastname[1])
print(firstname[2],lastname[2])
# write a program to create a number of lists and print the 3rd one
list=[23,24,12,54,65,34]
print(list[3])
# write a program to create a mixed lists containing int, float, string, and boolean.
list=['sunny',20,'BCA',76.12,True]
print(list)
print(len(list))#prints the length of list using len()
#access every elements of lists using indexing
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
marks=[76,54,87,98,12,87,90,13,21]
print(marks)

#create alist of 5 fruits and add one more using append().
# fruits=['apple','mango','grapes']
# fruits.append('orange')
# print(fruits)
#insert orange at index 2
# fruits.insert(2,'orange')
# print(fruits)
# #extend the list with kwi and pineapple.
# new_fruits=['kiwi','pineapple']
# fruits.extend(new_fruits)
# print(fruits)
#remove mango
# fruits.remove('mango')
# print(fruits)
#remove the last fruit using pop
# fruits.pop(2)
# print(fruits)
#create a list of marks and sort it in the ascending order 
# marks=[34,76,98,23,84,65,52,49]
# # marks.sort()
# print(marks)
# #sort the same list in decending order
# marks.sort(reverse=True)
# print(marks)
# #reverse the list
# r=[1,2,3,4]
# s=['alice','john','sunny']
# r.reverse()
# s.reverse()
# print(r)
# print(s)
#find the index of particular value
# print(marks.index(84))
# #count how many times a value appear.
# marks = [90,80,90,70,90]
# print(marks.count(90))


