import pandas as pd

# Sample data for DataFrame 1
data1 = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

# Sample data for DataFrame 2
data2 = {
    'A': [1, 2, 3],
    'B': [4, 0, 6],
    'C': [7, 8, 1]
}

# Create DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Compare the DataFrames
comparison = df1.ne(df2)
changed_entries = df1[comparison]

print("Differences between DataFrames:")
print(changed_entries)
