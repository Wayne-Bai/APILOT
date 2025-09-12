import pandas as pd

# Sample data
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}

# Create MultiIndex DataFrame
index = pd.MultiIndex.from_tuples(
    [('north', 0), ('north', 1), ('south', 0), ('south', 1)],
    names=['region', 'number']
)
df = pd.DataFrame(data, index=index)

# Create DataFrame with levels as columns
df_levels_columns = df.reset_index()
df_levels_columns.columns[:] = df_levels_columns.columns[:].str.lower()
df_levels_columns.columns.name = None

print(df_levels_columns)
