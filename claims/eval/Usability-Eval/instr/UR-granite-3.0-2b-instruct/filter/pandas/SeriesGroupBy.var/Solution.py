import pandas as pd

# Assuming df is your DataFrame and 'group' and 'value' are your columns
df['value'] = df['value'].replace(np.nan, 0)  # Replace missing values with 0
grouped = df.groupby('group')['value'].agg(['mean', 'std'])  # Compute mean and standard deviation for each group
