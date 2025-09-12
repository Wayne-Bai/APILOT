
import pandas as pd
import pickle

# Load the pickled DataFrame or object from the file
with open('my_file.pkl', 'rb') as f:
    my_data = pickle.load(f)

# Print the loaded data to the console
print(my_data)
