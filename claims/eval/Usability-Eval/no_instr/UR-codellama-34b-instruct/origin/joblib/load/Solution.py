
import joblib

# Load the serialized object from the file
with open('object_file', 'rb') as f:
    obj = joblib.load(f)

print(obj)  # Output the reconstructed Python object
