import pandas as pd

# Create a dictionary with MultiIndex levels as values
data = {
    ('A', 'B'): 1,
    ('A', 'C'): 2,
    ('B', 'C'): 3,
    ('B', 'D'): 4
}

# Create a MultiIndex from the dictionary values
index = pd.MultiIndex.from_tuples(data.items(), names=['level_1', 'level_2'])

# Create a DataFrame with the MultiIndex as columns
df = pd.DataFrame(data, columns=index)

print(df)
