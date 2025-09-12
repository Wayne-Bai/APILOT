
import pickle

# Open the file in read binary mode
with open('pickle_file.pkl', 'rb') as f:
    # Read the pickled object from the file
    obj = pickle.load(f)
