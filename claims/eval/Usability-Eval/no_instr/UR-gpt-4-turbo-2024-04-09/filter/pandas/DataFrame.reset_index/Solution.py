import pandas as pd

# Sample DataFrame with a MultiIndex
index = pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1), ('B', 2)], names=['Outer', 'Inner'])
df = pd.DataFrame({'Data': [10, 20, 30, 40]}, index=index)

# Reset the index of the DataFrame
df_reset = df.reset_index()

print(df_reset)
