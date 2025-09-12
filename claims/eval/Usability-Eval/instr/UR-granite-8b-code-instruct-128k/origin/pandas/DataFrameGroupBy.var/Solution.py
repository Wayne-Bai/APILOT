import pandas as pd

# Assuming you have a DataFrame called 'df' and a column called 'column_name'
variance = df.groupby('column_name').var(skipna=True)
print(variance)
