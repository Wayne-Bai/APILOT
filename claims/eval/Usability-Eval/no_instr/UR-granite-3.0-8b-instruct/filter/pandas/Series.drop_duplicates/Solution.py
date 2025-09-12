import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to remove duplicates from
df = pd.DataFrame({
    'column_name': ['value1', 'value2', 'value1', 'value3', 'value2']
})

# Remove duplicates from the column
df = df.drop_duplicates(subset='column_name')

# If you want to remove duplicates from the entire DataFrame, use:
# df = df.drop_duplicates()
