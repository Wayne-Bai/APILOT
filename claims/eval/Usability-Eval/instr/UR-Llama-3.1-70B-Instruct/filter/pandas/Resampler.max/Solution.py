# Import the pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# Compute max value of each group
max_value_by_group = df.groupby('Group')['Value'].transform('max')

# Print the result
print(max_value_by_group)
