
import pandas as pd

# Define a function to apply to each element in the DataFrame
def my_function(x):
    return x ** 2

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Apply the function to each element in the DataFrame
result = df.apply(my_function)
