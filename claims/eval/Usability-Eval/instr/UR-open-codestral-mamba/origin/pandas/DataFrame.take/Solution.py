
import pandas as pd

# Assuming our DataFrame is:
df = pd.DataFrame({
   'A': [1, 2, 3, 4],
   'B': [5, 6, 7, 8],
   'C': [9, 10, 11, 12]})

def select_elements_at_indices(df, *indices):
    return [df.iloc[index].values.tolist() for index in zip(*indices)]
