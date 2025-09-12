import pandas as pd

# Path to the pickled file
file_path = 'your_file_path_here.pkl'

# Load the pickled pandas object
data = pd.read_pickle(file_path)

# Display the loaded data (optional)
print(data)
