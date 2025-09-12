import joblib

# Let's assume we have a Python object named 'my_object' that we want to persist
my_object = {
    'key1': 'value1',
    'key2': 'value2'
}

# Persist the object to a file
with open('my_object.joblib', 'wb') as file:
    joblib.dump(my_object, file)

# Now, let's reconstruct the object from the file
with open('my_object.joblib', 'rb') as file:
    reconstructed_object = joblib.load(file)

# Print the reconstructed object
print(reconstructed_object)
