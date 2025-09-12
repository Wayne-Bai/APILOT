import pandas as pd

# Sample DataFrame
data = {
    'A': ['1', '2', '3'],
    'B': ['4.5', '5.6', '6.7'],
    'C': ['True', 'False', 'True'],
    'D': ['2023-01-01', '2023-01-02', '2023-01-03']
}

df = pd.DataFrame(data)

# Attempt to infer better dtypes for object columns
df = df.apply(pd.to_numeric, errors='ignore')
df['C'] = df['C'].astype('bool')
df['D'] = pd.to_datetime(df['D'])

print(df.dtypes)
