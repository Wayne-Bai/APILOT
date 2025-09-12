import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A'],
    'Score': [10, 12, 8, 15, 14, 10, None, 9, 12, 11]
}
df = pd.DataFrame(data)

# Compute standard deviation excluding missing values
result = df.groupby('Group')['Score'].apply(lambda x: x.dropna().std()).reset_index()

print(result)
