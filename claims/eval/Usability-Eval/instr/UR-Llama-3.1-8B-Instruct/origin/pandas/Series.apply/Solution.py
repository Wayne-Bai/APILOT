# Import the pandas library
import pandas as pd

# Create a sample pandas Series
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# Define a function to be invoked on the values of the Series
def increment_value(x):
    return x + 2

# Use the apply method to invoke the function on the values of the Series
result = s.apply(increment_value)

print(result)
