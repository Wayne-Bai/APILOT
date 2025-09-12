import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({'A': ['a', 'a', 'b', 'b', 'a', 'b'],
                   'B': ['x', 'y', 'x', 'y', 'x', 'y'],
                   'C': [1, 2, 3, 4, 5, 6]})

# Use sort_values method to sort DataFrame by multiple columns
df_sorted = df.sort_values(by=['A', 'B'])

# If you want to reset index after sorting
df_sorted_reset_index = df_sorted.reset_index(drop=True)
