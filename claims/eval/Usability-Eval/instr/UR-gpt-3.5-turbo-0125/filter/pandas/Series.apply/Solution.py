
import pandas as pd

# Create a sample Series
data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]}
s = pd.Series(data)

# Define a function to apply on each value of the Series
def custom_function(value):
    return value ** 2

# Apply the custom function on each value of the Series
result = s.apply(custom_function)

print(result)
