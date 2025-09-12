
import pandas as pd

# create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, None, None]})

# compute the last non-null entry of each column
result = df.apply(lambda x: x[~pd.isna(x)][-1])

print(result)
