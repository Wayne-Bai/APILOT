
import pandas as pd

# create sample data frame
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'score': [90, 80, 70]}
df = pd.DataFrame(data)

# calculate quantiles for each group
group_quantiles = df.groupby('name')['score'].quantile([0.25, 0.5, 0.75])
print(group_quantiles)
