import pandas as pd

# load data
data = pd.read_csv("data.csv")

# compute variance of each group
groups = data.groupby("group")
variances = groups.agg(lambda x: x.std()**2)

print(variances)
