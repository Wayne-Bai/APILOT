import pandas as pd
import numpy as np

# Assuming you have a DataFrame df
# If you don't have a DataFrame, you can create one like this:
# df = pd.DataFrame(np.random.rand(10, 5))

# To find index of first occurrence of maximum value along column axis
max_column_index = df.idxmax()

# To find index of first occurrence of maximum value along row axis
max_row_index = df.idxmax(axis=1)
