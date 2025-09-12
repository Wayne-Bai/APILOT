
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Assign desired index to given axis
df = df.set_index('A')

print(df)
