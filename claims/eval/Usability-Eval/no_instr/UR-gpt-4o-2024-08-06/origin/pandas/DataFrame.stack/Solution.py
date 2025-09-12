import pandas as pd

# Sample dataframe
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

# Create a DataFrame
df = pd.DataFrame(data, index=['row1', 'row2', 'row3'])

# Set a name for the columns to stack
df.columns.name = 'columns'

# Stacking the 'A' and 'B' columns
stacked_df = df.stack()

print(stacked_df)
