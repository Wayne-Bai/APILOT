import pandas as pd
import pickle

# Load pickled pandas object (or any object) from file
with open('your_file.pkl', 'rb') as file:
    data = pickle.load(file)
