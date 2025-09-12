import pandas as pd

# Load the data into a pandas dataframe
df = pd.read_csv('data.csv')

# Infer better dtypes for object columns
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Print the updated dataframe
print(df)
