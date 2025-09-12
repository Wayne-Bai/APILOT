import joblib

# Load the persisted Python object from a file
file_path = 'your_model.pkl'  # Replace with your file path
loaded_object = joblib.load(file_path)

# You can now use the `loaded_object` as needed
# Example usage (assuming it's a model and you have some sample data):
# predictions = loaded_object.predict(sample_data)
