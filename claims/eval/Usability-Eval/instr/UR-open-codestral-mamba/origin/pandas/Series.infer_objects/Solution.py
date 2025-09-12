import pandas as pd

# Let's consider df is a given pandas dataframe.
# df = pd.DataFrame({'Column1': ['A', 'B', 'C'], 'Column2': [1, 2, 3], 'Column3': ['X', 'Y', 'Z']})

# Infer better dtypes for object columns
df = df.convert_dtypes()
