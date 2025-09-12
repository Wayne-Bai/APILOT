# Import necessary libraries
from joblib import load

# Path to saved model
model_file = '/path/to/your/model.joblib'

# Load model from file
loaded_model = load(model_file)

# Now you can use loaded_model for further use
# For example, predicting on some data
input_data = [...] # replace [...] with your own input data
prediction = loaded_model.predict(input_data)
print("Model prediction: ", prediction)
