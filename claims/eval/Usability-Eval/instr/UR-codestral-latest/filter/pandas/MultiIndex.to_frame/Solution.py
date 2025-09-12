import pandas as pd

# Sample data
data = {
    ('A', 'one'): [1, 2, 3],
    ('A', 'two'): [4, 5, 6],
    ('B', 'one'): [7, 8, 9],
    ('B', 'two'): [10, 11, 12]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Set MultiIndex as columns
df.columns = pd.MultiIndex.from_tuples(df.columns)

print(df)
