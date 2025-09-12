
import pandas as pd

def load_parquet_file(file_path):
    return pd.read_parquet(file_path)

# Example usage
file_path = "path_to_file.parquet"
df = load_parquet_file(file_path)
