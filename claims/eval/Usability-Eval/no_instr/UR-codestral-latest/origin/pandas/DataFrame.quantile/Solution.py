import pandas as pd

# Assuming you have a DataFrame df
# If not, please define or load your DataFrame here

# Compute the quantile over the index
quantile_values = df.quantile(0.5)  # change 0.5 to your desired quantile

# If you want to compute quantile over a column, use axis = 0
quantile_values = df['column_name'].quantile(0.5)  # change 'column_name' and 0.5 to your desired column and quantile

# If you want to compute quantile over a row, use axis = 1
quantile_values = df.quantile(0.5, axis=1)  # change 0.5 to your desired quantile
