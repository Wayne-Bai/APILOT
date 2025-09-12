import pandas as pd

# Sample data
data = {
    'Group': ['A', 'A', 'B', 'B', None, 'C', 'C', 'D'],
    'Value': [10, 12, 15, 14, 16, 18, 20, 22]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Remove rows with missing values
df = df.dropna()

# Compute the variance for each group
variance_by_group = df.groupby('Group').var()

print(variance_by_group)
