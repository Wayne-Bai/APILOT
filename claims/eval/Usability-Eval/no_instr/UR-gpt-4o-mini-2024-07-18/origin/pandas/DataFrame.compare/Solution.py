import pandas as pd

# Sample DataFrames for comparison
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

df2 = pd.DataFrame({
    'A': [1, 2, 10],
    'B': [4, 15, 6],
    'C': [7, 8, 11]
})

# Comparing the two DataFrames
diff = df1.compare(df2)

# Displaying the differences
print(diff)
