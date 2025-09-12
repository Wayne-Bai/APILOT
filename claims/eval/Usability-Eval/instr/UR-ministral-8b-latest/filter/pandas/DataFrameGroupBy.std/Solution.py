import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, None, 3, 4, 5]
}

df = pd.DataFrame(data)

# Compute standard deviation for groups, excluding missing values
df_std = df.groupby(df.columns).std().replace([float('nan')], [0])
print(df_std)
