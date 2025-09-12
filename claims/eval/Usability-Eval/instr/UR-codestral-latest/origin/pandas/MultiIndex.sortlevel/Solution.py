import pandas as pd

# Assuming df is your DataFrame and you have a MultiIndex
# and you want to sort at level 1 while preserving the original ordering of the associated factor at that level

sorted_df = df.sort_values(by=df.index.get_level_values(1))
