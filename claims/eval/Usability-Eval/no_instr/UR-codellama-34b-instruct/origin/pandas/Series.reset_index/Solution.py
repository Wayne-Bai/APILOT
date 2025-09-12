
import pandas as pd

# Create a sample DataFrame with some data
data = {'A': [1, 2, 3, 4, 5], 'B': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(data)
print(df)

# Use the reset_index() method to generate a new DataFrame with the index reset
new_df = df.reset_index()
print(new_df)
