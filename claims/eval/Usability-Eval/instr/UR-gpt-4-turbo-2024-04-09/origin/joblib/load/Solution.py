import joblib

# Path to the file from which to load the object
file_path = 'your_file_path.pkl'

# Load the object from the file
loaded_object = joblib.load(file_path)

# Now you can use loaded_object as needed
print(loaded_object)
