import pandas as pd

# Sample data with MultiIndex
data = {
    ('A', 'X'): [1, 2, 3],
    ('A', 'Y'): [4, 5, 6],
    ('B', 'X'): [7, 8, 9],
    ('B', 'Y'): [10, 11, 12]
}

# Create DataFrame with MultiIndex columns
df = pd.DataFrame(data)

# Reset the index to make MultiIndex levels as columns
df.columns = df.columns.to_flat_index()
df.columns = [f"{col[0]}_{col[1]}" for col in df.columns]

print(df)
