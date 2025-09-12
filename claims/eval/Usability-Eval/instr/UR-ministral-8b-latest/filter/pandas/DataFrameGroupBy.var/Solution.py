import pandas as pd

# Sample dataframe
data = {
    'GroupA': [1, 2, 3, 4, None],
    'GroupB': [5, 6, None, 8, 9],
    'GroupC': [None, 11, 12, 13, 14]
}
df = pd.DataFrame(data)

# Compute variance of each group, excluding missing values
variance_per_group = df.dropna().var()
