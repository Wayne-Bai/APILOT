import pandas as pd

# Assuming you have a DataFrame named 'df' and a column named 'column_name'
min_value = df.groupby('column_name').min()

print(min_value)
