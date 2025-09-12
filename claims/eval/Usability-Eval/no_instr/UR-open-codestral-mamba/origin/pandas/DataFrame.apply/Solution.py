import pandas as pd

# Create a simple dataframe
df = pd.DataFrame({
   'A': [1, 2, 3, 4],
   'B': [5, 6, 7, 8],
   'C': [9, 10, 11, 12]
})

def add_one(x):
    return x + 1

# Apply the function along the row axis (axis=1)
df_result = df.apply(add_one, axis=1)

df_result
