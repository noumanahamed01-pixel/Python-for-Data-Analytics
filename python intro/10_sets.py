# A set is an unordered, mutable collection of unique elements.
# Unordered → Elements have no fixed position (no indexing).
# Mutable → You can add or remove elements.
# Unique → Duplicate values are automatically removed.
# #1. create a set of 5 fruits and print it.
# fruits={'mango','apple','grapes','kiwi','orange'}
# print(fruits)
# print(type(fruits))
# #2. create a set with duplicates and print it.
# fruits={'mango','orange','kiwi','apple','mango'}
# print(fruits)
# #3. print the len of set.
# fruits={'mango','orange','kiwi','apple','mango'}
# print(len(fruits))
# print(fruits)
# #4. check whether apple exist in the list.
# fruits={'mango','orange','kiwi','apple','mango'}
# if 'apple' in fruits:
#     print("Yes, Apple is in the set")
# else:
#     print("No, Apple is not is set")
# #create an empty set and print it type.
# x=set()
# print(type(x))
# #6. add a new fruits using add().
# fruits={'mango','orange','kiwi','apple','mango'}
# fruits.add('grapes')
# print(fruits)
# #7. remove a fruits using remove().
# fruits={'mango','orange','kiwi','apple','mango'}
# fruits.remove('apple')
# print(fruits)
# #8. remove a fruits using discard().
# fruits={'mango','orange','kiwi','apple','mango'}
# fruits.discard('mango')
# print(fruits)
# #9. remove a random element using pop().
# fruits={'mango','orange','kiwi','apple','mango'}
# fruits.pop()
# print(fruits)
# #10. clear the set using clear().
# fruits={'mango','orange','kiwi','apple','mango'}
# fruits.clear()
# print(fruits)
# #create two set and find their union.
# num1={1,2,3,6,5,4,7,5,3,4,5,6,5}
# num2={5,3,6,1,9,2,8}
# print(num1.union(num2))
# print(num1.intersection(num2))
# #OR
# print(num1 | num2)
# print(num1 & num2)
# #12. find their differce and symmetric difference.
# num1={1,2,3,6,5,4,7,5,3,4,5,6,5}
# num2={5,3,6,1,9,2,8}
# print(num1-num2)#difference
# print(num1^num2)#symmetric difference.
# #OR
# print(num1.difference(num2))
# print(num1.symmetric_difference(num2))

# #iterate through a set using for loop 
# num2={5,3,6,1,9,2,8}
# for i in num2:
#     print(i)