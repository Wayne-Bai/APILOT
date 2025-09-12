
import pandas as pd

# Assuming you have a DataFrame called 'df' and you want to find the index of the first occurrence of the minimum value in column 'A'
min_index = df['A'].idxmin()

print(min_index)
