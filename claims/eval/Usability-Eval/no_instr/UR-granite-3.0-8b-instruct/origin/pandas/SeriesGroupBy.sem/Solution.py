import pandas as pd

# Assuming df is your DataFrame and 'group' is the column for grouping
# and 'value' is the column with the values for which you want to compute the standard error of the mean

# Drop missing values
df = df.dropna()

# Group by 'group' and compute the mean of 'value' for each group
group_means = df.groupby('group')['value'].mean()

# Compute the standard error of the mean for each group
group_sem = df.groupby('group')['value'].apply(lambda x: x.std() / x.count() ** 0.5)

# Print the results
print(group_means)
print(group_sem)
