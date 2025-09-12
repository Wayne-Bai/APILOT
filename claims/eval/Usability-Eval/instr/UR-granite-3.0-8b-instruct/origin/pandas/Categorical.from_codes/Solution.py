import pandas as pd

# Assuming you have a DataFrame 'df' and 'column_name' is the column you want to convert to categorical
df['column_name'] = df['column_name'].astype('category')
