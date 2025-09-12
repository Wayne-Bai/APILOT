import pandas as pd

# Sample DataFrame
data = {
    'A': ['1', '2', '3'],
    'B': ['4.5', '5.6', '6.7'],
    'C': ['True', 'False', 'True'],
    'D': ['2023-01-01', '2023-02-01', '2023-03-01']
}

df = pd.DataFrame(data)

# Attempt to infer better dtypes for object columns
for col in df.select_dtypes(include=['object']):
    try:
        df[col] = pd.to_numeric(df[col])
    except ValueError:
        try:
            df[col] = pd.to_datetime(df[col])
        except ValueError:
            try:
                df[col] = df[col].astype('bool')
            except ValueError:
                pass  # Keep as object if no better dtype can be inferred

print(df.dtypes)
