import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Values': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

# Compute sum of group values
grouped_sum = df.groupby('Category')['Values'].agg('sum').reset_index()

print(grouped_sum)
