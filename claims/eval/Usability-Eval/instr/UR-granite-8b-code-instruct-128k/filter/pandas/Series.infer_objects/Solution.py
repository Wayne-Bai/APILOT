import pandas as pd

# Load your data into a pandas DataFrame
df = pd.read_csv('your_data.csv')

# Infer better dtypes for object columns
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert any remaining object columns to category dtype
df['remaining_cols'] = df['remaining_cols'].astype('category')
