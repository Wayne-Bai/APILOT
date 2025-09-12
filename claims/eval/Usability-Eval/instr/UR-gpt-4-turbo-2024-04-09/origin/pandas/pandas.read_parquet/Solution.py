import pandas as pd

# Load a parquet file into a DataFrame
file_path = 'path_to_your_parquet_file.parquet'
df = pd.read_parquet(file_path)

print(df)
