
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

# Prefix labels with 'string_prefix.'
df.columns = 'string_prefix.' + df.columns

print(df)
