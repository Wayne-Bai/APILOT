import pandas as pd

# Assuming df is your DataFrame and index is a MultiIndex
sorted_df = df.sort_index(level=0)

# If you want to sort by multiple levels, you can pass a list of levels to the level parameter
sorted_df = df.sort_index(level=[0, 1])

# If you want to sort in descending order, you can pass ascending=False
sorted_df = df.sort_index(level=0, ascending=False)