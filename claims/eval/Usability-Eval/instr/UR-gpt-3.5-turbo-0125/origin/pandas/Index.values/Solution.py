
import pandas as pd

# Create an Index object
index_data = pd.Index(['A', 'B', 'C', 'D', 'E'])

# Convert the Index object to array
index_array = index_data.to_numpy()

print(index_array)
