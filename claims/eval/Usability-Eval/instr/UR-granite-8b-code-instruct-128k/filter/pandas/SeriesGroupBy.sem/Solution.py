import pandas as pd

# Assuming df is your DataFrame and column_name is the column containing the data
std_err = df.groupby('column_name').sem()
print(std_err)
