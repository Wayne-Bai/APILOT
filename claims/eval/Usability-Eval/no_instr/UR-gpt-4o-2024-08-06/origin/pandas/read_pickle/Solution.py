import pandas as pd

# Load a pickled pandas object from a file
file_path = 'your_file_path.pkl'
df = pd.read_pickle(file_path)

# Display the loaded dataframe
print(df)
