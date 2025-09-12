import pandas as pd

def group_values_at_quantile(df, group_col, value_col, quantile):
    return df.groupby(group_col)[value_col].transform(lambda x: x.quantile(quantile))

# Example usage
data = {
    'group': ['A', 'A', 'A', 'B', 'B', 'B'],
    'value': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)

quantile_value = 0.5  # e.g., 50th percentile
df['quantile_value'] = group_values_at_quantile(df, 'group', 'value', quantile_value)

print(df)
