import joblib

# Load the pickled object from the file
with open('filename.pkl', 'rb') as f:
    obj = joblib.load(f)
