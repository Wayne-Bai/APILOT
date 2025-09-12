import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
    'Group': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Value': [1, 2, 3, 4, 5, 6]
})

# Group the data by 'Group' and calculate the 75th percentile of 'Value'
quantile_value = df.groupby('Group')['Value'].quantile(0.75)

print(quantile_value)
