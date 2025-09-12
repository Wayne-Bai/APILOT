import pandas as pd

# Create a sample DataFrame with groups and values
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 12, None, 15, 18, None, 22, 24, 26]
}
df = pd.DataFrame(data)

# Group by 'Group' and compute the standard error of the mean, excluding missing values
grouped_df = df.groupby('Group')['Value'].apply(lambda x: x.dropna().std() / (1 - x.dropna().isnull().mean()))

# Print the result
print(grouped_df)
