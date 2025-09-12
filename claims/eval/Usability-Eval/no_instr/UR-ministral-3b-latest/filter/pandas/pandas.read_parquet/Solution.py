import pandas as pd

def load_parquet(filepath):
    df = pd.read_parquet(filepath)
    return df
