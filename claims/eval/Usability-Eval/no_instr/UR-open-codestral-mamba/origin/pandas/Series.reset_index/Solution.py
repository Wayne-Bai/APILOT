import pandas as pd

# Creating a simple DataFrame
df = pd.DataFrame({
   'A': [1, 2, 3, 4, 5],
   'B': ['a', 'b', 'c', 'd', 'e']
})

# Resetting the index
new_df = df.reset_index(drop=True)

print(new_df)
