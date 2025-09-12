
import pandas as pd

# Create a sample dataframe with some data
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Gender': ['Female', 'Male', 'Non-Binary']}
df = pd.DataFrame(data)

# Hide the entire index / column headers from display
df.style.hide_index()

# Alternatively, to hide specific rows / columns from display, use the following methods:
# 1. df.style.hide_columns([column_name]) or df.style.hide_rows([row_number])
# 2. df.style.set_properties(**{'hidden': True}) for both rows and columns

print(df)
