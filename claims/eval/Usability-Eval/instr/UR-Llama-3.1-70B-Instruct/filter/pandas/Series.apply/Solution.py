# Import the pandas library
import pandas as pd
import numpy as np

# Create a sample series
series = pd.Series([1, 2, 3, 4, 5])

# Define a function to apply on series
def square_values(x):
    return x ** 2

# Apply function using map function
result_map = series.map(square_values)

# Apply function using lambda function and map function
result_lambda_map = series.map(lambda x: x ** 2)

# Apply function using list comprehension
result_list_comp = pd.Series([x ** 2 for x in series])

# Apply function using vectorized operations (recommended for performance)
result_vectorized = series ** 2

# Print the results
print("Original Series:")
print(series)

print("\nResult using map function:")
print(result_map)

print("\nResult using map function with lambda:")
print(result_lambda_map)

print("\nResult using list comprehension:")
print(result_list_comp)

print("\nResult using vectorized operation:")
print(result_vectorized)
