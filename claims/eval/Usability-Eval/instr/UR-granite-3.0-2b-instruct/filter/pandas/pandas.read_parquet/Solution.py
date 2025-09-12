import pandas as pd

def load_parquet(file_path):
    return pd.read_parquet(file_path)
