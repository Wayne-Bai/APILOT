
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Perform a reduction operation (e.g., sum) on a column
result = df['A'].sum()

# Print the result
print(result)
