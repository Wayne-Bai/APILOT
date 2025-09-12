import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# To hide the entire index, set the index to False
df.index = df.index.tolist()
df = df.set_index(False)

# To hide specific keys in the index, you can use the following approach:
# For example, if you want to hide the keys 'A' and 'B' from the index
df.index = df.index.get_level_values(0).drop_duplicates().tolist()
