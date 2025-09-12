import pandas as pd
import numpy as np

# Attempt to infer better dtypes for object columns.
df = pd.read_csv('path_to_your_file.csv')
df['object_column'] = df['object_column'].apply(convert_dtype)

def convert_dtype(val):
    try:
        val = int(val)
        return val
    except ValueError:
        try:
            val = float(val)
            return val
        except ValueError:
            val = None

df = df.astype({
    'object_column': 'int64' if not np.isnan(df['object_column']).any() else 'float64'
})
