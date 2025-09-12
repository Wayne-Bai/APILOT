import pandas as pd

# Assuming df is our DataFrame and 'A', 'B', 'C' are columns
df = pd.DataFrame({
   'A': ['foo', 'bar', 'baz'],
   'B': ['one', 'one', 'two'],
   'C': ['x', 'y', 'z'],
})

suffix = 'suffix'

df = df.rename(columns=lambda x: x + suffix)
