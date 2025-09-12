
import pandas as pd

# Create a sample DataFrame
data = {'Group': ['A', 'A', 'B', 'B', 'B'],
        'Values': [10, 20, 15, 25, 30]}
df = pd.DataFrame(data)

# Compute max value of each group
max_values = df.groupby('Group')['Values'].max()
print(max_values)
