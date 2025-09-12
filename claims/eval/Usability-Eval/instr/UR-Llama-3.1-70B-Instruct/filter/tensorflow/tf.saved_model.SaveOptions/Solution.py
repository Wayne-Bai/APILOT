import tensorflow as tf

# Define a simple model
class MyModel(tf.Module):
    def __init__(self):
        self.var = tf.Variable(42.0)
        self.bias = tf.Variable(1.0)

    def __call__(self, x):
        return self.var * x + self.bias

# Create an instance of the model
model = MyModel()

# Save the model to SavedModel format
tf.saved_model.save(model, "path_to_saved_model")

# Alternatively, you can save the model using the save method with options
options = tf.saved_model.SaveOptions(namespace_whitelist=["namespace1", "namespace2"])
tf.saved_model.save(model, "path_to_saved_model", options=options)

# Load the saved model
loaded_model = tf.saved_model.load("path_to_saved_model")

# Use the loaded model
print(loaded_model.var)
print(loaded_model.bias)

# Call the loaded model
print(loaded_model(tf.constant(2.0)))
