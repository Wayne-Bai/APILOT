import pandas as pd

# Create a MultiIndex DataFrame
data = {
    ('A', 'one'): ['A0', 'A1', 'A2', 'A3'],
    ('A', 'two'): ['A4', 'A5', 'A6', 'A7'],
    ('B', 'one'): ['B0', 'B1', 'B2', 'B3'],
    ('B', 'two'): ['B4', 'B5', 'B6', 'B7']
}
df = pd.DataFrame(data)

# Check if index is indeed a MultiIndex
print("Original DataFrame:")
print(df)
print(df.index)

# Create a DataFrame with the levels of the MultiIndex as columns
df = df.unstack()
df.columns = df.columns.swaplevel()

# Adding new columns 
df.reset_index(inplace=True, names=['new_column'])
df.columns = ['Level_0', 'Level_1', 'one', 'two']

print("\nDataFrame with levels of the MultiIndex as columns:")
print(df)
