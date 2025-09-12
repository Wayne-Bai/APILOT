import joblib

# Load the pickled object from the file
with open('my_pickle.pkl', 'rb') as f:
    data = joblib.load(f)

# Reconstruct the object using the loaded data
obj = joblib.loads(data)
