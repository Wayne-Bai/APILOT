import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)

# Compute prod of group values
group_prod = df.groupby('Group')['Value'].transform(np.prod)

# Print the result
print(group_prod)
