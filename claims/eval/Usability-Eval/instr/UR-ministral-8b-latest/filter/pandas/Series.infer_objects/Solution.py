import pandas as pd

# Function to infer dtypes based on column values
def infer_dtypes(series):
    if pd.api.types.is_numeric_dtype(series):
        return pd.to_numeric(series, errors='coerce')
    elif pd.api.types.is_datetime64_any_dtype(series):
        return pd.to_datetime(series, errors='coerce')
    else:
        return series.astype('category')

# Example DataFrame with object columns
df = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', 'not-a-date'],
    'Number': ['123', '456', '789', 'not-a-number'],
    'Category': ['A', 'B', 'C', 'Other']
})

# Apply the function to each object column
for col in df.columns:
    df[col] = infer_dtypes(df[col])

print(df)
