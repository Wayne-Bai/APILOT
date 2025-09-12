import pandas as pd

# Assume we have a DataFrame 'df' with groups and values
# df = pd.read_csv('data.csv') # Uncomment to load data from a file

# Example DataFrame
df = pd.DataFrame({
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 30, None, 50, 60]
})

# Calculate mean and standard error of the mean of groups, excluding missing values
grouped_df = df.dropna().groupby('Group')['Values'].agg(['mean', lambda x: x.std() / x.count() ** 0.5])

print(grouped_df)
