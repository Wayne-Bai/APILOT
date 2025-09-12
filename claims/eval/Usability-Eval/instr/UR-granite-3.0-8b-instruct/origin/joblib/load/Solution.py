import joblib

# Let's assume that we have a Python object named 'my_object' that we want to persist
my_object = {'key1': 'value1', 'key2': 'value2'}

# We can persist the object to a file using joblib.dump
with open('my_object.jbl', 'wb') as file:
    joblib.dump(my_object, file)

# To reconstruct the object from the file, we can use joblib.load
with open('my_object.jbl', 'rb') as file:
    reconstructed_object = joblib.load(file)

# Now, 'reconstructed_object' should be an exact copy of 'my_object'
print(reconstructed_object)
