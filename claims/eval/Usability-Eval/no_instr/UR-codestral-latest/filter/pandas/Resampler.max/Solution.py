import pandas as pd

# Assuming df is your dataframe and 'group_column' is the name of your group column and 'value_column' is the name of your value column
max_values = df.groupby('group_column')['value_column'].max()
