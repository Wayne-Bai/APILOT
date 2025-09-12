import pandas as pd

# Assuming df is your DataFrame and 'group' and 'value' are your columns
df = pd.DataFrame({
    'group': ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'value': [1, 2, 3, 4, 5, 6, 7, 8]
})

# Compute standard error of the mean of groups, excluding missing values
se_mean = df.groupby('group')['value'].apply(lambda x: x.std() / x.count()).compute()

print(se_mean)
