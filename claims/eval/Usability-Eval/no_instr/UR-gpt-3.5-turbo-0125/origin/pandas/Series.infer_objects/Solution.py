
import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3],
        'B': ['x', 'y', 'z'],
        'C': [True, False, True]}

df = pd.DataFrame(data)

# Inferring better dtypes for object columns
for col in df.select_dtypes(include='object'):
    df[col] = pd.to_numeric(df[col], errors='ignore')

print(df.dtypes)
