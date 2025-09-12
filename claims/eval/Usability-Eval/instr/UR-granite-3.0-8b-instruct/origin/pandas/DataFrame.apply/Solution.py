import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to apply the function to
def apply_function(row):
    # Replace this with your actual function
    return row * 2

df['column_name'] = df['column_name'].apply(apply_function)
