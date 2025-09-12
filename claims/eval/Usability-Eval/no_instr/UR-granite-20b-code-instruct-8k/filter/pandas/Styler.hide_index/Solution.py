import pandas as pd

# Create a sample dataframe
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Hide the entire index
df.index.names = [''] * len(df.index.names)

# Hide specific keys in the index
# df.index.names = [None if name == 'key_to_hide' else name for name in df.index.names]
