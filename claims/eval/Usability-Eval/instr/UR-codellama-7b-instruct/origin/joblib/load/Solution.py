
import joblib

# Load the object from the file using joblib.load()
with open('object_file', 'rb') as f:
    obj = joblib.load(f)

print(obj)
