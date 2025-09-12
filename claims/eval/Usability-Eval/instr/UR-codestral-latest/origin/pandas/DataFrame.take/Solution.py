import pandas as pd

# create a simple dataframe
df = pd.DataFrame({
   'A': ['foo', 'bar', 'baz', 'qux'],
   'B': ['one', 'one', 'two', 'three'],
   'C': ['x', 'y', 'z', 'w'],
   'D': [1, 2, 3, 4]
})

# specify the positional indices
indices = [0, 2]

# return the elements at the specified indices
elements = df.iloc[indices]

print(elements)
