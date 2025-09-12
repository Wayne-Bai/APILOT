import joblib

# Specify the file path where the object is saved
filename = 'path_to_your_file'

# Load the object from the file
loaded_obj = joblib.load(filename)

print(loaded_obj)
