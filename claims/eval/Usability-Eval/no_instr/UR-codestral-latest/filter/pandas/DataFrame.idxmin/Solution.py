import pandas as pd

# Assuming df is your DataFrame
min_index_per_column = df.idxmin()

# If you want to find the index of the minimum value of the whole DataFrame
min_index_overall = df.stack().idxmin()
