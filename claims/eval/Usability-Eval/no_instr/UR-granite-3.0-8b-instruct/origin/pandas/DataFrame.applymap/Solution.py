import pandas as pd

# Assuming df is your DataFrame and func is the function you want to apply elementwise
def func(x):
    # Your function logic here
    return x * 2

df['new_column'] = df['existing_column'].apply(func)
