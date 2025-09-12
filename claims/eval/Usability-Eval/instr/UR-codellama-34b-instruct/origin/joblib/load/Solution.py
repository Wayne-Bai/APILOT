import joblib

# Load the serialized data from the file
with open('filename.joblib', 'rb') as f:
    data = joblib.load(f)

# Reconstruct the original Python object
obj = joblib.loads(data)

print(obj)
