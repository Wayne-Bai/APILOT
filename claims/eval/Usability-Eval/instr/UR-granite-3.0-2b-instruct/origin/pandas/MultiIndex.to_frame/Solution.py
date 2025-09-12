import pandas as pd

# Create a dictionary with MultiIndex
data = {
    ('A', 'B'): [1, 2, 3],
    ('A', 'C'): [4, 5, 6],
    ('B', 'C'): [7, 8, 9]
}

# Create a MultiIndex from the dictionary keys
index = pd.MultiIndex.from_keys(data.keys())

# Create a DataFrame with the MultiIndex as columns
df = pd.DataFrame(data, index=index)

# Print the DataFrame
print(df)
