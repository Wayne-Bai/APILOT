import joblib

# Load or reconstruct a Python object from a file
filename = 'my_object.pkl'
loaded_object = joblib.load(filename)

# Now you can use 'loaded_object' as needed
print(loaded_object)
