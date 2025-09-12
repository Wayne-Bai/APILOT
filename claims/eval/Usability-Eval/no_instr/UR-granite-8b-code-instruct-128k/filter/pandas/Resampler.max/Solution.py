
import pandas as pd

# Create a sample DataFrame
data = {'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Value': [10, 20, 15, 25, 30, 40]}
df = pd.DataFrame(data)

# Group the DataFrame by 'Group' and compute the maximum 'Value' for each group
grouped_data = df.groupby('Group')['Value'].max()

# Print the result
print(grouped_data)
