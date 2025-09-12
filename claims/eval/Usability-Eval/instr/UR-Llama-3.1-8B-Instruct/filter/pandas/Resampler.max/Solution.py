import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Value': np.random.randint(1, 100, 9)
}
df = pd.DataFrame(data)

# Group by 'Group' and compute max value
max_values = df.groupby('Group')['Value'].max()

print(max_values)
