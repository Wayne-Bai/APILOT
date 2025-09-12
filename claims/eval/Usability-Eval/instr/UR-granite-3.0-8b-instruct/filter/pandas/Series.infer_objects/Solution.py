import pandas as pd

# Assuming df is your DataFrame
df = pd.read_csv('your_file.csv')

# Infer better dtypes for object columns
df = df.apply(lambda x: pd.to_datetime(x, errors='coerce') if x.name in ['date_column'] else x.astype(pd.Series(x.dtype).mode()[0]) if x.dtype == 'object' else x)
