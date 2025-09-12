import pandas as pd

# Sample DataFrame
data = {
    'Column1': ['A', 'B', 'C'],
    'Column2': [1, 2, 3]
}
df = pd.DataFrame(data)

# Suffix labels with string 'suffix'
df = df.add_suffix('_suffix')

print(df)
