import pandas as pd

# Load a parquet object from the file path, returning a DataFrame
file_path = 'path/to/your/file.parquet'
df = pd.read_parquet(file_path)
