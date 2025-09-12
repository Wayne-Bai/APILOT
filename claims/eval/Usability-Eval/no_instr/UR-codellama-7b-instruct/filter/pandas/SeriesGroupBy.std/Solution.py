import pandas as pd

# create sample dataframe
data = {'A': [1, 2, 3, 4, 5], 'B': [7, 8, 9, 10, 11], 'C': [13, 14, 15, 16, 17]}
df = pd.DataFrame(data)

# compute standard deviation of each group
grouper = df['A']
df_grouped = df.groupby(grouper)
df_std = df_grouped.std()

# exclude missing values
df_std = df_std[df_std.index != -1]

print(df_std)