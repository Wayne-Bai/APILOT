
import pandas as pd

# create a sample DataFrame
df = pd.DataFrame({'A': [1, np.nan, 3, 4], 'B': [np.nan, 2, 3, 4], 'C': [np.nan, 2, 3, 4]})

# compute the last non-null entry of each column
df_last = df.dropna().tail(1)

print(df_last)
