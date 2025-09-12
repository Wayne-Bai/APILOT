
import pandas as pd

# Load pickled pandas object from file
with open('data.pkl', 'rb') as file:
    data = pd.read_pickle(file)
