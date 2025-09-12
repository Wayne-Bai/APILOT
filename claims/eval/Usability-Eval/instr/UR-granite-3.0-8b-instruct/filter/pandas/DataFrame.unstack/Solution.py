import pandas as pd

# Assuming df is your DataFrame and 'column1' and 'column2' are the columns you want to pivot
df = pd.DataFrame({'column1': ['A', 'A', 'B', 'B'],
                   'column2': [1, 2, 3, 4]})

# Set 'column1' as the index
df.set_index('column1', inplace=True)

# Pivot 'column2'
df = df.unstack()

# Reset the index
df.reset_index(inplace=True)

print(df)
