import pandas as pd

# Example DataFrame with a MultiIndex
data = {
    'Value': [10, 20, 30, 40, 50, 60],
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Type': ['X', 'Y', 'X', 'Y', 'X', 'Y']
}
df = pd.DataFrame(data)
df.set_index(['Category', 'Type'], inplace=True)

# Pivot a level of the hierarchical index to columns
result = df.unstack(level='Type')

print(result)
