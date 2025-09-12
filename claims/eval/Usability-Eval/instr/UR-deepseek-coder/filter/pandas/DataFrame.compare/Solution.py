import pandas as pd

# Sample DataFrames for comparison
df1 = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
})

df2 = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 13],
    'C': [9, 10, 11, 12]
})

# Identify differences
diff = df1.compare(df2)

# Display the differences
print(diff)
