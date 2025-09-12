
import pandas as pd

# Create a DataFrame
data = {'Group': ['A', 'A', 'B', 'B'],
        'Value': [10, 20, 15, 25]}
df = pd.DataFrame(data)

# Compute min value of each group
min_values = df.groupby('Group')['Value'].min()
print(min_values)
