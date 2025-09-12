import pandas as pd

# Assuming you have a DataFrame 'df' with a MultiIndex
# Let's create a sample DataFrame for demonstration purposes
# DataFrame with a MultiIndex
arrays = [
    ['bar', 'bar', 'baz', 'baz'],
    ['one', 'two', 'one', 'two']
]
index = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))
df = pd.DataFrame({'A': [1, 2, 3, 4]}, index=index)

print("Original DataFrame:")
print(df)

# Reset the index of the DataFrame
df_reset = df.reset_index()

print("\nDataFrame after resetting the index:")
print(df_reset)
