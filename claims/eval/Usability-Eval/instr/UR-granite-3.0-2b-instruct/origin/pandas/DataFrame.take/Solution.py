import pandas as pd

# Assuming df is your DataFrame and indices are a list of positions
indices = [0, 2, 4]

# Use the DataFrame's loc function to return elements at the given indices
result = df.loc[indices]

# Print the result
print(result)
