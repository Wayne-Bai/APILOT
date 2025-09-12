
import pandas as pd

# create example dataframe
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# group by column A and get values at the given quantile
groups = df.groupby('A')
quantiles = groups['B'].transform(lambda x: np.percentile(x, 25))

print(quantiles)
