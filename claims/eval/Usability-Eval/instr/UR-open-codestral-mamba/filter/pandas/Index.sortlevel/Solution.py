import pandas as pd

# Assuming you have the following DataFrame:
data = {
    'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
    'B': ['one', 'one', 'two', 'two', 'one', 'one'],
    'C': ['small', 'large', 'large', 'small', 'small', 'large'],
    'D': [1, 2, 2, 3, 3, 4],
    'E': [2, 4, 5, 5, 6, 6]
}

df = pd.DataFrame(data)

# Sort the index:
df.sort_index(inplace=True)

print(df)
