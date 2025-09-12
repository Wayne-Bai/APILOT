import pandas as pd

# Sample Series
data = pd.Series([1, 2, 3, 4, 5])

# Define a function to apply
def my_function(x):
    return x ** 2

# Invoke the function on the values of the Series
result = data.apply(my_function)

print(result)
