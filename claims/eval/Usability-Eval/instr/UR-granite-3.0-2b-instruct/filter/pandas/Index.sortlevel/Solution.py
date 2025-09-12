import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': ['foo', 'bar', 'baz', 'qux'],
    'B': ['one', 'one', 'two', 'three'],
    'C': [1, 2, 3, 4],
    'D': [10, 20, 30, 40]
})

# Sort the DataFrame by column 'A' and 'B'
df_sorted = df.sort_values(by=['A', 'B'])
