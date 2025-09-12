import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
   'A': ['foo', 'bar', 'baz', 'qux'],
   'B': ['one', 'one', 'two', 'three'],
   'C': [1, 2, 3, 4],
   'D': [10, 20, 30, 40]
})

# Set the index to column 'B'
df.set_index('B', inplace=True)

# Reset the index
df.reset_index(drop=True, inplace=True)

print(df)
