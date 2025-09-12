import pandas as pd

# Create a sample Series
data = pd.Series([1, 2, 3, 4, 5])

# Define a function to apply to each value in the Series
def square(x):
    return x ** 2

# Apply the function to the Series
result = data.apply(square)

print(result)
