# Real-Workflow Assessment
# Scenario: Regional Sales Analysis

# You're a junior data analyst at a retail company.
# You receive this dataset:

# import numpy as np
# sales = np.array([
#     [12000, 18000, 25000, 32000, 45000],
#     [15000, 22000, 28000, 35000, 52000],
#     [9000,  17000, 31000, 42000, 48000],
#     [20000, 26000, 33000, 39000, 61000]
# ])

# Each row represents a region:
    # Row 0 → North
    # Row 1 → South
    # Row 2 → East
    # Row 3 → West

# Each column represents a month:
    # Column 0 → January
    # Column 1 → February
    # Column 2 → March
    # Column 3 → April
    # Column 4 → May
    # Business request

# The Sales Director asks:
# "I want to understand which regions are performing strongly, how much we're selling overall, and where we should investigate further."

# Task 1: Overall performance
# Calculate:
    # Total sales across all regions and months
    # Overall average sale

# Task 2: Regional performance
    # Calculate the total sales for each region.
    # You should end up with four numbers, one for each region.

# Task 3: Monthly performance
    # Calculate the total sales for each month.
    # You should end up with five numbers, one for each month.

# Task 4: High-value sales
# Find every individual sales value greater than ₹40,000.
# Then calculate:
    # Number of high-value sales
    # Total value of those high-value sales
    # Average of those high-value sales

# Task 5: Regional investigation
    # A region should be flagged for investigation if its total regional sales are below ₹140,000.
    # Create a result identifying which regions meet that condition.

# Task 6: Conditional business transformation
# Management wants to model a hypothetical incentive:
    # Sales ≥ ₹40,000 → increase by 10%
    # Sales < ₹40,000 → increase by 5%
    # Create a new array containing the adjusted sales.
    # Then calculate the new total sales after the hypothetical incentive.

# Final analyst question

# This is the important part.
# Based on your results, write 2–3 sentences answering:

# Which region appears strongest, which region deserves investigation, and what does the monthly trend suggest?

# Don't just dump numbers. Interpret them.
    # Rules
    # Use NumPy.
    # No Pandas.
    # No Python sum(), max(), etc. when NumPy methods can do the job.
    # No manually calculating results.
    # You may use anything we've learned so far.
    # I will not tell you which NumPy function to use.

# This is much closer to the workflow you'll eventually encounter with Pandas.

import numpy as np

sales = np.array([
    [12000, 18000, 25000, 32000, 45000],
    [15000, 22000, 28000, 35000, 52000],
    [9000,  17000, 31000, 42000, 48000],
    [20000, 26000, 33000, 39000, 61000]
])
# Task 1
print(sales.sum())    # total sales across all region and months
print(sales.mean())    # overall average sale

# Task 2
print(sales.sum(axis=1))   # sales by regional wise 
# Task 3
print(sales.sum(axis=0))   # sales by monthly wise
# Task 4
high_sales = sales[sales > 40000]
print(high_sales.size)
print(high_sales.sum())
print(high_sales.mean())
# Task 5
region = np.where(sales.sum(axis=1) < 140000,'Need to Investigate here','good')
print(region)
#Task 6
adjusted_sales = np.where(sales >= 40000,sales * 1.10,sales * 1.05)
print(adjusted_sales)
print(adjusted_sales.sum())
