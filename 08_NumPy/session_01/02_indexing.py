# 08_NumPy/02_indexing.py
# NumPy Indexing & Slicing

import numpy as np

# 1D Array indexing
arr1 = np.array([10, 20, 30, 40, 50])
print("Original 1D Array:", arr1)

# Single element access
print("Element at index 0:", arr1[0])
print("Element at index 3:", arr1[3])

# Slicing
print("Slice arr1[1:4]:", arr1[1:4])
print("Slice arr1[:3]:", arr1[:3])
print("Slice arr1[2:]:", arr1[2:])

# Negative indexing
print("Last element:", arr1[-1])
print("Second last element:", arr1[-2])

# Step slicing
print("Every second element:", arr1[::2])
print("Reverse array:", arr1[::-1])

# 2D Array indexing
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print("\nOriginal 2D Array:\n", arr2)

# Row access
print("First row:", arr2[0])
print("Second row:", arr2[1])

# Column access
print("First column:", arr2[:, 0])
print("Last column:", arr2[:, -1])

# Specific element
print("Element at row 2, col 3:", arr2[1, 2])

# Rectangular section
print("Subarray arr2[0:2, 1:3]:\n", arr2[0:2, 1:3])

# Boolean indexing
mask = arr2 > 4
print("Boolean mask:\n", mask)
print("Filtered values:", arr2[mask])
