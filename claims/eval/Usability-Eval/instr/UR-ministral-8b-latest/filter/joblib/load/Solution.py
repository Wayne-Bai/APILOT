import joblib

# Function to reconstruct a Python object from a file persisted with joblib.dump
def reconstruct_object(filepath):
    # Load the object
    obj = joblib.load(filepath)
    return obj

# Example usage
filepath = 'path/to/your/file.pkl'
reconstructed_object = reconstruct_object(filepath)
print(reconstructed_object)
