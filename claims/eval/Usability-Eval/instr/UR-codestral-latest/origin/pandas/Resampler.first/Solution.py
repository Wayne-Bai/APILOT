import pandas as pd
import numpy as np

# Assuming df is your DataFrame
df = pd.DataFrame({'A': [np.nan, 2, 3, np.nan],
                   'B': [np.nan, np.nan, 3, 4],
                   'C': [np.nan, np.nan, np.nan, 4]})

# The function to compute the first non-null entry of each column
def first_non_null(column):
    return column.dropna().iloc[0]

# Apply the function to each column
result = df.apply(first_non_null)

print(result)
