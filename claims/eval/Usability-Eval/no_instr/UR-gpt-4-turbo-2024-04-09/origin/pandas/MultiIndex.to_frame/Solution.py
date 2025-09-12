import pandas as pd

# Example data for MultiIndex DataFrame
data = {
    ('A', 'a'): [1, 2],
    ('A', 'b'): [3, 4],
    ('B', 'a'): [5, 6],
    ('B', 'b'): [7, 8]
}

# Creating the MultiIndex DataFrame
df = pd.DataFrame(data)
df.columns = pd.MultiIndex.from_tuples(df.columns)

# Reset the index to turn MultiIndex levels into columns
result = df.reset_index(drop=True)
print(result)
