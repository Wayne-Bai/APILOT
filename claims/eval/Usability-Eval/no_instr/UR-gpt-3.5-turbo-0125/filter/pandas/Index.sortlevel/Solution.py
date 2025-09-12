
import pandas as pd

# Create a sample dataframe
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Sort the index of the dataframe
df = df.sort_index()

print(df)
