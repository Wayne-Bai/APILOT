import pandas as pd

# Example DataFrame
data = {
    'group': ['A', 'A', 'A', 'B', 'B', 'B', None, 'B', None],
    'value': [10, 20, None, 30, None, 40, 50, None, 60]
}

df = pd.DataFrame(data)

# Drop missing values
df_cleaned = df.dropna()

# Compute the mean and standard error of the mean for groups
group_means = df_cleaned.groupby('group')['value'].mean()
group_se = group_means / (df_cleaned.groupby('group').size() ** 0.5)

print(f"Group means: {group_means}")
print(f"Group standard error of the mean: {group_se}")
