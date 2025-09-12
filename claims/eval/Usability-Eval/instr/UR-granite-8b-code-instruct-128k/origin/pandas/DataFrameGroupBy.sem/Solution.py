import pandas as pd

# Assuming you have a DataFrame called 'df' with columns 'group' and 'value'
# and that you want to compute the standard error of the mean for each group

# First, filter out missing values
df_no_missing = df.dropna()

# Then, group the data by 'group' and compute the mean of 'value' for each group
means = df_no_missing.groupby('group')['value'].mean()

# Finally, compute the standard error of the mean for each group
standard_errors = df_no_missing.groupby('group')['value'].sem()

# Print the results
print(means)
print(standard_errors)
