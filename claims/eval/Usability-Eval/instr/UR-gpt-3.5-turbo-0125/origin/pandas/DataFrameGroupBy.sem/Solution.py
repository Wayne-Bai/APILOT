
import pandas as pd

# Generate some sample data
data = {'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Values': [10, 15, 20, None, 25, 30]}
df = pd.DataFrame(data)

# Compute standard error of the mean of groups, excluding missing values
grouped = df.groupby('Group')['Values']
mean = grouped.mean()
group_sizes = grouped.count()
group_std = grouped.std()
sem = group_std / group_sizes**0.5

print(sem)
