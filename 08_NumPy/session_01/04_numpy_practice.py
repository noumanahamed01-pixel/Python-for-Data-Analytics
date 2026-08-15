# Question 1/10: NumPy array + vectorized operation
# You have:
# sales = [10000, 20000, 30000, 40000, 50000]
# Using NumPy:
# Convert sales into a NumPy array.
# Increase every sale by 15% using vectorized arithmetic.
# Print the resulting array.
# Expected:
# [11500. 23000. 34500. 46000. 57500.]
# Write the complete code yourself.
import numpy as np
sales = np.array([10000,20000,30000,40000,50000])
increased_sales = sales + sales * 15/100
print(increased_sales)

# Question 2/10 — Array properties
# Given:
# sales = np.array([
#     [12000, 15000, 18000],
#     [22000, 25000, 28000],
#     [32000, 35000, 38000]
# ])
# Write code to print:
# The shape
# The number of dimensions
# The data type
# Expected shape:
# (3, 3)
# Expected dimensions:
# 2
# Use NumPy properties, not manual counting.
sales = np.array([
    [12000, 15000, 18000],
    [22000, 25000, 28000],
    [32000, 35000, 38000]
])
print(sales.shape)
print(sales.ndim)
print(sales.dtype)

# Question 3/10 — Indexing + slicing
# Using the same array:
# sales = np.array([
#     [12000, 15000, 18000],
#     [22000, 25000, 28000],
#     [32000, 35000, 38000]
# ])
# Write code to print:
# 28000
# The second row
# The first two columns
# The bottom-right 2×2 section
# Expected:
# 28000
# [22000 25000 28000]
# [[12000 15000]
#  [22000 25000]
#  [32000 35000]]
# [[25000 28000]
#  [35000 38000]]
sales = np.array([
    [12000, 15000, 18000],
    [22000, 25000, 28000],
    [32000, 35000, 38000]
])
print(sales[1,2])
print(sales[1,:])
print(sales[0:3,:2])
print(sales[1:3,1:3])

# Question 4/10 — Aggregation
# Given:
# sales = np.array([12000, 45000, 18000, 67000, 25000, 90000])
# Using NumPy methods, calculate and print:
# Total sales
# Average sales
# Minimum sale
# Maximum sale
# Expected:
# 257000
# 42833.333333333336
# 12000
# 90000
# Use .sum(), .mean(), .min(), and .max().
# No built-in Python functions.
sales = np.array([12000, 45000, 18000, 67000, 25000, 90000])
print(sales.sum())
print(sales.mean())
print(sales.min())
print(sales.max())

# Question 5/10 — Boolean masking
# Given:
# sales = np.array([12000, 45000, 18000, 67000, 25000, 90000])
# Create a new NumPy array containing only sales greater than 30,000, then print:
# The filtered sales
# The total of those filtered sales
# Expected:
# [45000 67000 90000]
# 202000
# Use Boolean masking and a NumPy aggregation method.
# No list comprehensions.
sales = np.array([12000, 45000, 18000, 67000, 25000, 90000])
high_sales = sales[sales > 30000]
print(high_sales)
print(high_sales.sum())

# Question 6/10 — Multiple Boolean conditions
# Given:
# transactions = np.array([500, 1500, 2500, 3000, 4500, 6000])
# Find all transactions that are:
# greater than or equal to 2,000 AND less than or equal to 5,000.
# Then print:
# The filtered transactions
# Their total using a NumPy method
# Expected:
# [2500 3000 4500]
# 10000
# Use Boolean masking with &.
# No loops or list comprehensions.
transactions = np.array([500, 1500, 2500, 3000, 4500, 6000])
high_transaction = transactions[(transactions >= 2000) & (transactions <= 5000)]
print(high_transaction)
print(high_transaction.sum())

# Question 7/10 — Slicing
# Given:
# sales = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000])
# Print:
# The first 4 values
# The last 3 values
# Every second value starting from the first value
# Values from index 2 through index 5, with index 5 excluded
# Expected:
# [10000 20000 30000 40000]
# [50000 60000 70000]
# [10000 30000 50000 70000]
# [30000 40000 50000]
# Use NumPy slicing only.
sales = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000])
print(sales[1:4])
print(sales[4:])
print(sales[::2])
print(sales[2:5])

# Question 8/10 — 2D array slicing
# Given:
# sales = np.array([
#     [10000, 12000, 14000],
#     [20000, 22000, 24000],
#     [30000, 32000, 34000],
#     [40000, 42000, 44000]
# ])
# Print:
# The last two rows
# The first two columns
# The bottom-right 2×2 section
# Expected:
# [[30000 32000 34000]
#  [40000 42000 44000]]
# [[10000 12000]
#  [20000 22000]
#  [30000 32000]
#  [40000 42000]]
# [[32000 34000]
#  [42000 44000]]
# Use 2D slicing only. No loops.
sales = np.array([
    [10000, 12000, 14000],
    [20000, 22000, 24000],
    [30000, 32000, 34000],
    [40000, 42000, 44000]
])
print("\n")
print(sales[2:,0:3])
print(sales[:,0:2])
print(sales[2:,1:])

# Question 9/10 — Combined NumPy analysis
# Now we're moving beyond isolated syntax.
# You have transaction data:
# transactions = np.array([
#     1200, 3500, 1800, 4200, 5000,
#     750,  2800, 6100, 1500, 3900
# ])
# The business wants to analyze medium-to-high transactions.
# Your tasks
# Find transactions greater than or equal to 2,000.
# Find their total.
# Find their average.
# Use:
# Boolean masking
# NumPy .sum()
# NumPy .mean()
# Expected results
# [3500 4200 5000 2800 6100 3900]
# 25500
# 4250.0
# Write the complete code yourself. 
# This is where we're checking whether you can combine the pieces instead of solving each concept in isolation
transactions = np.array([
    1200, 3500, 1800, 4200, 5000,
    750,  2800, 6100, 1500, 3900
])
high_transaction = transactions[transactions >= 2000]
print(high_transaction)
print(high_transaction.sum())
print(high_transaction.mean())

# Question 10/10 — Final Challenge
# This one combines 2D arrays + Boolean masking + aggregation.
# You have monthly sales for three products:
# sales = np.array([
#     [12000, 18000, 25000],
#     [22000, 15000, 30000],
#     [35000, 28000, 42000],
#     [18000, 32000, 38000]
# ])
# Each row = month.
# Each column = product.
# The company wants to know about all sales values greater than 25,000.
# Your tasks
# Find all sales values greater than 25000.
# Calculate their total.
# Calculate their average.
# Calculate the maximum value.
# Use NumPy, not loops.
# Expected values
# [30000 35000 28000 42000 32000 38000]
# Total:
# 205000
# Average:
# 34166.666666666664
# Maximum:
# 42000
# This is the final question. Take your time and write the complete code.
sales = np.array([
    [12000, 18000, 25000],
    [22000, 15000, 30000],
    [35000, 28000, 42000],
    [18000, 32000, 38000]
])
high_sales = sales[sales > 25000]
print(high_sales)
print(high_sales.sum())
print(high_sales.mean())
print(high_sales.max())