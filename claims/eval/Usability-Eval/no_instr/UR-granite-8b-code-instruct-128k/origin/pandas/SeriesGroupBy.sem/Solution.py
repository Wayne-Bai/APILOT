import pandas as pd

# Assuming you have a DataFrame named 'df' with columns 'group' and 'value'
# and you want to calculate the standard error of the mean for each group

# Group the data by 'group' and calculate the mean of 'value' for each group
mean_by_group = df.groupby('group')['value'].mean()

# Calculate the standard error of the mean for each group
std_error = df.groupby('group')['value'].sem()

# Print the results
print(mean_by_group)
print(std_error)
