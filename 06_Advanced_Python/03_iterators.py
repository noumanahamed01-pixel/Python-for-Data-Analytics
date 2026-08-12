# Iterators are objects that let you traverse through elements one at a time, using the __iter__() and __next__() methods.
# Simple iterator using iter() and next()
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30
# print(next(iterator))  # Error: StopIteration

# Custom iterator class
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

# Using custom iterator
for num in CountDown(5):
    print(num)


# Python Iterators

# An iterator is an object that gives you values one at a time, rather than giving you the whole collection at once.

# Think of it like a queue:

# [1000, 2000, 1500, 3000]
#        ↓
#    iterator
#        ↓
# 1000 → 2000 → 1500 → 3000

# Python uses two important functions:

# iter() → creates an iterator
# next() → gets the next value
# Basic example

sales = [1000, 2000, 3000]

sales_iterator = iter(sales)

print(next(sales_iterator))
print(next(sales_iterator))
print(next(sales_iterator))

# Output:
# 1000
# 2000
# 3000

# Notice what happens:

# next() #1 → 1000
# next() #2 → 2000
# next() #3 → 3000

# Python remembers where it stopped.

# If you try:

# print(next(sales_iterator))

# again, you'll get:

# StopIteration

# because there are no more values.

# Why does this matter?

# This becomes important when you're dealing with large amounts of data.

# Imagine a file containing:

# 10 million transactions

# You don't necessarily want to load all 10 million records into memory at once.

# An iterator can give you:

# transaction 1
# ↓
# process it
# ↓
# transaction 2
# ↓
# process it
# ↓
# transaction 3
# ...

# rather than creating another giant list containing everything.

# That's one of the reasons Python uses iterators heavily.

# One important distinction

# A list is an iterable:

sales = [1000, 2000, 3000]

# An iterator is what keeps track of the current position:

sales_iterator = iter(sales)

# So:

# Iterable → can produce an iterator
# Iterator → produces the next value with next()

# We'll go deeper into for loops internally, 
# because a for loop is actually using the iterator mechanism under the hood. That's the part that makes iterators click.


# Create a Countdown iterator that produces:
# 5
# 4
# 3
# 2
# 1
# Hint:
# Start with self.current = 5
# __next__() should return the current number
# Decrease it by 1
# When it goes below 1, raise StopIteration
class CountDown_iterators:
    def __init__(self):
        self.current = 5
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
Countdown_iterator = CountDown_iterators()
print(next(Countdown_iterator))  # 5
print(next(Countdown_iterator))  # 4
print(next(Countdown_iterator))  # 3    
print(next(Countdown_iterator))  # 2
print(next(Countdown_iterator))  # 1

def sales_iterator(sales):
    for i in sales:
        yield i
sales=[10000,25000,40000,55000]
sales_iterator=sales_iterator(sales)
print(next(sales_iterator))
print(next(sales_iterator))
print(next(sales_iterator))
print(next(sales_iterator))