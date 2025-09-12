import pandas as pd

# Assuming df is your DataFrame and 'level_name' is the name of the level you want to sort by
df = df.sort_index(level='level_name', ascending=True)
