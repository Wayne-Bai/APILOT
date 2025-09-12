import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to compute variance for
df['variance'] = df['column_name'].apply(lambda x: pd.Series(x).var(skipna=True))
