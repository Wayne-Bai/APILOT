import pandas as pd
# Assuming you have a dataframe named df
# Replace 'column_name' with the actual column name you want to use
column_name = 'column_name'
df[column_name].value_counts().plot(kind='bar')
