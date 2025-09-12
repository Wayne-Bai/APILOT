import pandas as pd

# Load a pickled DataFrame from a file
with open('data.pkl', 'rb') as file:
    data = pd.read_pickle(file)

print(data)
