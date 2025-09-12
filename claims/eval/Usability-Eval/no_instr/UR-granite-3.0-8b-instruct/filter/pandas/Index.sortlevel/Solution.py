import pandas as pd

# Assuming df is your DataFrame and it has a MultiIndex
df.set_index(keys=['level_1', 'level_2'], inplace=True)

# Sort the MultiIndex
df.sort_index(inplace=True)
