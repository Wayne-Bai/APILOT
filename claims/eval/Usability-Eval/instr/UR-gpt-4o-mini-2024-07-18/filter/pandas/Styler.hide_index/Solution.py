import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data, index=['row1', 'row2', 'row3'])

# Option 1: Hide the entire index when printing
print(df.to_string(index=False))

# Option 2: Hide specific keys in the index by resetting the index
df_reset = df.reset_index(drop=True)
print(df_reset)
