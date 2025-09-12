import pandas as pd

# Let's assume df is the DataFrame and 'col1', 'col2' are the object columns
df = pd.read_csv('your_file.csv')

# Infer the best dtype for object columns
for col in ['col1', 'col2']:
    df[col] = pd.to_numeric(df[col], errors='ignore')
