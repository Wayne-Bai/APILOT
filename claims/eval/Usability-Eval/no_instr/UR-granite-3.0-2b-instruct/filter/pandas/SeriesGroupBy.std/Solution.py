import pandas as pd

# Assuming df is your DataFrame and 'column1' and 'column2' are the columns you want to compute standard deviation for

# Compute standard deviation of 'column1' and 'column2' for each group, excluding missing values
std_dev = df.groupby('column1').apply(lambda x: x['column2'].dropna().std()).reset_index()

print(std_dev)
