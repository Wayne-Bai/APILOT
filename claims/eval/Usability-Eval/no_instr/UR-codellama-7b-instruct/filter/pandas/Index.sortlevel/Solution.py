
import pandas as pd

# create a sample MultiIndex
mi = pd.MultiIndex.from_product([[1, 2], [3, 4]])

# sort the MultiIndex in ascending order
mi.sort_values(ascending=True)
