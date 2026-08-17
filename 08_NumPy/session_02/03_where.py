# where : to create a new value based on conditions as we used in python by list comprehension ["high" if x > 30000 else "low" for x in sales].
import numpy as np
sales = np.array([12000, 45000, 18000, 67000, 25000, 90000])
category = (np.where(
    sales >= 50000,    # condition 1
    "High",            # true
    np.where(          # false → check another condition
        sales >= 25000,
        "Medium",
        "Low"
    )
))
print(category)

sales = np.array([12000, 28000, 35000, 45000, 52000, 67000, 19000])
bonus_sales = np.where(sales >= 50000,sales*1.10,sales*1.05)
print(bonus_sales)