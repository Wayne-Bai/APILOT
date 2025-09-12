import pandas as pd

# Assuming you have a DataFrame named df and a column named 'column_name'
df['min_value'] = df.groupby('group_column_name')['column_name'].transform('min')

# The transformed column 'min_value' in the DataFrame df now contains the min value of 'column_name' for each group defined by 'group_column_name'
