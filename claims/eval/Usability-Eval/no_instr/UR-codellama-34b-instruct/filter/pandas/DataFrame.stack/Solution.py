
import pandas as pd

# create a sample dataframe
df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3], 'C': [4, 5, 6]})

# stack the levels from columns to index
stacked_df = df.melt(id_vars=['A'], value_vars=['B', 'C'])

print(stacked_df)
