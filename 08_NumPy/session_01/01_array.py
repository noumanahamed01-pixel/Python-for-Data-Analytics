import numpy as np
sales = np.array([15000, 28000, 42000, 55000, 19000])
print(sales)
print(type(sales))
increased_sales = sales + sales*10/100
print(increased_sales)
 #  ---  ARRAY Properties  ---
print(sales.shape)  # shows the no of elements in dimension as (5,) elements in one dimension
print(sales.ndim)  # shows the no of dimensions
print(sales.dtype)  # This tells you what numerical data type NumPy is storing, such as int64.
#  --- 2D-ARRAY ---
sales = np.array([
    [12000 , 15000,  18000],
    [22000 , 25000 , 28000],
    [32000 , 35000 , 38000]
])
print(sales)
print(sales.shape)
print(sales.ndim)
# --- Indexing in Numpy ---
print(sales[0][0])  # works, but the preferred NumPy style is: sales[0,0]
#      OR
print(sales[0,0])   # Because NumPy directly supports row, column indexing.
print(sales[1][2])
#      OR
print(sales[1,2])
print(sales[1])
print(sales[:,1])
# --- NumPy Aggregation ---
sales = np.array([12000, 45000, 18000, 67000, 25000, 90000])
print(sales.sum())
print(sales.mean())
print(sales.min())
print(sales.max())
# --- Boolean-Indexing or Boolean-Masking ---
sales = np.array([12000, 45000, 18000, 67000, 25000, 90000])
high_sales =  sales[sales > 30000]
print(high_sales)
print(high_sales.sum())
# --- Combining Conditions ---
sales = np.array([12000, 45000, 18000, 67000, 25000, 90000])
high_sales = sales[(sales >=20000) & (sales <= 70000)]
print(high_sales)
print(high_sales.sum())
# --- Slicing ---
sales = np.array([12000, 45000, 18000, 67000, 25000, 90000])
# You now understand the basic slicing pattern:
        # array[start : stop : step]
# And importantly, you correctly remembered that stop is excluded.
print(sales[:3])  # first three
print(sales[3:])  # last three
print(sales[::2])  # every second value
# --- 2D-ARRAY Slicing ---
sales = np.array([
    [12000, 15000, 18000],
    [22000, 25000, 28000],
    [32000, 35000, 38000]
])
print(sales[:2])
print(sales[:,:2])
print(sales[1:3, 1:3])  # Rectangular section from 2D-array

