# These are functional programming tools that work beautifully with lambdas.
from functools import reduce
from unittest import result

# Sample list
numbers = [1, 2, 3, 4, 5, 6]

# map → applies a function to each element
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# filter → keeps only elements that satisfy a condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", evens)

# reduce → applies a function cumulatively to reduce list to a single value
sum_all = reduce(lambda a, b: a + b, numbers)
print("Sum of all numbers:", sum_all)

product_all = reduce(lambda a, b: a * b, numbers)
print("Product of all numbers:", product_all)

#Practice 
#basic transformation using map
def square(x):
    return x**2
number=[1,2,3,4,5]
result=map(square,number)
print(list(result))

#with lambda function using map
doubled=list(map(lambda x:x*2,number))
print(doubled)

#type conversion using map
a=["1","2","3","4"]
result=list(map(int,a))
print(result)

#multiple iterables using map
a=[1,2,3]
b=[4,5,6]
result=list(map(lambda x,y:x+y,a,b))
print(result)

#filter()
#basic filtering
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6]

#filtering strings
names = ["M", "Alice", "Bob", "Mike"]
m_names = list(filter(lambda x: x.startswith("M"), names))
print(m_names)   # ['M', 'Mike']

#with a defined function
def is_positive(n):
    return n > 0
nums = [-5, -1, 0, 3, 7]
positives = list(filter(is_positive, nums))
print(positives)   # [3, 7]

# using opererator.add() more efiicient than lambda function
from functools import reduce
import operator
numbers = [1, 2, 3, 4, 5]
total_sum=reduce(operator.add,numbers)
print(total_sum)


# Use filter() + lambda to keep only sales amounts greater than 25,000.
sales = [12000, 45000, 8000, 67000, 25000, 90000]
print(list(filter(lambda x: x>25000,sales)))


#--------------------reduce() working use example------------------------
# in everyday data analysis, you'd usually use Python's built-in sum(orders) for this simple total. 
# reduce() becomes more interesting when the combination logic is something more specialized. That's why we're learning it—not because it's the best way to calculate a sum.

# you said something specialized what will be that 

# Yeah. "Specialized" means the operation isn't simply sum() or max()—you're combining items according to custom logic.

# For example, imagine you have transaction amounts:

transactions = [100, 200, 50, 300]

# A simple total is:

sum(transactions)

# No reason to use reduce() there.

# But suppose you want to build a cumulative transaction calculation where each new value is processed against the result so far.

# For example, applying successive discounts:

from functools import reduce

prices = [1000, 900, 800]

result = reduce(
    lambda total, price: total + price * 0.9,
    prices,
    0
)

print(result)

# Here the lambda isn't merely "add two numbers"; 
# each incoming value gets transformed before being combined with the accumulated result.

# Another useful example is finding the maximum using custom logic:

from functools import reduce

sales = [45000, 67000, 32000, 90000]

highest = reduce(
    lambda a, b: a if a > b else b,
    sales
)

print(highest)

# Internally:

# 45000 vs 67000 → 67000
# 67000 vs 32000 → 67000
# 67000 vs 90000 → 90000

# So reduce() can express:

# "Take the accumulated result and the next item, apply my rule, and keep the result."

# But here's the important Data Analyst point

# Don't overuse reduce().

# In normal analytics Python, you'll use:

# sum()
# max()
# min()
# sorted()
# comprehensions
# Pandas operations
# far more often than reduce().

# We're learning reduce() because it teaches an important Python concept: accumulation and passing functions around.
# It's useful knowledge, but it shouldn't become your favorite hammer just because we learned the hammer. 😄
from functools import reduce
transactions = [1000, 2000, 1500, 3000]
print(reduce(lambda x,y: x+y,transactions))
