import pandas as pd

# Sample DataFrame with object columns
data = {
    'A': ['1', '2', '3'],
    'B': ['true', 'false', 'true'],
    'C': ['2023-01-01', '2023-01-02', '2023-01-03']
}

df = pd.DataFrame(data)

# Attempt to infer better dtypes for object columns
df = df.infer_objects()

# Check dtypes of the DataFrame after conversion
print(df.dtypes)
