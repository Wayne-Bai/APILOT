
import pandas as pd

# Create a sample dataframe
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Set custom index values
custom_index = ['w', 'x', 'y', 'z']
df.index = custom_index

print(df)
