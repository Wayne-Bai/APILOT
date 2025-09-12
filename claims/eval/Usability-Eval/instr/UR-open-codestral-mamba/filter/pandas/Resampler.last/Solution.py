import pandas as pd

# Assuming df is your DataFrame

df = pd.DataFrame({
   'A': [1, 2, np.nan, 4],
   'B': [5, np.nan, np.nan, 8],
   'C': [9, 10, 11, np.nan]
})

last_non_null = df.fillna(method='bfill').ffill().iloc[0]

print(last_non_null)
