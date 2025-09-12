import pandas as pd

# Assuming df is your DataFrame and it has an Index
df = pd.DataFrame({
    'A': ['foo', 'bar', 'baz', 'qux'],
    'B': ['one', 'one', 'two', 'three'],
    'C': [1, 2, 3, 4],
    'D': [10, 20, 30, 40]
})

# Set the Index as the first column
df.set_index('A', inplace=True)

# Sort the Index
df.sort_index(inplace=True)
