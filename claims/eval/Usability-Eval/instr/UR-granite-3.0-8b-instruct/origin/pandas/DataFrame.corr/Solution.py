import pandas as pd

# Assuming df is your DataFrame
corr_matrix = df.corr()

# If you want to exclude NA/null values, you can use the following:
corr_matrix = df.dropna().corr()
