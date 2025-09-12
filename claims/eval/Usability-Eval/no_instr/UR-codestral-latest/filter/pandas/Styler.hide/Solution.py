import pandas as pd

# Let's assume you have a DataFrame called df
# To hide the entire index and column headers, use the following code

df.style.hide_index().hide_columns()

# If you only want to hide specific rows or columns, use the drop or hide functions respectively
# For example, to hide the first row and column, use the following code

df.drop(0).style.hide_index()   # to hide row

# or

df.drop(df.columns[0], axis=1).style.hide_columns()  # to hide column
