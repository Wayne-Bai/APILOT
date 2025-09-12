import pandas as pd

# Create a sample series
data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Define a function to apply
def double(x):
    return x * 2

# Apply the function to the series
result = data.apply(double)

print(result)
