import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to calculate the quantile for
quantile = 0.5  # You can change this to any quantile you want
axis = 0  # 0 for rows, 1 for columns

# Calculate the quantile
result = df['column_name'].quantile(quantile, axis=axis)

print(result)
