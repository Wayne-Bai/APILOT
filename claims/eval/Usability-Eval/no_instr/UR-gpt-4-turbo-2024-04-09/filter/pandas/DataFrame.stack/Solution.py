import pandas as pd

# Sample DataFrame creation
data = {
    'A': ['foo', 'bar', 'baz'],
    'B': [1, 2, 3],
    'C': [4, 5, 6]
}
df = pd.DataFrame(data)

# Stacking the DataFrame on specified level
stacked_df = df.stack()

print(stacked_df)
