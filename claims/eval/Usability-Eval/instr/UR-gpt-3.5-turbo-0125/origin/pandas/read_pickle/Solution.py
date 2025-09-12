
import pandas as pd

# Load pickled pandas object from file
with open('file.pkl', 'rb') as file:
    data = pd.read_pickle(file)
