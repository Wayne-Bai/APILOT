import pandas as pd
import numpy as np

# Create a hierarchical index
np.random.seed(0)
index = pd.MultiIndex.from_product(
    [['A', 'B'], ['X', 'Y'], ['a', 'b']],
    names=['Level 1', 'Level 2', 'Level 3']
)
data = np.random.randn(len(index))
df = pd.DataFrame(data, index=index, columns=['Values'])

print("Original DataFrame:")
print(df)

# Pivot 'Level 3' to a column level
pivoted_df = df.reset_index().pivot_table(index=['Level 1', 'Level 2'], columns='Level 3', values='Values')

print("\nPivot DataFrame:")
print(pivoted_df)
