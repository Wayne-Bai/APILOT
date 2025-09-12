
import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# assign a custom index to the dataframe
df = df.set_index(['C'])

print(df)
