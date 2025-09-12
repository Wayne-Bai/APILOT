import pandas as pd

# Define a function to test
def add_one(x):
    return x + 1

# Create a Sample Series
series = pd.Series([1, 2, 3, 4, 5])

# Apply the function to each element in the Series
modified_series = series.apply(add_one)

# Print the result
print(modified_series)
