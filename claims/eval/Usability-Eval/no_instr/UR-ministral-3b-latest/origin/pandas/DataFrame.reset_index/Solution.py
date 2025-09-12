import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': ['foo', 'bar', 'baz', 'qux'],
    'B': ['one', 'two', 'three', 'four']
})

print('Original DataFrame:')
print(df)

# Resetting the index
reset_df = df.reset_index()

print('\nDataFrame after resetting the index:')
print(reset_df)
