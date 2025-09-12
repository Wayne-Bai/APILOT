import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
   'A': [1, 2, 3],
   'B': [4, 5, 6],
   'C': [7, 8, 9]
})

# Assign desired index to axis 0 (rows)
df.index = ['a', 'b', 'c']

print(df)
