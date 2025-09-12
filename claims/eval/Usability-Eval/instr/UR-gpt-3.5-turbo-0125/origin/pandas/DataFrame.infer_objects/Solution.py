
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3],
        'B': ['x', 'y', 'z'],
        'C': ['2022-01-01', '2023-02-02', '2024-03-03']}
df = pd.DataFrame(data)

# Inferring better dtypes for object columns
for col in df.select_dtypes(include='object'):
    converted_col = pd.to_datetime(df[col], errors='ignore', format='%Y-%m-%d')
    if pd.api.types.is_datetime64_ns_dtype(converted_col.dtype):
        df[col] = converted_col

print(df.dtypes)
