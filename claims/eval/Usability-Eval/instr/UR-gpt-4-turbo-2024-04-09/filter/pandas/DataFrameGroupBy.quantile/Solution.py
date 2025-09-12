import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'data': [10, 15, 10, 20, 10, 30]
})

# Calculate the 50th percentile (median) for each group
result = df.groupby('group')['data'].quantile(0.5)

print(result)
