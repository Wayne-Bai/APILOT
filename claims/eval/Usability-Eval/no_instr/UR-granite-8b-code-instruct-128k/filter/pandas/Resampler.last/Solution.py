import pandas as pd

# Assuming you have a DataFrame named 'df'
last_non_null = df.notnull().idxmax(axis=0)
