import pandas as pd

# Sample data
data = {
    'group': ['A', 'A', 'B', 'B', 'A', 'B', 'A', None, 'B'],
    'values': [10, 12, None, 4, 5, 6, 8, 7, None]
}

df = pd.DataFrame(data)

# Clean the data by removing missing values
df = df.dropna(subset=['values'])

# Compute the mean for each group
group_means = df.groupby('group')['values'].mean()

# Compute the standard error of the mean
std_error = df.groupby('group')['values'].agg(lambda x: x.std()/pd.Series.count()/pd.Series.mean()**0.5)

print(group_means)
print(std_error)
