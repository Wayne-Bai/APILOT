import pandas as pd

# Assuming 'data' is your DataFrame and 'splits' is your array of splits
data = pd.DataFrame(...)
splits = [...]

# Create an IntervalIndex
index = pd.IntervalIndex.from_arrays(data['column_to_create_index_from'], splits)

# Set the index of the DataFrame
data.set_index(index, inplace=True)
