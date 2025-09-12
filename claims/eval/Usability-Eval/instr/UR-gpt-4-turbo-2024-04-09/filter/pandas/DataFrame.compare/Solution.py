import pandas as pd

# Example DataFrames
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

df2 = pd.DataFrame({
    'A': [1, 2, 4],
    'B': [4, 5, 7]
})

# Comparing DataFrames and displaying the differences
difference_df = (df1 != df2)
print("Differences:\n", difference_df)
