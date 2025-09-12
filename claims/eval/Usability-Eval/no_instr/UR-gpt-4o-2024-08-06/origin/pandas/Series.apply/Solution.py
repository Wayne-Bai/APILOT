import pandas as pd

# Create a sample pandas Series
data = pd.Series([1, 2, 3, 4, 5])

# Define a function to be applied on each value of the Series
def square(x):
    return x * x

# Invoke the function on each value in the Series
squared_data = data.apply(square)

# Print the resulting Series
print(squared_data)
