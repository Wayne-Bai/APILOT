import pandas as pd

# Assuming df is your DataFrame and 'group' and 'value' are your columns

# Compute standard error of the mean for each group, excluding missing values
df['std_error'] = df.groupby('group')['value'].apply(lambda x: x.std() / len(x))

# Filter out missing values
df = df.dropna(subset=['std_error'])
