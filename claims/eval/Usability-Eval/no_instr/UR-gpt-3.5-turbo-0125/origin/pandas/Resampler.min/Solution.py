
import pandas as pd

# Create a sample DataFrame
data = {'Group': ['A', 'A', 'B', 'B', 'C'],
        'Value': [10, 15, 5, 8, 3]}
df = pd.DataFrame(data)

# Compute the minimum value of each group
min_value_per_group = df.groupby('Group')['Value'].min()

print(min_value_per_group)
