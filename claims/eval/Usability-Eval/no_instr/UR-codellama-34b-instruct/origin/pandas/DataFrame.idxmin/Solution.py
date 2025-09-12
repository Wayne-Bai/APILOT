import pandas as pd

# Sample data frame
df = pd.DataFrame({'A': [4, 3, 2, 1], 'B': [1, 2, 3, 4]})

# Find the index of the first occurrence of the minimum value in column A
min_index = df['A'].idxmin()
print(min_index) # Output: 3
