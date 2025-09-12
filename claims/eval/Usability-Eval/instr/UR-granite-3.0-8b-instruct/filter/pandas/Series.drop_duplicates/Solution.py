import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to remove duplicates from
df = pd.DataFrame({
    'column_name': ['value1', 'value2', 'value1', 'value3', 'value2']
})

# Remove duplicates from 'column_name'
df = df.drop_duplicates(subset='column_name')

# If you want to remove duplicates based on multiple columns, you can specify them in the subset parameter
# df = df.drop_duplicates(subset=['column1', 'column2'])

# If you want to keep the first occurrence of duplicates and remove the rest, use keep=False
# df = df.drop_duplicates(subset='column_name', keep=False)
