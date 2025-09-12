import pandas as pd
import numpy as np

# Sample dataframe
df = pd.DataFrame({
    'A': [np.nan, 5, np.nan, 9],
    'B': [np.nan, np.nan, 2, 4],
    'C': [np.nan, 3, np.nan, np.nan]
})

# Calculate the first non-null entry for each column
first_non_null = df.apply(lambda x: x[x.notnull()].iloc[0])

print(first_non_null)
