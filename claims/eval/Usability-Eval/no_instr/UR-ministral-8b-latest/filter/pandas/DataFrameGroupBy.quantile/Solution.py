import pandas as pd

# Sample data
data = {
    'Values': [4, 5, 2, 7, 6, 3, 6, 8, 2, 4],
    'Category': ['A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B']
}

# Create DataFrame
df = pd.DataFrame(data)

# Define group and quantile
group_by = 'Category'
quantile = 0.75

# Calculate the quantile value
quantile_value = df.groupby(group_by)['Values'].quantile(quantile)

# Print the results
print(quantile_value)
