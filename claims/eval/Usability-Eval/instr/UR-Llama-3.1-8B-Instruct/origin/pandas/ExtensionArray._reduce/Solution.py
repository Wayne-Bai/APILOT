import pandas as pd
import numpy as np

# Create a simple DataFrame
data = {'Name': ['Tom', 'Nick', 'John'],
        'Age': [20, 21, 19]}
df = pd.DataFrame(data)

# Apply reduction operation using pandas Series functions
print("Sum of Age:", df['Age'].sum())
print("Mean of Age:", df['Age'].mean())
print("Median of Age:", df['Age'].median())
print("Mode of Age:", df['Age'].mode().values[0])
print("Standard Deviation of Age:", df['Age'].std())
print("Variance of Age:", df['Age'].var())

# Perform element-wise operations using pd.Series.apply
series = pd.Series([1, 2, 3, 4, 5])
def square(x):
    return x**2

squared_series = series.apply(square)
print("Squared series:", squared_series)

# Apply custom reduction operation using reduce function from functools
import functools
def multiply(a, b):
    return a * b

product = functools.reduce(multiply, series.values)
print("Product of series:", product)
