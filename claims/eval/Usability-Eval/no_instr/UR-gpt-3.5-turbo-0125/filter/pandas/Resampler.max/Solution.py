
import pandas as pd

# Create a sample DataFrame
data = {'Category': ['A', 'A', 'B', 'B', 'B', 'C'],
        'Values': [10, 20, 30, 40, 50, 60]}
df = pd.DataFrame(data)

# Compute max value of each group
max_values = df.groupby('Category')['Values'].max()
print(max_values)
