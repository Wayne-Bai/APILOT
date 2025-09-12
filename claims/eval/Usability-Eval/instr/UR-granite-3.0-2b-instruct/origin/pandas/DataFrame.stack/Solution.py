import pandas as pd

# Assuming df is your DataFrame and 'column1' and 'column2' are the columns from which you want to stack levels
df = pd.DataFrame({
    'column1': [1, 2, 3],
    'column2': [4, 5, 6]
})

# Create a new column 'stack' by stacking the levels from 'column1' and 'column2'
df['stack'] = df.apply(lambda row: row['column1'] + row['column2'], axis=1)

# Set the 'stack' column as the index
df.set_index('stack', inplace=True)
