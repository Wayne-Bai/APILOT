import pandas as pd

# Load a parquet object from the file path, returning a DataFrame
def load_parquet_to_dataframe(file_path):
    df = pd.read_parquet(file_path)
    return df
