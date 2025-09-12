import pandas as pd
import numpy as np

# Assuming df is your DataFrame and 'group' and 'value' are your columns
df = pd.DataFrame({
    'group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'value': [1, np.nan, 3, 4, 5, np.nan]
})

# Compute the mean of each group, excluding missing values
group_means = df.groupby('group')['value'].apply(lambda x: x.dropna().mean())

# Compute the standard error of the mean for each group
group_std_error = df.groupby('group')['value'].apply(lambda x: x.dropna().std() / np.sqrt(len(x.dropna())))

print(group_means)
print(group_std_error)
