import pandas as pd

# Load a pickled pandas object from file
file_path = 'your_file_path.pkl'
data = pd.read_pickle(file_path)

# Display the loaded data
print(data)
