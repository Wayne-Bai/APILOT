import pandas as pd

def load_parquet(file_path):
    df = pd.read_parquet(file_path)
    return df
