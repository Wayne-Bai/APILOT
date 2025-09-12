import pandas as pd
# Assuming 'df' is your DataFrame and 'column_name' is the column you want to sum by group
grouped_data = df.groupby('column_name')['value_column'].sum()
print(grouped_data)
