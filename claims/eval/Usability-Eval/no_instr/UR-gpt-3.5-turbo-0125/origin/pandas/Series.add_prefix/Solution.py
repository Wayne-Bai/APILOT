
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)

# Prefix labels with 'string_prefix.'
df.columns = 'string_prefix.' + df.columns

print(df)
