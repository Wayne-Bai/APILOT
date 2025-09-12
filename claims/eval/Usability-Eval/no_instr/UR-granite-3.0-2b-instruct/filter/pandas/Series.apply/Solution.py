import pandas as pd

# Create a sample Series
s = pd.Series([1, 2, 3, 4, 5])

# Define a function to invoke on values
def invoke_function(x):
    return x * 2

# Apply the function to the Series
s = s.apply(invoke_function)

# Print the resulting Series
print(s)
