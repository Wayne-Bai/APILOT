import pandas as pd

# Sample DataFrame
data = {
    'A': ['1', '2', '3'],
    'B': ['4.5', '5.6', '6.7'],
    'C': ['True', 'False', 'True'],
    'D': ['2023-10-01', '2023-10-02', '2023-10-03']
}

df = pd.DataFrame(data)

# Attempt to infer better dtypes for object columns
df = df.convert_dtypes()

print(df.dtypes)
