import pandas as pd

def load_pickled_object(file_path):
    return pd.read_pickle(file_path)
