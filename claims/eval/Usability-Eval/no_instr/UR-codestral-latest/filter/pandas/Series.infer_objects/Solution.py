import pandas as pd

# Load the data
df = pd.read_csv('your_data.csv')

# Iterate through columns
for col in df.columns:
    if df[col].dtype == 'object':
        # Infer better dtype
        df[col] = pd.to_numeric(df[col], errors='ignore')
