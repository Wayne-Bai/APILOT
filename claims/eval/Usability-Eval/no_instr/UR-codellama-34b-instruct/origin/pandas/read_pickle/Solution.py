import pandas as pd

# Load the pickled pandas object from a file
with open('data.pkl', 'rb') as file:
    df = pd.read_pickle(file)

print(df.head())
