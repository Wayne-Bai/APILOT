import pandas as pd

# Load a pickled pandas object from a file
file_path = 'path_to_your_file.pkl'  # Replace with your actual file path
df = pd.read_pickle(file_path)

# Display the loaded DataFrame
print(df)
