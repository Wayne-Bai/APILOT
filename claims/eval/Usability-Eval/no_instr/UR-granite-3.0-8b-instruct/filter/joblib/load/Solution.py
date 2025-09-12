import joblib

# Let's assume we have a Python object named 'data' that we want to persist to a file
data = {"key": "value"}

# Use joblib.dump to persist the object to a file
joblib.dump(data, "data.joblib")

# Now, let's load the object back from the file
loaded_data = joblib.load("data.joblib")

# Print the loaded data
print(loaded_data)
