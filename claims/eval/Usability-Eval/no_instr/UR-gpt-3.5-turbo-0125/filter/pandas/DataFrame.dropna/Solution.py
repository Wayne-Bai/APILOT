
import pandas as pd

# Creating a sample DataFrame
data = {'A': [1, 2, None, 4],
        'B': ['a', None, 'c', 'd'],
        'C': [None, 22, 33, 44]}
df = pd.DataFrame(data)

# Removing missing values from the DataFrame
df.dropna(inplace=True)

print(df)
