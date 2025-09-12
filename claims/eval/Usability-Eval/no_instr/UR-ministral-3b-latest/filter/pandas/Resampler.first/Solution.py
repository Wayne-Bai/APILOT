import pandas as pd

# Example DataFrame
df = pd.DataFrame({'A': [1, 2, None], 'B': [None, 2, 3], 'C': [4, None, 6]})

# Compute the first non-null entry of each column
df.loc[:, df.apply(lambda x: x.ffill(min_count=1))]

