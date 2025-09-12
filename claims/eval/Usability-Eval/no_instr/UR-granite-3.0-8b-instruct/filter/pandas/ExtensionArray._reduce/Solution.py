import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to perform the reduction operation on
result = df['column_name'].sum()  # Replace 'sum' with the reduction operation you want to perform (e.g., mean, min, max, etc.)
print(result)
