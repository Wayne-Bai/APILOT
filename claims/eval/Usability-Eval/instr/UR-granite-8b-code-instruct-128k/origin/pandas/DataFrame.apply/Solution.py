
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Define a function to apply along the rows (axis=0)
def add_one(row):
    return row + 1

# Apply the function to each row of the DataFrame
result = df.apply(add_one, axis=0)

# Print the result
print(result)
