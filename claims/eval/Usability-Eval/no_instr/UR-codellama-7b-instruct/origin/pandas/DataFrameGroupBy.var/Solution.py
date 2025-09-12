
import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15]}
df = pd.DataFrame(data)

# compute the variance of each group, excluding missing values
groups = df.groupby('A')
variances = groups['B'].agg(lambda x: np.var(x[x.notnull()]))
