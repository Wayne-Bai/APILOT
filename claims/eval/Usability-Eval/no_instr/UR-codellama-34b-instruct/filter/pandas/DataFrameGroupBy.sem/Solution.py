
import pandas as pd

# Sample data
data = {'group': ['A', 'B', 'C'],
        'value': [10, 20, 30]}
df = pd.DataFrame(data)

# Compute the standard error of the mean for each group
mean_se = df.groupby('group')['value'].agg(['mean', 'sem'])

print(mean_se)
