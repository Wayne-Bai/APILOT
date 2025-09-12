import pandas as pd

# Assuming df is your DataFrame
df = pd.read_csv('your_file.csv')

# Attempt to infer better dtypes for object columns
df = df.infer_objects()

# Convert object columns to appropriate data types
for col in df.select_dtypes(include=['object']).columns:
    try:
        df[col] = pd.to_numeric(df[col])
    except ValueError:
        pass

# Display the DataFrame
print(df)
