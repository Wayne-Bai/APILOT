
import joblib

# Load the joblib data from a file
data = joblib.load('file_name.joblib')

# Reconstruct the original Python object from the joblib data
object = joblib.loads(data)

print(object) # Print the reconstructed object
