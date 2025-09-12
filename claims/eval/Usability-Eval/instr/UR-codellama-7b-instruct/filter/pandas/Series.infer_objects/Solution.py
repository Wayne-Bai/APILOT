
import pandas as pd

# Read CSV file into a pandas DataFrame
df = pd.read_csv("data.csv")

# Infer better dtypes for object columns
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].astype('category')

# Convert to categorical data type
df = pd.get_dummies(df)
