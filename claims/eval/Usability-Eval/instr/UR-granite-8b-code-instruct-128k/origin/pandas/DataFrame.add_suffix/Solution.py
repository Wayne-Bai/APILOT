import pandas as pd

# Assuming you have a DataFrame named df and you want to suffix the labels of a specific column with '_label'
df['column_name'] = df['column_name'].map(lambda x: str(x) + '_label')
