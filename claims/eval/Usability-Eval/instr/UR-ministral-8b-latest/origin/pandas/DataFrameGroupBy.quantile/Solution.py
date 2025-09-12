import pandas as pd

# Sample data
data = pd.DataFrame({
    'values': [1, 2, 2, 3, 4, 4, 4, 5, 6, 7],
    'group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C']
})

# Define a function to return group values at the given quantile
def get_group_quantile(data, quantile, group):
    return data[data['group'] == group].iloc[int((1 - quantile) * (len(data) - 1)):int(quantile * (len(data) - 1)) + 1]['values'].values

# Example usage
quantile = 0.5  # For example, the 50th percentile
group = 'A'
result = get_group_quantile(data, quantile, group)
print(f"Values at {quantile * 100}% quantile for group '{group}':", result)
