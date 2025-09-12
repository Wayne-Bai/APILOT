import pandas as pd

# Load pickled pandas object from file
with open('file.pkl', 'rb') as f:
    df = pd.read_pickle(f)
