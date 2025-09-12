# First, import pandas
import pandas as pd

# Suppose we have the following DataFrame
df = pd.DataFrame({
   'A': ['foo', 'bar', 'baz'],
   'B': ['one', 'one', 'two'],
   'C': [1, 2, 3],
   'D': [4, 5, 6]
})

# Then we set 'A' as the index of DataFrame df
df.set_index('A', inplace=True)

print(df)
