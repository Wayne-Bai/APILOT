import pandas as pd

# Sample data
data = {
    'index_col1': ['A', 'A', 'A', 'B', 'B', 'B'],
    'index_col2': ['X', 'Y', 'Z', 'X', 'Y', 'Z'],
    'value_col': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)
df.set_index(['index_col1', 'index_col2'], inplace=True)

# Pivot the level of index labels
pivot_df = df.unstack(level=-1)

# Display the pivoted DataFrame
print(pivot_df)
