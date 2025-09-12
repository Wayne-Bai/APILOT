
import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, None], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# compute the last non-null entry of each column
last_non_null = df.apply(lambda x: x[x.notna()].iloc[-1])

print(last_non_null)
