
import pandas as pd

# Sample data
data = {'Group': ['A', 'A', 'B', 'B', 'B'],
        'Value': [10, 20, 30, 40, 50]}

df = pd.DataFrame(data)

# Compute the product of group values
result = df.groupby('Group')['Value'].prod().reset_index()

print(result)
