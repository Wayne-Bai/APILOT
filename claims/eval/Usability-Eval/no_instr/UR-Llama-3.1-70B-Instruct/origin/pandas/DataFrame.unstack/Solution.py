# Import necessary libraries
import pandas as pd
import numpy as np

# Create a multi-index DataFrame
arrays = [np.array(['foo', 'foo', 'foo', 'bar', 'bar', 'bar']),
          np.array(['A', 'A', 'B', 'A', 'B', 'C']),
          np.array(['one', 'two', 'one', 'one', 'one', 'two'])]
index = pd.MultiIndex.from_arrays(arrays, names=['first','second', 'third'])
df = pd.DataFrame(np.random.randn(6), index=index)

# Pivot the'second' level of the index
df_pivoted = df.unstack(level='second')

# Print the original and pivoted DataFrames
print("Original DataFrame:")
print(df)
print("\nPivoted DataFrame:")
print(df_pivoted)
