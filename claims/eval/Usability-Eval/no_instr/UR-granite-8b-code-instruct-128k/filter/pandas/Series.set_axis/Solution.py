import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Assign a desired index to the rows
df.index = ['a', 'b', 'c']

# Print the updated DataFrame
print(df)
