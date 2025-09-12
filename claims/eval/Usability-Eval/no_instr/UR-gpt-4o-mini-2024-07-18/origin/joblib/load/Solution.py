import joblib

# Load the Python object from a file
file_path = 'your_file_path.pkl'  # Replace with the path to your file
reconstructed_object = joblib.load(file_path)

# Now you can use the reconstructed_object as needed
print(reconstructed_object)
