import pandas as pd

# Load your data into a DataFrame
df = pd.read_csv('your_data.csv')

# Infer better dtypes for object columns
object_cols = df.select_dtypes(include=['object']).columns
for col in object_cols:
    df[col] = pd.to_datetime(df[col])
