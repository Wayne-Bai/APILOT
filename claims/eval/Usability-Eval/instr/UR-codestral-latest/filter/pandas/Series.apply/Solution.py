import pandas as pd

# Let's assume we have the following Series
data = pd.Series([1, 2, 3, 4, 5])

# Define a custom function
def square(x):
    return x ** 2

# Apply the custom function to each element of the Series
squared_data = data.apply(square)

print(squared_data)
