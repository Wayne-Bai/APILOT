import pandas as pd

# Replace this with your own file path
file_path = "example.parquet"

# Load the parquet object into a DataFrame
df = pd.read_parquet(file_path)

print(df)
