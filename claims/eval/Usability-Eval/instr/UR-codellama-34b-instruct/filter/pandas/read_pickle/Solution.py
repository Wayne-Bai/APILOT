
import pandas as pd

# Load the pickled object from the file
with open('data.pkl', 'rb') as f:
    df = pd.read_pickle(f)

print(df)
