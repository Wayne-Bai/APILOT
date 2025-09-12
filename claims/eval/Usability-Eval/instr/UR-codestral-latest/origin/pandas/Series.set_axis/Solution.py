import pandas as pd

# let's assume we have a DataFrame df
df = pd.DataFrame({
   'A': ['foo', 'bar', 'baz'],
   'B': ['one', 'one', 'two'],
   'C': ['x', 'y', 'z'],
   'D': [1, 2, 3]
})

# we can assign a new index to the rows
new_index = ['first', 'second', 'third']
df.index = new_index

print(df)
