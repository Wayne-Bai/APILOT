
import pandas as pd

# Creating a sample DataFrame
data = {'A': [1, 2, None, 4, 5],
        'B': [None, 22, 33, 44, 55],
        'C': ['foo', 'bar', 'baz', None, 'qux']}
df = pd.DataFrame(data)

# Removing missing values
df = df.dropna()

# Displaying the DataFrame after removing missing values
print(df)
