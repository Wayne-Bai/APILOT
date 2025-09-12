import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame(...)

# Infer better dtypes for object columns
df = df.astype(pd.to_numeric(df, errors='coerce'))
df = df.apply(pd.to_datetime, errors='ignore')
