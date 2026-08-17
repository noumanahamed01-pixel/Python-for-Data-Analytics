import numpy as np
sales = np.array([
    #p1     #p2    #p3
    [10000, 15000, 20000], # month_1
    [20000, 25000, 30000], # month_2
    [30000, 35000, 40000]  # month_3
])
print(sales.sum(axis=0))   # one result per column
print(sales.sum(axis=1))   # one result per row
print(sales.sum(axis=-1))  # axis =-1 is equal to axis=1

# The key idea

# axis is an argument used by many NumPy operations that reduce or aggregate an array.
# NumPy's documentation explicitly supports axis-based operations for things such as sum, mean, min, max, std, var, and more.

 # axis = 0 performs operations vertivally down the columns,
 # while axis = 1 performs operations horizontally across the rows using built-in statistical operatoins in numpy.
print(sales.mean(axis=0))
print(sales.mean(axis=1))

print(sales.min(axis=0))
print(sales.min(axis=1))

print(sales.max(axis=0))
print(sales.max(axis=1))

print(sales.std(axis=0))
print(sales.std(axis=1))

print(sales.var(axis=0))
print(sales.var(axis=1))


