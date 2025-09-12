
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, None, 4],
        'B': ['apple', None, 'banana', 'orange'],
        'C': [None, 20, 30, 40]}
df = pd.DataFrame(data)

# Remove missing values
df.dropna(inplace=True)

print(df)
