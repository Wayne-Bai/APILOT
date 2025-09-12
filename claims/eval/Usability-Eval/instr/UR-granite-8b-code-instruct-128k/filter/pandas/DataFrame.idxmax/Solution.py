import pandas as pd

# Assuming you have a DataFrame named df and you want to find the index of the first occurrence of the maximum value in the 'column_name' column
idx = df['column_name'].idxmax()

print(idx)
