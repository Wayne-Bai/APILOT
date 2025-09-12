import pandas as pd

# Assuming you have a DataFrame called 'df' with columns 'group' and 'value'
# and that you want to compute the standard deviation of 'value' within each group

# Group the DataFrame by 'group' and compute the standard deviation of 'value'
# excluding missing values
sd_by_group = df.groupby('group')['value'].std(skipna=True)

# Print the result
print(sd_by_group)
