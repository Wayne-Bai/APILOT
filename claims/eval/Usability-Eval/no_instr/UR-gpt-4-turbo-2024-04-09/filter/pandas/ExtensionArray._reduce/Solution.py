import pandas as pd

# Creating a sample DataFrame
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Performing a reduction operation (example: sum)
scalar_result = df['A'].sum()  # Sum of column A
scalar_result
