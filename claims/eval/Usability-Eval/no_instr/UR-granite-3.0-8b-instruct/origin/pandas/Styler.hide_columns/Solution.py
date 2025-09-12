import pandas as pd

# Assuming df is your DataFrame and you want to hide the first column
df = df.iloc[:, 1:]

# If you want to hide specific columns, you can do so like this:
# df = df.drop(['column1', 'column2'], axis=1)
