import joblib

# Save the object to a file
joblib.dump(my_object, 'my_object.joblib')

# Load the object from the file
loaded_object = joblib.load('my_object.joblib')
