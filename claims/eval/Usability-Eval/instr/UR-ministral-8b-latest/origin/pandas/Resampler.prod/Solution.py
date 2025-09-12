import pandas as pd

# Sample data
data = {
    'group': ['A', 'A', 'B', 'B', 'B', 'C'],
    'value': [1, 2, 3, 4, 5, 6]
}

df = pd.DataFrame(data)

# Compute the product of values for each group
def compute_product(group):
    return group['value'].prod()

# Group by 'group' and apply the compute_product function
result = df.groupby('group').apply(compute_product)

print(result)
