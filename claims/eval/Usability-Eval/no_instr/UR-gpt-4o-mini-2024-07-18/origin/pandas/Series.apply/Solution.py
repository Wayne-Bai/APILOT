import pandas as pd

# Sample data
data = pd.Series([1, 2, 3, 4, 5])

# Define a function to be applied
def square(x):
    return x ** 2

# Invoke the function on values of the Series
result = data.apply(square)

print(result)
