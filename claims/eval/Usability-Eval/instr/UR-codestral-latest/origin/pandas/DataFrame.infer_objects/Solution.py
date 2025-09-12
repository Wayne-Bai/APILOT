import pandas as pd

# Load the CSV file
df = pd.read_csv('your_file.csv')

# Display the initial data types
print(df.dtypes)

# Convert object columns to category if low cardinality
for col in df.select_dtypes(include=['object']).columns:
    if df[col].nunique() < df.shape[0] * 0.5:
        df[col] = df[col].astype('category')

# Display the inferred data types
print(df.dtypes)
