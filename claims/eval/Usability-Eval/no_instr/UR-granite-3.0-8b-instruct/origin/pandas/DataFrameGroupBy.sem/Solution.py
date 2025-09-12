import pandas as pd

# Assuming df is your DataFrame and 'group' is the column for grouping
# and 'value' is the column with the values for which you want to compute the standard error of the mean

# Filter out missing values
df_clean = df.dropna(subset=['group', 'value'])

# Group by 'group' and compute the mean of 'value' for each group
group_means = df_clean.groupby('group')['value'].mean()

# Compute the standard error of the mean for each group
std_err = df_clean.groupby('group')['value'].apply(lambda x: x.std() / x.count() ** 0.5)

# Combine the mean and standard error into a single DataFrame
result = pd.concat([group_means, std_err], axis=1)
result.columns = ['mean', 'std_err']

print(result)
