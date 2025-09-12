import pandas as pd

# Assuming you have a DataFrame df
# df = pd.DataFrame({'group': ['A', 'A', 'B', 'B'], 'value': [1, 2, 3, 4]})

# Compute the product of values for each group
prod_of_groups = df.groupby('group')['value'].prod()

print(prod_of_groups)
