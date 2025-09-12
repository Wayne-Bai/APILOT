import pandas as pd

# Assuming df is your DataFrame and 'group' is the column by which you want to group
grouped = df.groupby('group')

# Compute the product of values in each group
prod = grouped['column_to_multiply'].apply(lambda x: x.prod())

# If you want to get the result as a Series, you can convert it like this:
prod_series = pd.Series(prod)
