import pandas as pd

# Assuming df is your DataFrame and 'index_label' is the level of the index you want to pivot
df = df.pivot(index = df.index.get_level_values(0), columns = 'index_label', values = 'value_column')
