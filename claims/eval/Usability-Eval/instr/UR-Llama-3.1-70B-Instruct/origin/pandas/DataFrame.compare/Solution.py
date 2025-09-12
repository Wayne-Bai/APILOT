import pandas as pd

# Creating the first DataFrame
df1 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10],
    'C': [11, 12, 13, 14, 15]
})

# Creating the second DataFrame
df2 = pd.DataFrame({
    'A': [1, 2, 3, 4, 6],
    'B': [6, 7, 8, 10, 10],
    'C': [11, 12, 13, 14, 15]
})

# Find the differences
diff_df = pd.concat([df1, df2]).reset_index(drop=True).drop_duplicates(keep=False)

# Displaying the differences
print(diff_df)
