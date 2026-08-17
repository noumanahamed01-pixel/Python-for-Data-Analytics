import numpy as np

sales = np.array([
    12000, 28000, 35000,
    45000, 52000, 67000,
    19000, 75000, 31000
])
high_sales = sales[sales >= 30000]
print(high_sales)
print(high_sales.sum())
print(high_sales.mean()) 
bonus_sales = np.where(sales >= 30000,sales * 1.10,sales)
print(bonus_sales)
print(bonus_sales.max())