import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'Group': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Value': [10, 20, 30, 40, 50, 60]
})

# Compute the minimum value of each group
min_values = df.groupby('Group')['Value'].min()

# Print the results
print(min_values)
