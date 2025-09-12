import pandas as pd

# The path to the pickled file
file_path = 'data.pkl'

# Load the pickled object
data = pd.read_pickle(file_path)

# Display the loaded data
print(data)
