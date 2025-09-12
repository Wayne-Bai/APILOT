import pandas as pd

# Sample data in a pandas Series
data = pd.Series([1, 2, 3, 4, 5])

# Define a simple function to apply on each element of the Series
def square(x):
    return x ** 2

# Invoke the function on each value of the Series using .map()
result = data.map(square)

print(result)
