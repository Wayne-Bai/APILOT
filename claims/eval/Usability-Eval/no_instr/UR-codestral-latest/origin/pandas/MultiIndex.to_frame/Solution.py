import pandas as pd

# Creating a MultiIndex
index = pd.MultiIndex.from_tuples([('A', 'one'), ('A', 'two'), ('B', 'one'), ('B', 'two')], names=['first', 'second'])

# Creating a DataFrame
df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8]}, index=index)

# Resetting index and creating a DataFrame with levels of the MultiIndex as columns
df = df.reset_index()

# With the MultiIndex levels now as columns, we can set them as the index and unstack to get the data in the desired format
df = df.set_index(['first', 'second']).unstack()

print(df)
