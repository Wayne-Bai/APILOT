import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 3, 2]})
result = df.idxmax(axis=1)
print(result)
