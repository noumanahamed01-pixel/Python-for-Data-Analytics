# 08_NumPy/03_broadcasting.py
# NumPy Broadcasting Examples

import numpy as np

# 1. Simple broadcasting with scalar
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)
print("Add 10 to each element:", arr + 10)
print("Multiply each element by 2:", arr * 2)

# 2. Broadcasting with arrays of different shapes
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\n2D Array:\n", arr2)

# Add a 1D array to each row
row_add = np.array([10, 20, 30])
print("Add row vector:\n", arr2 + row_add)

# Add a column vector to each column
col_add = np.array([[100],
                    [200]])
print("Add column vector:\n", arr2 + col_add)

# 3. Broadcasting in arithmetic
arr3 = np.arange(12).reshape(3, 4)
print("\n3x4 Array:\n", arr3)

# Subtract a 1D array (length 4) from each row
subtract_vec = np.array([1, 2, 3, 4])
print("Subtract vector from each row:\n", arr3 - subtract_vec)

# 4. Broadcasting with different dimensions
arr4 = np.array([1, 2, 3])
arr5 = np.array([[10], [20], [30]])
print("\nBroadcasting arr4 and arr5:\n", arr4 + arr5)

# 5. Practical example: normalize rows
data = np.array([[10, 20, 30],
                 [40, 50, 60]])
row_means = data.mean(axis=1).reshape(-1, 1)  # reshape for broadcasting
print("\nRow means:\n", row_means)
print("Normalized data (row-wise):\n", data - row_means)