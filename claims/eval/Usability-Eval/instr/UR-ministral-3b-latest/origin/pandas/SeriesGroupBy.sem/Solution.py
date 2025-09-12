import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'group': [1, 2, 1, 2, 1, 2, 2, 1, 1, 2],
    'value': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
})

# Select only the rows where 'value' is not NaN
df = df.dropna(subset=['value'])

# Group by 'group' and calculate the mean
grouped = df.groupby('group')['value'].mean()

# Calculate the standard error of the mean for each group
std_err = grouped.groupby(level=0).std() / sqrt(len(grouped))

print(std_err)
