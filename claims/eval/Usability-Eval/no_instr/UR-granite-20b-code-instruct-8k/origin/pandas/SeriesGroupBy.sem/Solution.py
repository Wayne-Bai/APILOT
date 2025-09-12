
import pandas as pd

# Assuming you have a DataFrame named 'df' with a column named 'column_name' and a column named 'group_name'
# that contains the groups for each row in 'column_name'

# Compute standard error of the mean by group
std_error = df.groupby('group_name')['column_name'].sem()
