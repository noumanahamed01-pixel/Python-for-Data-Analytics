import numpy as np
sales = np.array([
    #p1     #p2    #p3
    [10000, 15000, 20000], # month_1
    [20000, 25000, 30000], # month_2
    [30000, 35000, 40000]  # month_3
])
# mean, calculate entire average by axis 
print(sales.mean(axis=0))   # average sales by products
print(sales.mean(axis=1))   # average sales by month
# Variance, a measure of how spread out the distribution of data points is
print(sales.var(axis=0))    # computes the variance along a product side
print(sales.var(axis=1))    # computes variance along a month side
# standard deviation, measure how spread out ypur data points are relative to their mean
print(sales.std(axis=0))    # computes standard deviation along product side
print(sales.std(axis=1))    # computes standard deviation along month side 

