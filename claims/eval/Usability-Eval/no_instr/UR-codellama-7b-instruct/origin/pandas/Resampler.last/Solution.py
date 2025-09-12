
import pandas as pd

# Compute the last non-null entry of each column
df = pd.read_csv("data.csv")
for col in df.columns:
    last_non_null_entry = df[col].notna().idxmax()
    print(f"Last non-null entry in {col} is {last_non_null_entry}")
