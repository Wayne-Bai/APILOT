import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Get the data in the Index as an array
data_in_index = df.index.values

print(data_in_index)
