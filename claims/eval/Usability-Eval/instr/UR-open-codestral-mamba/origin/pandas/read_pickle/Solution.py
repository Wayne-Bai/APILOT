import pandas as pd
import pickle

# Load the pickled pandas object
with open('filename.pkl', 'rb') as f:
    df = pickle.load(f)

# Now, you can use the `df` variable for further analysis
print(df.head())
