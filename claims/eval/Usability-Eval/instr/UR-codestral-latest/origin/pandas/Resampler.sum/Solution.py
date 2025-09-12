# Import the pandas library
import pandas as pd

# Assuming you have a DataFrame df and you want to compute the sum of 'values' column grouped by 'group' column
df_sum = df.groupby('group')['values'].sum().reset_index()
