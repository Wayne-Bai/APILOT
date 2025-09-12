import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# To get the index as an array
index_array = df.index.array

print(index_array)
