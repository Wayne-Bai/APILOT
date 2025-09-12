import pandas as pd

def elementwise_func(x):
    return x**2

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = df[['A', 'B']].transform(elementwise_func)
print(df)
