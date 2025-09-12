import pandas as pd

# Assuming df is your DataFrame and 'group' is the column for grouping
# and 'value' is the column for calculating variance

# Drop missing values
df = df.dropna(subset=['group', 'value'])

# Group by 'group' and calculate variance
grouped = df.groupby('group')['value'].var()

print(grouped)
