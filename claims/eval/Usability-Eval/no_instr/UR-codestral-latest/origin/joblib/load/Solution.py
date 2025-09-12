# Import the joblib library
import joblib

# Reconstruct a Python object from a file persisted with joblib.dump
def load_object(filename):
    # Load object from the file
    loaded_object = joblib.load(filename)
    return loaded_object

# Usage
# filename = 'object_file.joblib'
# loaded_obj = load_object(filename)
