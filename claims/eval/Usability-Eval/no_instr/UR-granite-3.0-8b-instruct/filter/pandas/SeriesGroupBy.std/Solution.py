import pandas as pd

# Assuming df is your DataFrame and 'group' is the column for grouping
df['group'] = df['group'].replace('missing', pd.NA)  # Replace 'missing' with NaN
grouped = df.groupby('group').apply(lambda x: x.dropna().std())
