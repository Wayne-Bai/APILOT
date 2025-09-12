import pandas as pd

# Create a Series
s = pd.Series([1, 2, 3, 4, 5])

# Define a custom function
def add_one(x):
    return x + 1

# Apply the function to the values of the Series
result = s.apply(add_one)

# Print the result
print(result)
