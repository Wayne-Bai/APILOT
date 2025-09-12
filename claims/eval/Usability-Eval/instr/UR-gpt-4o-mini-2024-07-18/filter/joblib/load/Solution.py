import joblib

# Reconstruct the Python object from the file
filename = 'your_file_path.pkl'  # Replace with your file path
reconstructed_object = joblib.load(filename)

# Use the reconstructed_object as needed
print(reconstructed_object)
