import pandas as pd

# Assuming df is your DataFrame
df_dict = df.to_dict(orient='records')

# If you want to convert the DataFrame to a dictionary with columns as keys and rows as values, you can use:
df_dict = df.T.to_dict('list')
