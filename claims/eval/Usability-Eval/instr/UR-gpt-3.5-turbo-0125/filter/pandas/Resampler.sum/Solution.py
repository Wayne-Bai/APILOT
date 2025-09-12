
import pandas as pd

# Create a sample DataFrame
data = {'Group': ['A', 'A', 'B', 'B', 'B'],
        'Values': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Compute sum of group values
group_sum = df.groupby('Group')['Values'].sum()
print(group_sum)
