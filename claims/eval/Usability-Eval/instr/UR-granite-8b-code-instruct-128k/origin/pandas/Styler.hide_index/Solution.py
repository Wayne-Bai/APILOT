
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Hide the entire index
df.index.name = None

# Hide specific keys in the index
df.loc[['A', 'C'], 'A'] = None

print(df)
