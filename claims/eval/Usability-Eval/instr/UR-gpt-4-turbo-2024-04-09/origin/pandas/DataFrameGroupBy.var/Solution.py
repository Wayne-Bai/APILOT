import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 15, 10, None, 20, 25]
}

df = pd.DataFrame(data)

# Computing variance of groups, excluding missing values
variance = df.groupby('Group')['Values'].var(ddof=1)  # ddof=1 for sample variance
print(variance)
