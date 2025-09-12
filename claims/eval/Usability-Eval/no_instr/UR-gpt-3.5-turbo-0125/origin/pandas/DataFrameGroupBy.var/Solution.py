
import pandas as pd

# Create a sample DataFrame
data = {'group': ['A', 'A', 'B', 'B', 'A', 'B'],
        'value': [1, 2, 3, None, 5, 6]}
df = pd.DataFrame(data)

# Compute variance of groups excluding missing values
variance = df.dropna().groupby('group')['value'].var()

print(variance)
