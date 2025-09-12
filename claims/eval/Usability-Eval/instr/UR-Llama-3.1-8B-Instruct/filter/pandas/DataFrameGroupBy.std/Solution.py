# Import the pandas library
import pandas as pd

# Create a sample DataFrame
data = {'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
        'Value': [10, 15, 8, 12, 18, pd.NA, 5, 16, 9]}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Compute standard deviation of groups, excluding missing values
std_dev_groups = df.groupby('Group')['Value'].std(drop=False)

# Print the result
print("\nStandard Deviation of Groups, Excluding Missing Values:")
print(std_dev_groups)
