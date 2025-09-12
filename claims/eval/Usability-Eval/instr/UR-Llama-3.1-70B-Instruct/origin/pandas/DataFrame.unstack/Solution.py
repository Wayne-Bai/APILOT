# Importing pandas library
import pandas as pd
import numpy as np

# Creating a DataFrame with hierarchical index
data = np.random.randn(4, 2)
index = pd.MultiIndex.from_product([['A', 'B'], ['X', 'Y']], names=['Letter', 'Number'])
df = pd.DataFrame(data, index=index, columns=['Value1', 'Value2'])

# Displaying the DataFrame
print("Original DataFrame:")
print(df)

# Pivoting the 'Letter' level of the index
df_pivot = df.pivot_table(index=df.index.get_level_values(1), columns=df.index.get_level_values(0), values=['Value1', 'Value2'])

# Displaying the pivoted DataFrame
print("\nPivoted DataFrame:")
print(df_pivot)
