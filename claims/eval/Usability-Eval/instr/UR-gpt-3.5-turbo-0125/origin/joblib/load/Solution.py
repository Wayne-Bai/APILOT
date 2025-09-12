
import joblib

# Load the object from file
filename = 'saved_object.joblib'
loaded_object = joblib.load(filename)

print(loaded_object)
