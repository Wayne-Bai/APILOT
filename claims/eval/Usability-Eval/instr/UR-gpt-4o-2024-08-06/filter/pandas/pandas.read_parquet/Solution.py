import pandas as pd

# Replace 'file_path.parquet' with the path to your parquet file
file_path = 'file_path.parquet'

# Load the parquet file into a DataFrame
df = pd.read_parquet(file_path)

# Displaying the DataFrame
print(df)
