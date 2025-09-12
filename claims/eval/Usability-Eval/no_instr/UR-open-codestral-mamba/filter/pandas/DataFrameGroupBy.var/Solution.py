import pandas as pd
import numpy as np

def compute_group_variance(df, group_column, value_column):
    result = df.groupby(group_column)[value_column].var()
    return result

# Example usage
data = {
    'group': ['A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'value': [1, 2, np.nan, 4, np.nan, 6, 7]
}
df = pd.DataFrame(data)

variances = compute_group_variance(df, 'group', 'value')
print(variances)
