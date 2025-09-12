import pandas as pd

# Assume 'df' is your DataFrame and 'column_name' is the column you want to apply the function to

def my_function(value):
    # Write your function here
    # For example, let's assume we're squaring the value
    return value ** 2

df['column_name'] = df['column_name'].apply(my_function)
