import pandas as pd

# Load your data (assuming it's a csv file)
data = pd.read_csv('data.csv')

# Get the data in the Index (as array)
index_data = data.index.to_list()
