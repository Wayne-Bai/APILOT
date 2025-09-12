# Import pandas library
import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame({
   'A': [1, 2, 3, 4, 5],
   'B': [5, 3, 2, 1, 0],
   'C': [1, 3, 5, 2, 4]
})

# Use idxmax() function to find index of first occurrence of maximum over specified axis
print("Index of maximum value over rows (axis=0):")
print(df.idxmax(axis=0))

print("\nIndex of maximum value over columns (axis=1):")
print(df.idxmax(axis=1))
