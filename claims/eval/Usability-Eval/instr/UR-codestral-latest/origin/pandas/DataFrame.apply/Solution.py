# Import the necessary library
import pandas as pd

# First, let's create a simple DataFrame as an example
data = {'Column1': [1, 2, 3, 4, 5],
        'Column2': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Now, let's define a custom function that we want to apply
def custom_function(x):
    return x * 2

# Apply the function to each row (axis=1)
df = df.apply(lambda row: custom_function(row), axis=1)

# Print the DataFrame to see the results
print(df)
