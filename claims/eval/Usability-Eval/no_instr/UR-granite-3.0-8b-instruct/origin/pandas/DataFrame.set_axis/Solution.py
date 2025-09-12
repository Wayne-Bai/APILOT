import pandas as pd

# Assuming df is your DataFrame and 'index_col' is the column you want to use as the index
df = pd.DataFrame(...)

# Assign the 'index_col' column as the index
df.set_index('index_col', inplace=True)
