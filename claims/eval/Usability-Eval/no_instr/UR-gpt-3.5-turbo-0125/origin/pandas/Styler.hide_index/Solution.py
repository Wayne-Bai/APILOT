
import pandas as pd

# Create a sample dataframe
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Hide the entire index from rendering
df.index = pd.RangeIndex(len(df))  # Set a RangeIndex to hide the index when rendered

# If you want to hide specific keys in the index from rendering, you can set them to empty strings
index_to_hide = [1, 3]
df.index = ['' if i in index_to_hide else i for i in df.index]

print(df)
