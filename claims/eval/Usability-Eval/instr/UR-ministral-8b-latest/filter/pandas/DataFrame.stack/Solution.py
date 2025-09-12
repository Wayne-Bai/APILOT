import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Prescribed level
level = 1

# Stacking the columns to index
df_stacked = df.stack(level=level)

print(df_stacked)
