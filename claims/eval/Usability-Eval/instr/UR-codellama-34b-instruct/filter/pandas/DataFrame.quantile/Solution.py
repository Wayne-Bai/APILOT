
import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

# calculate the values at the 50th percentile over axis=0 (rows)
values_at_quantile = df.quantile(q=0.5, axis='index')
print(values_at_quantile)
