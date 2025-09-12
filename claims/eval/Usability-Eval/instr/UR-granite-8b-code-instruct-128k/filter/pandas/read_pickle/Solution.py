
import pandas as pd

# Load pickled pandas object from file
def load_pickle(file_path):
    df = pd.read_pickle(file_path)
    return df
