import pandas as pd

# Specify the file path of the pickled object
file_path = 'path_to_pickle_file.pkl'

# Load the pickled object using pandas
df = pd.read_pickle(file_path)

# Optionally, print the DataFrame to verify contents
print(df)
