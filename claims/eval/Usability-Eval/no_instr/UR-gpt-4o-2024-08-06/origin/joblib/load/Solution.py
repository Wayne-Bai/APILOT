import joblib

# Specify the file path where the object was saved
file_path = 'saved_object.pkl'

# Load the object from the specified file path
loaded_object = joblib.load(file_path)

# Now you can use `loaded_object` in your program
print(loaded_object)
