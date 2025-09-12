import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column where you want to apply the function
# Let's say we want to apply a function that squares each element in the column

def square(x):
    return x ** 2

# Apply the function to the column
df['column_name'] = df['column_name'].apply(square)
