import pandas as pd

# Create a sample MultiIndex
arrays = [
    ['foo', 'foo', 'bar', 'bar'],
    ['one', 'two', 'one', 'two']
]
index = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))

# Create a DataFrame using the MultiIndex
df = pd.DataFrame({
    'values': [1, 2, 3, 4]
}, index=index)

# Reset the MultiIndex levels into columns
df_reset = df.reset_index()

print(df_reset)
