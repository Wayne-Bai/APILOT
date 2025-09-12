import pandas as pd

# Suppose df is your DataFrame and 'column_name' is the column of interest
quantile_value = df['column_name'].quantile(q=0.5)  # replace 0.5 with your desired quantile
