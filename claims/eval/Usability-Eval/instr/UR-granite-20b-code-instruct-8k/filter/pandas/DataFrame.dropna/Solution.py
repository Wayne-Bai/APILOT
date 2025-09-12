import pandas as pd
df = pd.DataFrame({'A': [1, 2, None], 'B': [4, 5, 6]})
df.dropna(inplace=True)
print(df)
