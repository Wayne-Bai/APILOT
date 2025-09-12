# Import necessary libraries
import pandas as pd

# Create a sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 12, None, 18, 20, 22]
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Compute standard deviation of groups, excluding missing values
std_dev = df.groupby('Group')['Value'].std(skipna=True)

# Print the result
print("\nStandard Deviation of Groups (excluding missing values):")
print(std_dev)
