
import pandas as pd

# Create a sample dataframe with hierarchical index
data = {'A': [1, 1, 1, 2, 2, 2],
        'B': [10, 20, 30, 40, 50, 60],
        'C': [100, 200, 300, 400, 500, 600]}
df = pd.DataFrame(data)
df = df.set_index(['A', 'B'])
print("Original DataFrame:")
print(df)

# Pivot the index level 'A'
pivoted_df = df.unstack('A')
print("\nPivoted DataFrame:")
print(pivoted_df)
