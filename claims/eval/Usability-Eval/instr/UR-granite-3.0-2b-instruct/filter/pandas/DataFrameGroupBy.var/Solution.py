import pandas as pd

# Assuming df is your DataFrame and 'group' and 'value' are your columns
df['value_squared'] = df['value'].apply(lambda x: x ** 2)
grouped = df.groupby('group')['value_squared'].transform('var')
