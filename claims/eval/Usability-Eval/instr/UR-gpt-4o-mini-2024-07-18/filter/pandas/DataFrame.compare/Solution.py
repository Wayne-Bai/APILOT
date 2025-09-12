import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

df2 = pd.DataFrame({
    'A': [1, 2, 10],
    'B': [4, 15, 6],
    'C': [7, 8, 9]
})

# Compare DataFrames and show differences
difference = df1.compare(df2, keep_shape=True, keep_equal=True)

print(difference)
