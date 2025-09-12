import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Performing the reduction operation: calculating the sum of a specific column
result = df['A'].sum()

print(result)
